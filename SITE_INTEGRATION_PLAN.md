# AGESOMA — Existing Vercel Website Integration & Release Plan

**Audit date:** 2026-11-04  
**Scope:** preserve and improve the **existing** Vercel project `agesoma`; do not create another site or duplicate the marketing stack.  
**Change status:** Planning and source inspection only. No production code or Vercel configuration has been modified by this plan.

## Verified Vercel baseline

| Item | Verified result | What this does **not** prove |
| --- | --- | --- |
| Project | `agesoma` in the existing Vercel workspace | That GitHub is connected to its source |
| Canonical configured domain | [agesoma.vercel.app](https://agesoma.vercel.app) (domain verified, attached to the project and latest production deployment alias) | Anonymous visitor accessibility |
| Latest production deployment | `dpl_9GUpJaJCFH2YnVchoNjpuDx2bnV1` (`READY`) | That the site is live to the public or commercially ready |
| Production inspector | [Vercel deployment](https://vercel.com/teenagemutantninjaturtles/agesoma/9GUpJaJCFH2YnVchoNjpuDx2bnV1) | Public viewing rights |
| Protection | Vercel Authentication/SSO is enabled in the project settings | Actual unauthenticated behavior of each production alias |
| Deployment file tree | Static `src/index.html`, `src/assets/styles.css`, images/fonts, `src/robots.txt`, `src/vercel.json` | That this is the complete editable source repository |
| Git source | The deployment record showed no Git source commit/branch, and `agesoma` did not appear among discovered Git-linked projects | A definitive statement that no original source repository exists anywhere |
| Website metadata | `<title>Raphael Ribeiro · Founder & AI Engineer at AGESOMA</title>`; description emphasizes founder, remote roles and freelance work | Full inspection of every visible page section |

**Inspection limitations:** The deployment source API returned only the beginning of `index.html` before truncation. Direct public-site inspection was unsuccessful, so the exact visitor experience, all links, page-body copy and conversion analytics remain **unverified**. The project details also reported `live: false` alongside a `READY` deployment; verify actual anonymous access before describing the site as publicly operational.

## Portfolio-wide project alignment gate

**The AGESOMA website must evolve in lockstep with approved, independently verified AGESOMA projects, not only current AI Engineering services.** The [Website ↔ Project Alignment Contract](WEBSITE_PROJECT_SYNC.md) is the canonical content traceability policy for commercial services, technical case studies, verified App Factory products, and only owner-approved public INSTANT/DOTS/AGE product lines. Planned or internally researched apps are not public launches.

Before any site refinement, compare each proposed page section against its authoritative repository, current project stage, release/deployment state, independently observed result, brand/publication approval and authorized product link. Produce a concrete `SITE ↔ PROJECTS DELTA` and propose small reviewed site edits; do **not** modify or deploy the existing Vercel website without confirming editable source, preview evidence, anonymous access and permission to release. Reconcile outdated claims in both directions, including removal/downgrading of obsolete case claims.

## Main commercial alignment problem

The current **title and page description** prioritize a personal founder/AI Engineer job-search identity. AGESOMA now also has a separate public company capability and evidence hub at [AGESOMA-PROJECTS](https://github.com/RiverThreeR3/AGESOMA-PROJECTS). A buyer should immediately understand what business problem AGESOMA solves, how a scoped engagement works, which examples are real and how to inquire. Retain an authentic founder identity, but move recruiting information to an **About/Founder** or clearly separated personal link rather than mixing a job-seeker CTA with the primary customer CTA.

## Proposed company-first information architecture

1. **Hero:** AGESOMA | AI Engineering for reliable business operations. Explain results without promising unmeasured ROI. Main action: `Discuss an AI Integration Project` — only connect to a **confirmed owner-approved, functioning** contact destination; do not invent an email, form or appointment link.
2. **Services:** Five cards grounded in [SERVICES.md](SERVICES.md): workflow/CRM/n8n integrations; enterprise knowledge/RAG; permissioned business agents; multi-tenant support copilots; LLM reliability/cost and evaluations. Label each as an offered service, not a delivered customer contract.
3. **How we work:** scoped discovery → measurable baseline → API/integration implementation → authorization/negative testing → independently evidenced pilot/handoff → optional support.
4. **Proof:** deep links to [AGESOMA-PROJECTS case specifications](CASE_STUDIES.md) and the active [Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), **explicitly in review, not deployed/client-validated**. Show measured numbers, live demos or logos only after evidence exists and publication permission is verified.
5. **Founder:** link to Raphael's [personal AI Engineer technical portfolio](https://github.com/RiverThreeR3/AIEngineer) without exposing the private CV, interview history or private learning tracker.
6. **Contact:** a verifiably functioning and consent-compliant inquiry mechanism; clear privacy statement before collecting personal data.

### Suggested navigation

`Services` · `Technical Evidence` · `Process` · `About` · `Contact`

A recruiter can still reach the founder's separate [public recruiter guide](https://github.com/RiverThreeR3/AIEngineer/blob/main/docs/RECRUITER_GUIDE.md); it should not displace the commercial conversion goal.

## Release and integration gates — do not deploy blindly

1. **Source ownership:** identify the real editable repository or source archive behind the existing deployment, establish who owns it and preserve the current deployment as rollback reference. Avoid guessing a linked Git repo or copying a private AGESOMA codebase.
2. **Visitor access:** test `https://agesoma.vercel.app` and any final custom domain in an anonymous browser; log HTTP response, SSO gating, redirects, mobile and navigation. Do not disable deployment protection without owner review.
3. **Content truthfulness:** compare current page headings, links, services, case claims, and CTAs against `SERVICES.md`, `CASE_STUDIES.md`, `MARKET_SIGNAL_WATCHLIST.md` and actual GitHub project PR/CI statuses.
4. **Accessible design:** retain existing approved visual assets and layout where possible; measure responsiveness, contrast, keyboard access, heading structure, load behavior and image alt labels.
5. **SEO/content:** once the intended production URL is confirmed, audit title/description, canonical, OG image/URL, robots/sitemap policy and service semantics. Current document metadata is founder-first; proposed company-first wording needs owner review.
6. **Conversion:** connect a validated business CTA with consent/privacy and optional event measurement only if explicitly approved; never invent inbound-lead data or insert analytics credentials.
7. **Engineering:** preview on a reviewed branch with actual build/toolchain, functional smoke tests and link checking; verify the exact code revision and deploy target. Approve a **preview** before changing the existing production project. Do not silently alter DNS or deploy a replacement website.
8. **Post-release:** confirm live production alias and external access, service links, response errors, performance and a rollback path. Record observed before/after findings, not assumed success.

## One existing commercial research & engineering routine

The existing combined Raphael AI Engineer + AGESOMA PROJECTS scheduled workflow should:

- **Monday:** review dated LinkedIn-only remote freelance/contract opportunities eligible to Brazil, separating these from salaried hiring-skill signals; produce a scoped site-services delta without publishing. Workana/Upwork citations previously recorded are archival context, not sources for new searches in this routine. Update offer priority only with verified linked evidence.
- **BUILD/AUDIT days:** improve or independently test the one active original Knowledge API project, and only connect a site case claim when verifiable.
- **Sunday:** reconcile current Vercel project/domain/deploy, site copy, the AGESOMA service catalogue, actual case PR/test evidence, the personal recruiter guide, and the private CV (without publishing its data). Record `VERIFIED / PENDING / BLOCKED` and exact missing permissions.

**Commercial success criterion:** a prospect can reach an accurate service description, understand a safe scope, independently inspect available technical evidence, and use an owner-validated contact route. We cannot claim this is achieved until the site is inspected and tested.

## Privacy and authorization

Never copy data from the private AGESOMA repository, create additional public sites, expose Vercel tokens, publish private learner grades/resume/contact details or client information, modify DNS/SSO, deploy to production, or automate recruiter/client contact without explicit authorization.
