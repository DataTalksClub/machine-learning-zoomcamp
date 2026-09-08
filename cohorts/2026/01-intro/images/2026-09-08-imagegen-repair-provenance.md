# Imagegen repair provenance: 2026-09-08

This ledger records the focused repair of four published illustrations in the
2026 intro cohort. Each replacement was generated with the built-in imagegen
tool using both the original non-crisp video-frame source and a bounded crop or
bounded reference. No target was produced by resizing, sharpening, or enlarging
the previous target.

The generated outputs were inspected at native resolution and at a simulated
608px-wide lesson display before publication. The final PNGs retain the
imagegen C2PA/OpenAI Media Service markers.

## Source and output ledger

| Published target | Original non-crisp source | Bounded crop/reference | Imagegen output | Source SHA-256 | Crop/reference SHA-256 | Published output SHA-256 | Validation |
|---|---|---|---|---|---|---|---|
| `03-supervised-ml-05-multiclass-imagegen-pilot.png` | `03-supervised-ml-05-multiclass.jpg` (598x360) | `03-supervised-ml-05-multiclass-cropped.png` (496x320) | `exec-3aa0a953-cf82-4ff2-bd68-1e793e9a8b5f.png` in `/home/alexey/.codex/generated_images/01a08247-f6a0-7a40-bd69-f1b9009315bf/` | `25ee2097005d68b87af4f806e1bd4d98880d78ba6e1d9c0907b8021309e0b0b6` | `6d4710f3a41d8c684d0345890ba879afd56bebfa101c001d9966cef4d9b244b9` | `33f8bb5966dd28991185081a79c6fc36dd098af460a1f57a055497eb442ee53b` | Native and 608px render checked; exact `Classification`, `Multiclass:`, `cat`, `dog`, `car` content; no webcam/UI/cursor. |
| `05-model-selection-02-multiple-comparisons-imagegen-pilot.png` | `05-model-selection-02-multiple-comparisons.jpg` (598x360) | `05-model-selection-02-multiple-comparisons-cropped.png` (496x320) | `exec-bfd75f36-1963-4e71-b3d2-98f4a1b8e77e.png` in `/home/alexey/.codex/generated_images/01a08255-b52b-7241-9d97-ad6a224c8c5d/` | `b20680138792ec0c925546d058fc95d22c6831f18b57660859a92dc8a53c90b2` | `18553ed081996a13aae5a66b00ca8b6dbb0bd2836ec65f40071d913496c587e0` | `790e0dfe8d99c5cef6ac412a3c806477e1bd2e673d2ea3a6a2fdfcb55e35668c` | Replaced after review found currency drift in the prior redraw. Native and 608px render checked; exact title, `20%` callout, five email examples, five coin examples, and labels `EURO`, `US DOLLAR`, `ZLOTY`, `RUBLE`, `HRYVNIA`; no webcam/UI/cursor/scribbles. |
| `08-linear-algebra-02-dot-product-crisp.png` | `08-linear-algebra-02-dot-product.jpg` (598x360) | `08-linear-algebra-02-dot-product-cropped.png` (940x534), pre-existing bounded reference | `exec-49a5cc06-573a-463a-8a82-c47bc654669f.png` in `/home/alexey/.codex/generated_images/01a08247-f6a0-7a40-bd69-f1b9009315bf/` | `43bf40189d9d69403bf402d7c26272be8e2bd2a642b32c1b4e7835a8430e74d8` | `d5e27c676eaacb38b821e2f2e242497e1358ee1c2f1ec0b8c2ee68e9f3c2fb52` | `930c042f75b5560fd32be14aa7d9d4d4c12bf386602a909bee67fd7717904329` | Native and 608px render checked; exact vectors `[2,4,5,6]`, `[1,0,0,2]`, and terms `2 · 1`, `4 · 0`, `5 · 0`, `6 · 2`; no capture artifacts. |
| `08-linear-algebra-04-matrix-vector-idea-crisp.png` | `08-linear-algebra-04-matrix-vector-idea.jpg` (598x360) | `08-linear-algebra-04-matrix-vector-idea-cropped.png` (980x570), pre-existing bounded reference | `exec-3c4c1e60-faee-4cfc-a111-924eaec3e5ac.png` in `/home/alexey/.codex/generated_images/01a08247-f6a0-7a40-bd69-f1b9009315bf/` | `8fa1d14031e1000ade2a1423fbe155d6ac603607d3fecffd36d9b632bbd22f76` | `b69786383503c0e50bace7e53fadf8ca409d6fa5570c2357a831102b76c58966` | `5570e1b536783c40113fb3cb65d01ae5a6a1d1e1a67ed192c3b879579d9b8aa5` | Native and 608px render checked; exact matrix rows, highlighted first row, vector `[1,0.5,2,1]`, `u`, `v`, and `Uv`; no capture artifacts. |

## Crop construction

The two new bounded references were cut directly from their original JPEG
video frames before imagegen was called:

```bash
convert 03-supervised-ml-05-multiclass.jpg \
  -crop 496x320+8+8 +repage -strip \
  03-supervised-ml-05-multiclass-cropped.png

convert 05-model-selection-02-multiple-comparisons.jpg \
  -crop 496x320+8+8 +repage -strip \
  05-model-selection-02-multiple-comparisons-cropped.png
```

The crop excludes the webcam/UI strip and bottom capture bar while retaining
the lesson content. The two linear-algebra bounded references were already
present in the repository and were supplied unchanged alongside their original
JPEG sources.

## Imagegen invariants

- Preserve the exact lesson relationship, labels, numbers, and arrow direction.
- Remove webcam, browser/UI chrome, cursors, capture controls, and accidental
  source scribbles or overlays.
- Redraw text and mathematical notation sharply; do not use the prior enlarged
  target as an input.
- Check both the full native output and the 608px lesson-size render.
- Keep the original JPEG and bounded reference available for auditability.

The two environment images containing personal faces were intentionally outside
this batch and were not modified.

## Follow-up replacement

The multiple-comparisons asset was regenerated on 2026-09-08 from the original
non-crisp JPEG and the bounded crop above. The previous output was not reused as
an imagegen input and was superseded because it rendered `EURO CENT`, `RIAL`, and
`РУБЛЬ`-style coin content instead of the lesson's required euro, American dollar,
Polish zloty, Russian ruble, and Ukrainian hryvnia examples. The replacement was
copied byte-for-byte from the generated output into the published target. The
five exact visible labels were checked at native resolution and in the 608px
lesson-size render.
