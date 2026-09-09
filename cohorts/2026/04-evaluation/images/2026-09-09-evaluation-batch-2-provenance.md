# Evaluation illustration redraw batch 2 — 2026-09-09

This ledger covers these three active references only:

- `03-confusion-table-04-confusion-counts-crisp.png`
- `04-precision-recall-03-precision-pie-crisp.png`
- `04-precision-recall-05-recall-example-crisp.png`

Each output was generated with imagegen from the unchanged original JPG and
the tracked bounded crop. The prompts required exact lesson values and labels,
clean typeset/vector-like redraws, and removal of the webcam, recording
controls, cursor, color-wheel overlay, handwriting, and other screenshot
artifacts. These are redraws, not enlargements or sharpened screenshots.

## Reproducible crops

Run `2026-09-09-evaluation-batch-2-crops.sh` from this directory. It uses
ImageMagick `convert`, JPEG quality 92, and `2x2,1x1,1x1` sampling.

| Source JPG | Crop coordinates `(x,y,w,h)` | Tracked crop |
|---|---:|---|
| `03-confusion-table-04-confusion-counts.jpg` | `(27,70,523,290)` | `03-confusion-table-04-confusion-counts-imagegen-crop.jpg` |
| `04-precision-recall-03-precision-pie.jpg` | `(27,65,523,295)` | `04-precision-recall-03-precision-pie-imagegen-crop.jpg` |
| `04-precision-recall-05-recall-example.jpg` | `(27,0,478,360)` | `04-precision-recall-05-recall-example-imagegen-crop.jpg` |

## Hashes and validation

| Asset | Original JPG SHA-256 | Crop SHA-256 | Output PNG SHA-256 | Native / 608px render |
|---|---|---|---|---|
| `03-confusion-table-04-confusion-counts` | `5bd9df275d2afed47a8bb5f2612e452bf52e9465b3bd3988396c9540c0f97527` | `b7d0b4d52784ecd3c7cc296b6a4ed507492949a25124bb5712f8793fc413b3f1` | `f9a9bf5fcddaec3dcb68ca361cf0823299f347a939cb762c96cbe263ea8b4924` | `1685x933` / `608x337` |
| `04-precision-recall-03-precision-pie` | `0e7a6085a9be56f30a7b4024ecf1be6ed0dd1e236ad857eb9058f68d49b3700b` | `e1cbbff558795f5984462daaf2ed27e72cea4d7c676a9450ae2228a1cf321892` | `310be9f87edfb7234f5d2d74dd46897b0c54e7cea624a19516d2ca58ece84f77` | `1670x941` / `608x343` |
| `04-precision-recall-05-recall-example` | `7cbd46c699efd4e6ca6f639045e5db312cec9df119720ffd04d6316dc315e960` | `7b2224cd7225ba69fb888352ef62f56674f09875fbd89a9b7ced617714e46fd6` | `90475c45eb8d14bcf905d5d6b1790ac479431062ba411b9b1da61cef655d9a8d` | `1536x1024` / `608x405` |

All three PNGs contain C2PA metadata with `gpt-image` and `OpenAI Media
Service` markers. Native and 608px inspections confirmed:

- `TN=922`, `FP=101`, `FN=176`, and `TP=210` in the confusion-count diagram;
- the precision diagram's green `TP` and red `FP` predicted-positive split;
- exactly three flagged and one missed actual churner, with `R = 3/4 = 75%`.

No webcam, browser, cursor, overlay, or simple-upscale artifacts remain.
