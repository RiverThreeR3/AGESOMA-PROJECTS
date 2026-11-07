# AGESOMA Website ↔ Project Portfolio — Alignment Contract

**Established:** 2026-11-04  
**Existing website:** [agesoma.vercel.app](https://agesoma.vercel.app), Vercel project `agesoma`.  
**Scope:** keep the **existing AGESOMA company website** aligned with the evidence-backed InstantWork product proposition, its demonstrated business-work capabilities and the separate AGESOMA business units. A product-sales page must not describe proposed demos as delivered work. This is a reconciliation policy, **not proof of current site synchronization**, public accessibility, live launches or customer outcomes.

## Company architecture: one website, distinct proof sources

| Website area | Canonical upstream evidence | Rule for inclusion | Current verification boundary |
| --- | --- | --- | --- |
| **InstantWork product** | [README.md](README.md), [CAPABILITIES.md](CAPABILITIES.md) and [DEMONSTRATIONS.md](DEMONSTRATIONS.md) in AGESOMA-PROJECTS; actual engineering in private `AGESOMA/InstantWork` | Present **one business-work execution product**, with status-separated actual demonstrations and independent evidence; no checkout, customer ROI or live automation claims without release gates | Private laboratory/preproduction; the new demo roadmap is NOT six completed examples |
| **Older independent engineering** | [LEGACY_ENGINEERING_EVIDENCE.md](LEGACY_ENGINEERING_EVIDENCE.md) and archived Knowledge API cases | Link only from a clearly labeled historical evidence area if relevant; do not count as active InstantWork capabilities or homepage sales proof | Knowledge API Python simulator was NOT executed by InstantWork |
| **Other AGESOMA case studies** | Approved original public source/PR, CI, reproducible eval, sanitized demo and publication permission | Include only what exists, with status and limitations; no fabricated clients, revenue or test outcomes | Project specifications are proposals, not delivered work |
| **App Factory / AGESOMA-owned products** | Verified product's authorized *public* repository, domain/app-store listing, actual release and availability evidence; research from the existing **AGESOMA — App da Semana** weekly workflow | The site may list published products and explicitly labeled authentic betas. **Weekly app research and app concepts are not launched products.** Never reveal internal/private product code or unapproved brand plans | The weekly research pipeline does not itself verify a public launch |
| **Brands INSTANT / DOTS / AGE** | Authorized public brand assets, verifiable product pages or release links; AGESOMA App Factory's brand categorization | Treat as **distinct product lines** under AGESOMA only when publication is approved; keep product identities distinct. Do not conflate AGE brand line with AGESOMA company | Do not infer public availability from a planned app or design assignment |
| **Founder, engineering and recruitment** | [Raphael's AI Engineer public recruiter guide](https://github.com/RiverThreeR3/AIEngineer/blob/main/docs/RECRUITER_GUIDE.md) and evidence links | Founder profile belongs in **About**; link personal portfolio and offer recruiting info separately from business lead conversion | Private CV, personal interview answers, course progress and learner tracker must never appear on the public website |

### Publishability status ladder (must be explicit)

`Research` → `Concept` → `In development / open PR` → `Privately tested` → `Public beta` → `Available / publicly deployed` → `Verified customer case`.

Each step needs **its own independently verified evidence**. A `READY` Vercel deployment is not proof of anonymous public access. An AGESOMA-owned app may have its own deployment without being connected to this website. Do not list concepts as released products. A claimed customer case requires customer permission and observable outcome evidence.

## Required project-to-site traceability record

For every site service, case study, app, or brand card, maintain a reviewable record with:

| Field | Meaning |
| --- | --- |
| `site_section` | Services, Engineering Work, Products, About, Contact |
| `business_line` | AI Engineering, App Factory (INSTANT/DOTS/AGE), or Founder |
| `public_name` and `owner_approval` | The user-approved public label and proof it may be published |
| `canonical_source_url` | Public GitHub PR/repository, product website, or app-store listing |
| `exact_revision` | PR state, commit SHA, release number and last observed date |
| `evidence_type` | Plan, source code, local test, CI at SHA, public beta, independently observed deployment, client outcome |
| `actual_status` | One of the publishability labels above |
| `claims_and_limits` | Accurate scope, measured metrics only when evidenced, known constraints |
| `target_site_link` | Public product/case URL if it exists and works; otherwise omit |
| `last_verified_site_version` | Vercel deployment/alias, content snapshot and visitor-access test |
| `sync_state` | `ALIGNED`, `CONTENT CHANGE PROPOSED`, `IN REVIEW`, `DEPLOYED NOT TESTED`, `VERIFIED LIVE`, `BLOCKED` |
| `next_action` | Named smallest fix/test, source owner and approval needed |

**Never infer evidence or URLs from a product name.** A GitHub document referencing a project does not establish its latest release status. Only owner-approved material goes to the public site.

## Change triggers and workflow

1. **New public project milestone** — compare that project's approved published state with site cards, service copy, hero, case link and CTA. Produce a change proposal; no automatic website update.
2. **New app launched or genuinely accessible beta** — verify public URL or store listing, release status, screenshots usage rights, privacy disclosures and functional access before proposing a product card.
3. **New actual InstantWork evidence** — once an InstantWork work order passes defined QA or authorized provider acceptance, propose an updated product-demo card linked to [DEMONSTRATIONS.md](DEMONSTRATIONS.md) with public-safe artifacts and precise status. Upwork/Workana briefs are read-only technical requirement signals (small, dated samples), not client wins. LinkedIn career scouting remains separate and does not populate product marketing.
4. **New product idea from App Factory** — record in the **private/research pipeline** only; do not publicly advertise the idea, copy competitor claims, or imply it's available.
5. **Change in proof state** — when CI breaks, PR changes, deployment is withdrawn, or a case's scope changes, downgrade the public claim promptly through the approved source/release process.
6. **Weekly reconciliation** — compare AGESOMA-PROJECTS case/service evidence, authorized App Factory product releases, the existing Vercel site, and Raphael's separate public recruiter profile. Generate one concise `SITE ↔ PROJECTS DELTA`: additions, outdated copy, working links, verified status, risk and next safe action.

## Release policy (do not skip)

- Preserve the existing Vercel `agesoma` project and production alias. **Do not create a second AGESOMA website.**
- Before editing code, identify and gain access to its **actual editable source**. The current Vercel deployment's Git repository and commit were **not** established by prior inspection.
- Validate anonymous access and protection configuration. Do not change authentication/SSO or domain/DNS without authorization.
- Use a reviewed **preview deployment**, verify desktop/mobile/accessibility/links/consent, and explicitly approve production changes; maintain rollback reference.
- Report **deployed status only from Vercel evidence**, and **site live only after an unauthenticated visitor test**. No speculative SEO, traffic, leads, pricing or ROI.
- Keep private client data, commercial secrets, application credentials, GitHub private repos, personal CV and interview/learning scores out of all public repositories and website copy.

## Roles of the existing routines — no duplicate scheduling

**Daily "AI Engineer — Raphael + AGESOMA PROJECTS"**: uses the single commercial source of truth and Vercel deployment data to propose site copy changes in the existing BUILD/AUDIT workflow. Monday reviews only verified LinkedIn demand; archived Workana/Upwork examples are not actively monitored. Sunday verifies website↔service claims↔technical evidence↔personal recruiter links.

**Weekly "AGESOMA — App da Semana"**: studies product opportunities. Its output may suggest a **private** future website entry, but only verified public AGESOMA-owned product releases or approved betas are eligible for public listings. That weekly task must **not** deploy or edit the site directly.

**Conflict rule:** when research marketing copy conflicts with verified project source/CI/deployment, project evidence controls the public claim. On a conflict, mark `BLOCKED / NEEDS REVIEW`, not `ALIGNED`.

For existing-site architecture and technical inspection, see [SITE_INTEGRATION_PLAN.md](SITE_INTEGRATION_PLAN.md).
