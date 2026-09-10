# ROC plot repair provenance — 2026-09-09

This record covers only the three active ROC references in `05-roc.md`:

- `05-roc-04-model-vs-ideal-tpr-fpr-crisp.jpg`
- `05-roc-05-roc-curve-manual-crisp.jpg`
- `05-roc-06-roc-curve-sklearn-crisp.jpg`

The original JPGs were inspected for content and retained unchanged. No crop
was used for this batch: these are deterministic native plots, not imagegen
redraws. The previous PNGs were enlarged screenshot-derived plots; they were
replaced with fresh rasterizations of the lesson's plotting code.

## Source of truth

The renderer is `2026-09-09-roc-plot-render.py`. It follows the exact data
preparation, split, model, threshold loop, ideal-model construction, and
`roc_curve` calls in `../05-roc.md` and `../notebook.ipynb`.

The source CSV is the file downloaded by the original lesson notebook:

```text
https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

Source CSV SHA-256:

```text
88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a
```

The historical runtime is pinned because newer scikit-learn solvers can shift
the validation probabilities even with the same CSV:

```text
Python 3.8
numpy 1.18.5
pandas 1.0.5
scikit-learn 0.22.2.post1
matplotlib (renderer only)
```

The notebook's validation set has 1,409 rows: 1,023 negatives and 386
positives. At threshold `0.5`, the lesson confusion matrix is:

```text
[[922, 101],
 [176, 210]]
```

The notebook records ROC AUC `0.843850505725819`; the renderer uses the
lesson's plotted `df_scores` and `roc_curve` values rather than a hand-drawn
approximation or a screenshot trace.

## Reproduction

From this directory, after downloading the CSV to `/tmp/data-week-3.csv`:

```bash
uv run --python 3.8 \
  --with numpy==1.18.5 \
  --with pandas==1.0.5 \
  --with scikit-learn==0.22.2.post1 \
  --with matplotlib \
  python 2026-09-09-roc-plot-render.py \
  --data-path /tmp/data-week-3.csv \
  --output-dir .
```

No enlargement, sharpening, imagegen, camera, browser chrome, cursor, or
overlay is involved. The outputs are rendered at native high resolution and
remain readable in a 608px-wide lesson render.

## Hashes

| Artifact | SHA-256 |
|---|---|
| Source `05-roc-04-model-vs-ideal-tpr-fpr.jpg` | `0533987b275ec0b1118887441d0af3482eeebe5ade41bb272a66f07820696cc4` |
| Source `05-roc-05-roc-curve-manual.jpg` | `1addce45368858d5a96dafa1e07d7dcd659e8eeca29bf4bc109695704b1f5c84` |
| Source `05-roc-06-roc-curve-sklearn.jpg` | `2d2e3c6325a5c28828a4df66db56243ce62015060679f038b1c484a27c8e7c36` |
| Renderer script | `346317be698a044f8852a4c4cfb62b612b855d9dcade14383de66b816586d112` |
| Repaired `05-roc-04` PNG | `242f7c73b08929bf994bf7281e15f6f9e9f041de1f798f2b3642e355487cf9c5` |
| Repaired `05-roc-05` PNG | `342e9d6ac416665fcc36c4def75db3c4d420716c86acdda1245b23ad77699a79` |
| Repaired `05-roc-06` PNG | `a69ed6accaef6054934b7f8439ee3931e9f9ccce0775a8ad0583a05f3936ef3c` |

The three deterministic PNGs do not carry C2PA metadata because they were
rendered from code; C2PA is required only for imagegen-produced assets.
