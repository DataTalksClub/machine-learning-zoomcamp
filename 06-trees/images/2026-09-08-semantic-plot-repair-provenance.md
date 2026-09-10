# Semantic and plot repair provenance — 2026-09-08

This ledger records the focused repair of exactly the 13 published image
references identified as `NEEDS-CORRECTION` in Bacon's independent audit of
`05-deployment` and `06-trees`.

The ten native-content removals and ten provenance-unresolved queues were not
touched. The unrelated dirty files in `03-classification` were also left
untouched.

## Method

Three semantic diagrams were regenerated with the built-in imagegen tool. Each
generation used the unchanged original non-crisp JPG and a bounded crop cut
directly from that JPG. The previous published PNG was never used as an input.
The final PNGs were copied byte-for-byte from the selected imagegen outputs.

Ten exact charts were rendered natively by
`2026-09-08-semantic-plot-repair.py`. The script uses the lesson's printed
values for both heatmaps, the wider-search values transcribed from the original
workshop output frame, the notebook's RandomForest/XGBoost source algorithms
and dataset, and the notebook's exact unrestricted-tree AUC values. No chart
was enlarged, sharpened, or generated from a screenshot.

Every final PNG was checked at native resolution and after a 608px-wide lesson
display render. Original JPG sources and the three bounded crops remain in this
directory for auditability.

## Imagegen redraws

| Published target | Original source | Crop `(x, y, width, height)` | Imagegen output ID | Source SHA-256 | Crop SHA-256 | Final SHA-256 |
|---|---|---:|---|---|---|---|
| `01-credit-risk-01-loan-application-imagegen.jpg` | `01-credit-risk-01-loan-application.jpg` | `(20, 0, 450, 330)` | `exec-112ce2a6-f0d0-4e5c-bd68-ec5cca438c72` | `49a3473b88e1adbb6aa00050a07553b6d15f5cb41c6a3343e8eef17d20925bd5` | `f9d44d3f6fa9b5ca40c32cf5f90e21a6c9722ab974da493156dfa12ae69dd9bf` | `a52c7775d2210ee941244b4d06ae5f0c6372261bbf310e0d8f9b1f48ccd75858` |
| `03-decision-trees-06-learned-rules-imagegen.jpg` | `03-decision-trees-06-learned-rules.jpg` | `(90, 0, 410, 250)` | `exec-5b5656e1-89aa-4d84-8dd0-a370f726423b` | `e9317ab139386d90e8c85ce0c33279cb2aa35be7f827a8daa0826a77c8b14d1c` | `235c424f6df6bc486ad4cfe2c49c93a9b7161bab3650f9752c327ab987354449` | `202c1f75deebda1c7a6ce2254978cf33730de85959877954165742ad86bca3ee` |
| `10-summary-02-decision-tree-imagegen.jpg` | `10-summary-02-decision-tree.jpg` | `(10, 0, 500, 240)` | `exec-ee7fcc30-5c7f-484b-abb5-f87d4173923e` | `8882074ceff13ffaaa8751350d298d00ce9f9a5a461b5b666dc152913ba1bd14` | `935d07b9388ab6b33b2dd6e19851b540a1207365b4efa011b594dbd879659539` | `59b8a1493da0c47d95d57f542fd14c9e22dd0460cd854852e7eca4ac5ece39be` |

The loan diagram was regenerated once after an intermediate candidate added an
unwanted `MORE` label (`exec-b790533a-1286-43be-85ff-a209d02f3ea4`). The final
run used the clean crop above and has only the required labels. The final
arrows are explicit: loan application left-to-right, `YES / NO` right-to-left.

The learned-rules target was regenerated after an independent review found that
the root branches were reversed. The new diagram uses the original JPG and its
bounded crop as the only inputs and preserves the corrected lesson semantics:
`records = no?` → `Yes` → `job in [yes]`, and `No` → `seniority < 5`. It contains
only those two child tests, with no invented leaves or extra labels. The other
two generated PNGs preserve the class mapping and summary-tree semantics
described above. All three generated PNGs carry C2PA metadata from the built-in
imagegen tool.

## Deterministic native chart renders

