export const meta = {
  name: 'uqs-repro-kumada',
  description: 'UQS reproducibility: kumada x {v18.4,v19} x N replicates, Sonnet 4.6 (model inherited from parent session)',
  phases: [
    { title: 'ModelGate', detail: '1-agent probe: abort unless agents run on claude-sonnet-4-6' },
    { title: 'Replicates', detail: 'one full S0->S2 pipeline per (version, replicate) cell' },
  ],
}

// ---------------------------------------------------------------------------
// Path B execution: run this ONLY from a Claude Code session whose main model
// is claude-sonnet-4-6. agent() calls OMIT the model override on purpose, so
// each agent INHERITS the parent session model (the model enum cannot name 4.6;
// "sonnet" would resolve to Sonnet 5 and void the experiment).
// Authoritative model gate is still repro_extract.py (model_ok filter); this
// probe just fails fast. Launch:  Workflow({ scriptPath: "papers/dev/kumada/repro_2026-07/repro_workflow.js" })
// Optional:  args = { N: 5 }
// ---------------------------------------------------------------------------

const N = (args && args.N) || 5
const VERSIONS = ['v184', 'v19']
const OUT = 'papers/dev/kumada/repro_2026-07'
const PDF = 'papers/dev/kumada/Kumada_1972.pdf'

function replicatePrompt(ver, k) {
  const pdir = `prompts/${ver}`
  const tag = `kumada_${ver}_sonnet46_repro_run${k}`
  return [
    'You are executing ONE independent UQS reproducibility replicate. Do NOT touch the',
    'production registry (papers/_database/uqs_analysis_registry.csv). Do NOT run /record.',
    '',
    `TARGET: ${PDF} is a JACS page with THREE communications. Analyze ONLY the MIDDLE one:`,
    'Tamao, Sumitani & Kumada, "Selective Carbon-Carbon Bond Formation by Cross-Coupling of',
    'Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes."',
    'Use the Stage 0 boundary procedure to isolate it (exclude the hydrosilylation paper before',
    'it and the chymotrypsin paper after it).',
    '',
    `PROMPTS: use ONLY the canonical files in ${pdir}: prompt_stage0_${ver}.md,`,
    `prompt_stage1_turn1..4_${ver}.md, prompt_stage2_${ver}.md (NO pilot/textbook turn4 variants).`,
    '',
    'RUN in THIS single context (do not split): Read the PDF, then S0 -> S1 turn1 -> turn2 ->',
    'turn3 -> turn4 -> S2, exactly per the prompts. Stage 2 must see the full PDF+S0+turn1-3 context.',
    '',
    'MODEL ID: Your system context tells you your exact model id. At the VERY FIRST LINE of the',
    'S0 file (before any UQS content), write EXACTLY this line (filling in your actual model id):',
    '<!-- model_info: claude-sonnet-4-6 -->',
    '(If your model id is NOT claude-sonnet-4-6, write that id instead and set saved=false.)',
    '',
    `SAVE with Write tool:`,
    `  ${OUT}/${tag}_s0.md  — first line: <!-- model_info: YOUR_ID -->, then the UQS S0 output`,
    `  ${OUT}/${tag}_s1.md  — the Turn 4 consolidated output (final S1 list, after all 4 turns)`,
    `  ${OUT}/${tag}_s2.md  — the S2 output verbatim`,
    '',
    'RETURN the structured object: model_info (the exact id you embedded in S0), saved (true only',
    'if all three files were written), nB (count of distinct B-items in your final S1).',
  ].join('\n')
}

const REP_SCHEMA = {
  type: 'object',
  properties: {
    model_info: { type: 'string' },
    saved: { type: 'boolean' },
    nB: { type: 'integer' },
  },
  required: ['model_info', 'saved'],
}

// ---- Phase 1: model gate --------------------------------------------------
phase('ModelGate')
const probe = await agent(
  'Report ONLY the exact model id the system reports you are running as, as a JSON object. Read and write nothing.',
  { label: 'model-probe', phase: 'ModelGate',
    schema: { type: 'object', properties: { model_info: { type: 'string' } }, required: ['model_info'] } }
)
log(`probe model_info = ${probe && probe.model_info}`)
if (!probe || !/sonnet-4-6/.test(String(probe.model_info || ''))) {
  throw new Error(
    `ABORT: agents report model "${probe && probe.model_info}", not claude-sonnet-4-6. ` +
    'Launch this workflow from a Claude Code session whose model IS Sonnet 4.6, and do not set a model override. ' +
    'If 4.6 is unavailable in your harness, the frozen-baseline reproduction is not possible here.'
  )
}

// ---- Phase 2: replicates (independent agents; each = one full pipeline) ----
phase('Replicates')
const cells = []
for (const ver of VERSIONS) for (let k = 1; k <= N; k++) cells.push({ ver, k })

const results = await parallel(cells.map(c => () =>
  agent(replicatePrompt(c.ver, c.k), { label: `${c.ver}/run${c.k}`, phase: 'Replicates', schema: REP_SCHEMA })
    .then(r => (r ? { ...c, ...r } : { ...c, saved: false, model_info: null }))
))

const done = results.filter(Boolean)
const on46 = done.filter(r => /sonnet-4-6/.test(String(r.model_info || '')) && r.saved)
log(`replicates saved on 4.6: ${on46.length}/${cells.length}`)
log('Next: python3 papers/dev/kumada/repro_2026-07/repro_extract.py && python3 .../repro_aggregate.py')
return { total: cells.length, on_46_saved: on46.length, cells: done }
