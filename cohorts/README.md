# Cohorts

The current curriculum — every module, unit, image and notebook — lives at the
**repository root**, not here. `cohorts/<year>/` holds only what is specific to
one delivery of the course: dates, homework, and (for a past cohort) a frozen
copy of the curriculum as it was taught that year.

**2026 is the current cohort. Fix curriculum at the repository root, not
inside `cohorts/2026/`.** This is recorded once, machine-readably, at the
root: `course.yaml:current_cohort` names it, and it must match the one
`cohorts/<year>/cohort.yaml` that declares `curriculum: current`.

## Layout

```
<repo root>/
├── course.yaml                   # course identity, incl. the description
├── 01-intro/                     # the directory name IS the module slug
│   ├── module.yaml                # module identity and unit list
│   ├── README.md                  # GitHub-facing module index, not published
│   ├── 01-what-is-ml.md           # units: NN-kebab.md, the stem IS the unit slug
│   ├── 02-ml-vs-rules.md
│   ├── images/                    # every image the module's units reference
│   └── notebooks/                 # notebooks and scripts the units link
├── ...
└── cohorts/
    ├── README.md                  # this file
    ├── 2026/                      # the directory name IS the cohort identifier
    │   ├── cohort.yaml            # dates, curriculum: current, homework list
    │   ├── README.md              # the human-readable schedule
    │   ├── article.md             # non-module cohort material is allowed
    │   ├── projects.md
    │   └── homework/
    │       ├── 01-intro/
    │       │   ├── homework.md    # homework instructions, fixed name
    │       │   └── homework.yaml  # homework identity, due date, form, questions
    │       └── ...
    ├── 2025/                      # earlier cohorts: frozen, full copies
    └── 2021 … 2024/
```

Two rules carry most of the weight:

- **Names are identity.** The module slug and the unit slug are the directory
  and file names. Nothing in YAML restates them, and renaming one moves a
  published URL.
- **A module directory is self-contained.** Its units, images and notebooks
  live inside it, units are siblings of `module.yaml`, and a relative link
  never climbs past the module directory except into a sibling module or the
  repository root. Anything further away is written as an absolute GitHub URL.

## Current cohort vs. frozen cohort

A cohort's `cohort.yaml` says which kind it is:

- **`curriculum: current`** — the cohort teaches whatever is currently at the
  repository root. `cohorts/<year>/` carries only dates and homework
  (`cohorts/<year>/homework/<module>/`); there is no module or lesson content
  here to duplicate or drift from the root.
- **`curriculum: github_archive`** — the cohort's curriculum was materially
  different from what root teaches now, so it was frozen: a full, standalone
  copy of every module it taught, byte-for-byte, under
  `cohorts/<year>/<module>/`. It is kept for GitHub readers only and is never
  re-imported as current module or lesson content.

Freezing happens once, when a cohort's curriculum is about to be superseded at
the root (typically when the next cohort starts): copy the outgoing root
modules into `cohorts/<year>/`, then edit root for the new cohort. Until that
happens, editing root fixes the live cohort immediately — there is no separate
copy to keep in sync.

## Editing

- Fix curriculum content (lessons, images, notebooks) at the **repository
  root**. That is where pull requests for the current cohort are accepted.
- Fix dates or homework for the current cohort under `cohorts/2026/`.
- Earlier, frozen cohorts are archives: the drift is the record of what was
  actually taught. Backport only factual or breaking errors, and do it
  per-cohort explicitly.
- A published slug is frozen. Renaming one is a platform decision, not a
  repository pull request.

## The conventions themselves

This repository does not restate them. `DataTalksClub/zoomcamp-ops` is the
authority: `STRUCTURE.md` for the repository layout and
`docs/shared-curriculum-v2.md` for the shared-root schema this repository
follows, plus the curriculum contract documented beside it for the YAML
schemas and the unit page rules.

The website's ingestion parser is the final authority and fails loudly on push.
