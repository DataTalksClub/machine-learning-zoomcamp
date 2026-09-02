# Cohorts

Each `cohorts/<year>/` directory is one delivery of the course. The directory
name is the cohort identifier the course platform publishes.

**2026 is the current cohort. Edit there.**

## Layout

```
cohorts/
├── 2026/                     # the directory name IS the cohort identifier
│   ├── cohort.yaml           # cohort identity, dates, module flow
│   ├── README.md             # the human-readable schedule
│   ├── 01-intro/             # the directory name IS the module slug
│   │   ├── module.yaml       # module identity and unit list
│   │   ├── README.md         # GitHub-facing module index, not published
│   │   ├── 01-what-is-ml.md  # units: NN-kebab.md, the stem IS the unit slug
│   │   ├── 02-ml-vs-rules.md
│   │   ├── homework.md       # homework instructions, fixed name
│   │   ├── homework.yaml     # homework identity, due date, form, questions
│   │   ├── images/           # every image the module's units reference
│   │   └── notebooks/        # notebooks and scripts the units link
│   ├── ...
│   ├── article.md            # non-module cohort material is allowed
│   └── projects.md
├── 2025/                     # earlier cohorts: frozen archives
└── 2021 … 2024/
```

Two rules carry most of the weight:

- **Names are identity.** The cohort identifier, the module slug and the unit
  slug are the directory and file names. Nothing in YAML restates them, and
  renaming one moves a published URL.
- **A module directory is self-contained.** Its units, images, notebooks and
  homework live inside it, units are siblings of `module.yaml`, and a relative
  link never climbs past the cohort directory. Anything further away is written
  as an absolute GitHub URL.

The repository root holds the landing page, the course-wide helper documents and
branding images only. No curriculum lives there.

## Editing

- Fix the current cohort. That is where pull requests are accepted.
- Earlier cohorts are frozen archives: the drift is the record of what was
  actually taught. Backport only factual or breaking errors, and do it
  per-cohort explicitly.
- A published slug is frozen. Renaming one is a platform decision, not a
  repository pull request.

## The conventions themselves

This repository does not restate them. `DataTalksClub/zoomcamp-template` is the
authority: `STRUCTURE.md` for the repository layout and the curriculum contract
documented beside it for the YAML schemas and the unit page rules.

The website's ingestion parser is the final authority and fails loudly on push.
