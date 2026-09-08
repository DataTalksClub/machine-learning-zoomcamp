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
