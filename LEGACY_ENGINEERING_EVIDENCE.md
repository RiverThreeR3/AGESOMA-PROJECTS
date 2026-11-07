# Historical Engineering Evidence — Not InstantWork Outputs

**Archive index (2026-11-07).** Earlier AGESOMA technical work and studies existed before the decision that **all new AGESOMA delivery work must be executed through InstantWork**. Keep the record for provenance and reproducibility, but do **not** present it in the active InstantWork capability gallery.

## Standalone Knowledge API

The earlier [Knowledge API implementation PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) contains a deterministic FastAPI lexical-retrieval baseline over five fictional Markdown policy documents. It has document/line citations and explicit abstention, and it does **not** call an LLM or serve real documents.

An independent [retrieval-guardrail increment PR #7](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/7) added stricter lexical matches, numeric checks and adversarial regressions. The [CI run for commit `895c32f`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42372898957) previously passed 62 synthetic/unit tests and Docker checks on that branch.

An additional [business-simulation PR #8](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/8) executed **30 fictional queries in a standalone Python simulator**, yielding 20 expected passage/source matches and ten handoff drafts on authored examples. The [CI run at `1c25782`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42375020327) previously passed 71 tests and emitted an arithmetic handling-time model. The calculated minutes and percentages are **assumptions-based projections, not real business savings**.

**Execution provenance:** `projects/knowledge-api/` in this public portfolio. **Not executed by InstantWork. Not a real customer engagement. Not verified production deployment.** The PRs are historical review artifacts and their current state must be rechecked before updating status.

For the full original calculations, controls and reproduction instructions, see [SIMULATIONS.md](SIMULATIONS.md) and [CASE_STUDIES.md](CASE_STUDIES.md). These remain separated from the current [InstantWork capability register](CAPABILITIES.md).

## No backdated capability claims

If a knowledge-search adapter is later built **inside** InstantWork, document a **new** actual InstantWork work order with the exact integration revision, inputs, tests, permission controls, real executor and evidence. Do not relabel the old Python results as InstantWork work.