| Published target | Source of truth | Render result SHA-256 |
|---|---|---|
| `05-decision-tree-tuning-05-heatmap-imagegen.png` | `05-decision-tree-tuning.md` printed 8×3 AUC table; columns `4, 5, 6` | `4c1a5932a29254150714ea1bed8b70014b137ae52fb2a22b102689fc598c1927` |
| `05-decision-tree-tuning-07-wider-search-imagegen.png` | Original `05-decision-tree-tuning-07-wider-search.jpg` output table; columns `None, 4, 5, 6, 7, 10, 15, 20` | `84548dcabdae52a4a1197c3ddd428b98da4fa924b2f1e8ee75ddee9df7de2ac5` |
| `06-random-forest-03-auc-vs-trees-imagegen.png` | `06-random-forest.md` `RandomForestClassifier(n_estimators=n, random_state=1)` loop | `bbb1f1ae91cea91a230e819554789e70e72385038356559554c6dc8342084775` |
| `06-random-forest-04-tuning-max-depth-imagegen.jpg` | `06-random-forest.md` depths `5, 10, 15` loop | `732bdc6d1bd4bd488893b53df58b40084a81f2ce7009f883b4a2435380f33c8a` |
| `06-random-forest-05-tuning-min-samples-leaf-imagegen.jpg` | `06-random-forest.md` leaf sizes `1, 3, 5, 10, 50` loop | `00cf98cbe36d066bec564713f656b6eabdecd15a4037823708426951cb5d14ca` |
| `07-boosting-03-train-val-auc-imagegen.png` | `07-boosting.md` XGBoost monitoring plot, `eta=0.3`, `max_depth=6`, `min_child_weight=1` | `430ea8c3b0753c995daf5c93aaa86efff9feddd30e3e96bc69b7bc7bcc596dd6` |
| `08-xgb-tuning-02-tuning-eta-imagegen.jpg` | `08-xgb-tuning.md` eta values `0.3, 1.0, 0.1, 0.05, 0.01` | `76d5073a442e076832bf59352991639b24bd3ac167b86d75a8454ea41d7de702` |
| `08-xgb-tuning-03-max-depth-curves-imagegen.jpg` | `08-xgb-tuning.md` max depths `6, 3, 4` after removing `10` | `0b0831412394b16c2ed94903551c2b90a00ad80e0e4da4554f3936550b87cc30` |
| `08-xgb-tuning-04-min-child-weight-curves-imagegen.jpg` | `08-xgb-tuning.md` child weights `1, 10, 30` | `6bbc5b0260f6c26a306e1bca6002094382c132a653a7f4f766d96303b5ec8ae3` |
| `10-summary-03-overfitting-auc-imagegen.png` | `03-decision-trees.md` notebook output: train `1.0`, validation `0.6548400377860302` | `e1e7d3589c4423452ae8409b2878aa85e2942398e476485337b5bea31acd015c` |

All native charts now have explicit teaching axes. Heatmaps use
`max_depth` and `min_samples_leaf`, and the wider search labels the actual
unlimited-depth value as `None` rather than the malformed `auc-*` or
`None-max_depth` labels from the source capture.

## Reproduction record

Renderer: `2026-09-08-semantic-plot-repair.py`

Renderer SHA-256: `744f29db138d34f1129a44228ee782cad794c8a98f8aadbd0297810ba0911e06`

Dataset URL: `https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-06-trees/CreditScoring.csv`

Dataset SHA-256 at render time: `b42d4fb62b3c1e3428b295d1f152e71ec79e003f86cfa23d7ddb1fc7ea1f624f`

Render command:

```bash
uv run --python 3.11 --with numpy --with pandas --with scikit-learn \
  --with matplotlib --with seaborn --with xgboost \
  python 2026-09-08-semantic-plot-repair.py
```

The final native render used NumPy `2.4.6`, pandas `3.0.5`, scikit-learn
`1.9.0`, matplotlib `3.11.1`, seaborn `0.13.2`, and XGBoost `3.2.0`, with
XGBoost `nthread=1` for reproducible local rendering. The exact literal
heatmap values, chart labels, model parameters, and source URL are retained in
the renderer.
