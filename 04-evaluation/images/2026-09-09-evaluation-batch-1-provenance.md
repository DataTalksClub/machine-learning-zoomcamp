# Evaluation illustration redraw batch 1 — 2026-09-09

This ledger covers only these three active references:

- `01-overview-02-churn-scenario-crisp.jpg`
- `02-accuracy-08-class-imbalance-crisp.jpg`
- `03-confusion-table-01-four-outcomes-crisp.jpg`

The original non-crisp JPGs remain unchanged. Each output was generated with
imagegen using the original JPG and the tracked bounded crop as references. The
crop removes the recording border and webcam area; the generation prompt also
required removal of any cursor, color-wheel control, handwriting, and other
capture artifacts. No enlargement, sharpening, or screenshot tracing was used.

## Reproducible crops

Run `2026-09-09-evaluation-batch-1-crops.sh` from this directory. The script
uses ImageMagick `convert`, JPEG quality 92, and `2x2,1x1,1x1` sampling.

| Source JPG | Crop coordinates `(x,y,w,h)` | Tracked crop |
|---|---:|---|
| `01-overview-02-churn-scenario.jpg` | `(27,0,478,360)` | `01-overview-02-churn-scenario-imagegen-crop.jpg` |
| `02-accuracy-08-class-imbalance.jpg` | `(27,0,478,360)` | `02-accuracy-08-class-imbalance-imagegen-crop.jpg` |
| `03-confusion-table-01-four-outcomes.jpg` | `(27,80,523,280)` | `03-confusion-table-01-four-outcomes-imagegen-crop.jpg` |

## Hashes and validation

| Asset | Original JPG SHA-256 | Crop SHA-256 | Output PNG SHA-256 | Native / 608px render |
|---|---|---|---|---|
| `01-overview-02-churn-scenario` | `cc9e70c271e6dc28e0e6b0bf55992f946727acce02bbec601a9c1a4c53b3115f` | `c3724955eda0c1dd77f9cf5111d2fab44ca6ada0b080703703064c94a37d5826` | `da77d026e613c154132b73765ebefe7b795f530e9dba62fc36e26f26eef238cb` | `1445x1088` / `608x458` |
| `02-accuracy-08-class-imbalance` | `1eb6b87db34c62028e305109c6a81a2a1e671363b329821dfc91b7d2fd08a6d7` | `db2768d71d2beb0e40d071cba0fdd6e9ea073c3187719996f4db43dfc8487fc6` | `8da7aea9a519cfca6fd588aac7cf501b36e88658d106c8fd74c13b0bb920ae95` | `1619x971` / `608x365` |
| `03-confusion-table-01-four-outcomes` | `b1930d3330a469f90615eddba7be04b55e33439661fe7e7474885c06c21deec3` | `7b52ab5b34b1343e52b923e99662841571f613ab3e2e9549df953a58b7816ec7` | `0652471c81e5bb978515c0553800c119ba0e3df0a904c29294c5db1fee394921` | `1774x887` / `608x304` |

All three PNGs contain C2PA metadata with `gpt-image` and `OpenAI Media
Service` markers. Native and simulated 608px inspections confirmed readable
labels, complete compositions, exact percentages/scores, and no webcam,
browser, cursor, overlay, or simple-upscale artifacts.

The three outputs are a completed focused batch, not a repository-wide
crispness approval. The two remaining strict-audit references are now
documented in
[`2026-09-09-remaining-provenance.md`](2026-09-09-remaining-provenance.md),
which records their source/crop/output chain or direct-imagegen retention
decision.
