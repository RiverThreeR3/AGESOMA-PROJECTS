# Fictional Business Workload Simulations — Knowledge API

**Status: simulation code only, not a customer implementation or a production pilot.**

These two scenarios model realistic *types of work* described in recent public
requests for document-backed support and reliable business-process automation.
Neither scenario uses the private data or proprietary text of any buyer. We
do not claim that the 30 hand-authored queries represent actual platform demand
volume, real customer traffic, or measured company performance.

## Simulated workflows

1. **Customer support knowledge desk:** fictional policy questions produce a
   cited, extractive **draft for human review** when the expected evidence is
   present. Unsupported questions create a **human-handoff draft**.
2. **Internal operations knowledge desk:** fictional access, incident and
   billing policy questions take the same citation-or-handoff path.

The implementation is the *existing deterministic Knowledge API* plus
[`simulate_workload.py`](../simulate_workload.py). It does **not** implement
the requested commercial integrations (CRM, n8n, WhatsApp, PDF ingestion or
LLM-based answering). No messages or database writes occur.

### Reproduce the measured *code behavior*

From `projects/knowledge-api`:

```bash
python -m pip install -r requirements-dev.txt
python simulate_workload.py --format markdown
python simulate_workload.py --format json
python -m pytest -q
```

The [fictional workload fixture](workload_cases.json) contains **30 authored
cases: 15 for customer support and 15 for internal operations**.
For each query the simulator executes `KnowledgeIndex.search`, compares the
returned passage's source and expected excerpt substring to the fixture labels,
then emits a proposed decision:
- `cited_draft_for_human_review`: matching source **and** matching expected
  excerpt; a person must still check substantive correctness.
- `human_handoff_draft`: no verified match under the evaluator labels.
  The labeled evaluator is an **offline oracle unavailable in production**.

It separately counts unsafe/wrong candidates and false abstentions.
The CI gate fails if an authored unsupported or mismatched case would have
received a cited draft. This **does not prove** zero false answers in the wild.

### Explicit model assumptions — NOT observed savings

| Workflow | Hypothetical manual handling | Hypothetical review of supported draft | Unsupported / incorrect candidates |
| --- | ---: | ---: | --- |
| Customer support | 6 minutes/ticket | 1 minute/ticket | Full 6 minutes, routed for human work |
| Internal operations | 8 minutes/ticket | 2 minutes/ticket | Full 8 minutes, routed for human work |

The report adds *assumed* manual minutes, counts reviewed drafts, and subtracts
*modeled* assisted minutes. These are arithmetic **scenario outputs**, not
measured process times, financial savings, real resolution rate or ROI.
There is no estimate of real-world support quality, payroll, uptime or
deployment cost. The chosen workload frequencies are deliberately not used
to extrapolate to an unmeasured population.

### How this connects to buyer requests

The modeled requirements mirror two broad requests seen in public briefs:
source-backed policy answers with citations/abstention and business workflows
with human escalation and auditable states. Full customer requirements usually
also include integrations, identity and permissions, data ingestion, and
operating reliability. **None of those missing capabilities is implied by
this demonstration**. Market sources are reviewed separately; the company
homepage shows only the code and verified evaluation.

### Releasing a genuine pilot would require

An independent unseen evaluation set, real authentication and tenant-scoped
permissions, customer-approved ingestion and consent, CRM connector
idempotency/failure-retry testing, reviewer workflow, actual timing measurement,
load/security assessment, deployment and rollback plan. Obtain written approval
before accessing real data or initiating any outbound action.
