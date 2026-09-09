# ROC 01/02/03 deterministic repair provenance — 2026-09-09

This ledger covers only the three active references below. ROC 04/05/06 are
outside this repair and were not modified.

- `05-roc-01-tpr-fpr-vs-threshold-crisp.png`
- `05-roc-02-random-model-tpr-fpr-crisp.png`
- `05-roc-03-ideal-model-tpr-fpr-crisp.png`

## Source of truth

The renderer is `2026-09-09-roc-01-03-render.py`. It follows the data
preparation, split, logistic-regression model, 101-threshold loop, random
model, and ideal-model construction in `../05-roc.md` and
`../notebook.ipynb`. These are deterministic native rasterizations; they are
not enlarged, sharpened, imagegen-produced, or traced from the old screenshots.

The source CSV is the file used by the lesson notebook:

```text
https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

Source CSV SHA-256:

```text
88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a
```

The pinned reproduction runtime is:

```text
Python 3.8
numpy 1.18.5
pandas 1.0.5
scikit-learn 0.22.2.post1
matplotlib
```

The validation set has exactly 1,409 rows: 1,023 negatives and 386
positives. The lesson facts asserted by the renderer are:

```text
thresholds = np.linspace(0, 1, 101)
threshold 0.5: TN=922, FP=101, FN=176, TP=210
threshold 0.5: TPR=210/386=0.5440414507772021
threshold 0.5: FPR=101/1023=0.09872922776148582
random model: np.random.seed(1)
random model accuracy at threshold 0.5 = 0.5017743080198722
ideal model: y_ideal = np.repeat([0, 1], [1023, 386])
ideal scores: y_ideal_pred = np.linspace(0, 1, 1409)
ideal separation threshold = 0.726; accuracy = 1.0
```

The output plots use the exact TPR/FPR values computed by that procedure. To
make the charts self-identifying at lesson size, the deterministic renderer
adds the axis labels `Threshold` and `Rate`; the plotted series remain exactly
`TPR` and `FPR` from the lesson.

## Reproduction

From the repository root, after downloading the verified CSV to
`/tmp/data-week-3.csv`:

```bash
uv run --python 3.8 \
  --with numpy==1.18.5 \
  --with pandas==1.0.5 \
  --with scikit-learn==0.22.2.post1 \
  --with matplotlib \
  python cohorts/2026/04-evaluation/images/2026-09-09-roc-01-03-render.py \
  --data-path /tmp/data-week-3.csv \
  --output-dir cohorts/2026/04-evaluation/images
```

The renderer asserts the validation size, class counts, and threshold-0.5
confusion counts before writing any PNG. A clean reproduction produced byte-
identical outputs for all three targets.

## Native and 608px verification

Each native PNG was inspected at full resolution. A proportional ImageMagick
render to 608px width was then inspected separately. All six views showed
complete curves, readable `TPR`/`FPR` legends, readable `Threshold`/`Rate`
axes, and no camera, browser, cursor, overlay, or screenshot artifacts.

| Target | Native dimensions | 608px dimensions | Source JPG SHA-256 | Output PNG SHA-256 |
|---|---:|---:|---|---|
| `05-roc-01-tpr-fpr-vs-threshold-crisp.png` | `1510x1030` | `608x415` | `39ffa6dbe8f4d84a34230c295e9015e8536b3270f0f697712d0837b2cefe4d06` | `e5fad46bc39a4edeec0845ca45fba18b057f2ccbe255e3e6d33eb8386c51301b` |
| `05-roc-02-random-model-tpr-fpr-crisp.png` | `1510x1030` | `608x415` | `a7f2c2cf457dacbfaee988596642fc0fb103619ee3b14bcaf9d6346dbb3e29bc` | `19289e22be543f645664469aa129797cb58c33edcf807ffa6d04073f69288007` |
| `05-roc-03-ideal-model-tpr-fpr-crisp.png` | `1510x1030` | `608x415` | `abffffe11b9cfc7f7e6c554933c99ac1da6458db263f7fc4cffffd3204535933` | `75d75f60a2395c63639636bc932849fdf44da804fcdc689bedf42f9155bbe127` |

The ROC source JPGs remain preserved for historical comparison. The output
PNGs are deterministic code renders, so C2PA/imagegen metadata is not
expected or required for this batch.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| `2026-09-09-roc-01-03-render.py` | `a50804a58047aa9829a16810ac973e53fe5096a15f00164a48ea9eef0ff0c933` |
| Source CSV | `88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a` |
