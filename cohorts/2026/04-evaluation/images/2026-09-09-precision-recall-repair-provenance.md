# Precision and recall illustration repair evidence

Date: 2026-09-09

This record covers only the two repaired illustrations in `04-precision-recall.md`.
The source JPGs remain unchanged. Each output was generated from the original JPG
and a bounded crop that excluded the camera inset, screen borders, and recording
controls. The final PNGs were inspected at native resolution and in simulated
608px-wide renders.

## Precision definition

Target: `04-precision-recall-01-precision-definition-crisp.png`

The previous redraw had the defective wording “HOW MANY FRACTION OF ... THAT ARE
CORRECT”. The repaired redraw uses the exact sentence “WHAT FRACTION OF POSITIVE
PREDICTIONS ARE CORRECT”, while preserving the source's precision oval and
predicted-positive partition.

| Artifact | SHA-256 |
|---|---|
| Original JPG `04-precision-recall-01-precision-definition.jpg` | `011540d437f3dab2bd0133c345428cbf5cb823deebd76a46c2f868d2bac10df1` |
| Bounded crop (temporary) | `90f2da1f7d41c2adda5c8fe8a25d6e32aea52c3b15c78964466b9e03ac516847` |
| Final PNG `04-precision-recall-01-precision-definition-crisp.png` | `a9c1c17c3f1b665355f89701d0f3d05385c1a8e2c9681f944714e79c1a14ad4b` |

Validation:

- Final dimensions: `1619×972`; simulated 608px render: `608×365`.
- The final PNG carries C2PA metadata identifying `gpt-image`.
- No camera, cursor, playback controls, borders, watermark, or extra text remain.
- The generated text was checked visually against the required wording.

## Precision/recall table

Target: `04-precision-recall-06-precision-recall-table-crisp.png`

The previous redraw retained an overwritten/crossed-out `PRECISION` label. The
repaired redraw cleanly labels the predicted-positive column `PRECISION` and the
actual-positive row `RECALL`, with the original `TN`, `FP`, `FN`, and `TP` cells.

| Artifact | SHA-256 |
|---|---|
| Original JPG `04-precision-recall-06-precision-recall-table.jpg` | `6a6671d0d41b134fefc7ba035f60da38244437002c9ff764f9b272230894a3a7` |
| Bounded crop (temporary) | `c671c9595b5c18a7cde8fbffd82d5814bdc89e9d615a9e929ec81c159e7b4e79` |
| Final PNG `04-precision-recall-06-precision-recall-table-crisp.png` | `795de7c988e33653ef9c1b73dde4dfb261af726e1927097279b8cf336b8b0267` |

Validation:

- Final dimensions: `1536×1024`; simulated 608px render: `608×405`.
- The final PNG carries C2PA metadata identifying `gpt-image`.
- The green bottom row and right column correspond to recall and precision,
  respectively; all four confusion-table labels are visible at 608px.
- No camera, cursor, playback controls, borders, watermark, or overwritten label
  remain.

## Removed low-value recall-definition embed

The Markdown embed for `04-precision-recall-04-recall-definition-crisp.png` was
removed from `04-precision-recall.md`. The surrounding prose and exact recall
formula remain in the lesson, so this generic oval-and-label screenshot added no
instructional information beyond the text. The source JPG and generated PNG are
preserved in the repository for auditability and possible future reuse.

| Preserved artifact | SHA-256 |
|---|---|
| Source JPG `04-precision-recall-04-recall-definition.jpg` | `2b20b09e0efc03d9010b590c126bc4c04c3bd4ea6d89e590765ea56402cb3755` |
| Removed embed PNG `04-precision-recall-04-recall-definition-crisp.png` | `f855ccc29c0cb6d4741a4ce50b30872028321e744b68846ad5467ab06d11b37d` |
