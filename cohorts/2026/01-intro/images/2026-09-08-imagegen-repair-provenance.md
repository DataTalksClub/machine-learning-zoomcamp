# Imagegen repair provenance: 2026-09-08 through 2026-09-09

This ledger records the focused repair of nine published illustrations in the
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
| `06-environment-01-create-repo-crisp.png` | `06-environment-01-create-repo.jpg` (640x360) | `06-environment-01-create-repo-cropped.png` (500x314), pre-existing deterministic bounded crop | `exec-1bbc325a-b889-472f-a9b7-17aba853ce14.png` in `/home/alexey/.codex/generated_images/01a083d2-dd13-7f33-92ba-1b1bc186329d/` | `d21484268e3fb954f86f06fd958918dc63b551ae489eb2220e721213183c9152` | `cf9e1cbf44ae8c0f7d1d9b845c19e7fe0dd650e5aa20195cef7e39e5944c4bf9` | `cb4148800e0a8815dc43ee7fb4e43298a5b51c4b71f9c25909f6bbd316409614` | Native and 608px render checked; exact repository-creation UI retained; owner avatar replaced with a face-free geometric mark; webcam excluded; C2PA/OpenAI Media Service markers present. |
| `06-environment-02-create-codespace-crisp.png` | `06-environment-02-create-codespace.jpg` (640x360) | `06-environment-02-create-codespace-cropped.png` (520x322), pre-existing deterministic bounded crop | `exec-56a8a278-fe7f-4724-b6a1-73a0f99275f6.png` in `/home/alexey/.codex/generated_images/01a083d2-dd13-7f33-92ba-1b1bc186329d/` | `14a2a7c7b5b49363cfdb903e872f26da2f3efae31cbbc510ad20d39343f828dd` | `b7a82980daae121aac838047ea2bdf4b3e5e12746b443b4c0c8d73b15c710fea` | `b78771cb3c87c881f81d090f780fa0e4d8a86f67386ab069b47b6abd1e56373c` | Native and 608px render checked; exact repository/Codespaces UI retained; both visible profile avatars replaced with face-free geometric marks; webcam excluded; C2PA/OpenAI Media Service markers present. |
| `01-what-is-ml-05-model-training-imagegen-pilot.png` | `01-what-is-ml-05-model-training.jpg` (598x360) | `01-what-is-ml-05-model-training-cropped.png` (500x255), deterministic crop `500x255+25+82` | `exec-2f0b83c1-9943-4ea1-aa12-473458679955.png` in `/home/alexey/.codex/generated_images/01a083f4-cb0e-72a0-a1d8-256ed3954c4b/` | `8db777ea0c89cadaee8af964501f938680e074ecf23d8c8d8b75cc878ff2e04f22` | `8fbb30c261c3c30b5c78e3da57f76d6e383c58a75c590e961be7f02c46c200c5` | `b6b8f49a79153316a8cf4a1c8e6e734cf0186a36158689472b036321d51015ff` | Native and 608px render checked; source `BWM` corrected to lesson-required `BMW`; exact feature/price values and arrows retained; no capture artifacts; C2PA `urn:c2pa:48bc46c0-b605-4903-a4e8-d87716edbb20`. |
| `01-what-is-ml-06-using-model-imagegen-pilot.png` | `01-what-is-ml-06-using-model.jpg` (598x360) | `01-what-is-ml-06-using-model-cropped.png` (500x255), deterministic crop `500x255+25+82` | `exec-0551654c-5b5e-4e77-85f7-1294c4a7d07d.png` in `/home/alexey/.codex/generated_images/01a083f4-cb0e-72a0-a1d8-256ed3954c4b/` | `27a42ad4d58cbb7b7e7bf4e1f90939f453eff810e7a7a25e6f9adcf217ebe8cd` | `4ad140e7440f5e2d14b44b6fc55bbe4f5281966ce4ee6fdb104826e96382a049` | `2a74d914173946dec82eae82c28aed0f2f1e023323f08d6e1e2e1e2b2d56b694` | Native and 608px render checked; source `BWM` corrected to lesson-required `BMW`; exact faded targets, predictions, model flow, and labels retained; no capture artifacts; C2PA `urn:c2pa:e0d9d1c7-73d5-488d-a5fb-9fb4eb75923a`. |
| `01-what-is-ml-07-suggest-price-imagegen-pilot.png` | `01-what-is-ml-07-suggest-price.jpg` (598x360) | `01-what-is-ml-07-suggest-price-cropped.png` (220x285), deterministic crop `220x285+15+30` | `exec-5cd28d37-3c25-40bd-9ba3-0a20cc0fcc53.png` in `/home/alexey/.codex/generated_images/01a0840b-9dd1-7c82-af53-1e3ccb13cbd9/` | `92482d032c3186a8612033b1581064c72cbd02508625aeada49e6e0bd91f8428` | `649685ac224caf351e30339035f58c8fa78cf0b92e00cdd6dea94f5f5ef7fd9d` | `412af79981e170aa6d3e9a5d7e856a8120e7c529b4c26b39daabaeb6298d2723` | Regenerated from the original JPG and bounded crop; native and 608px renders checked; exact `Toyota Hilux, almost new` form retained; price input is blank with `UAH` and `Required field`; no numeric amount or `Suggested by model`; no capture artifacts; C2PA `urn:c2pa:53032dbb-8e1c-4ff1-9a1f-18d50313cbd9`. |

## Crop construction

The first two bounded references were cut directly from their original JPEG
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
JPEG sources. The two environment bounded crops were also pre-existing
deterministic references and were supplied unchanged alongside their original
JPEG sources; they remove the webcam area while retaining the UI used by the
lesson.

## Imagegen invariants

- Preserve the exact lesson relationship, labels, numbers, and arrow direction.
- Remove webcam, browser/UI chrome, cursors, capture controls, and accidental
  source scribbles or overlays.
- Remove human faces from incidental profile/avatar images by replacing them
  with neutral geometric marks; preserve the avatar circle and its UI position.
- Redraw text and mathematical notation sharply; do not use the prior enlarged
  target as an input.
- Check both the full native output and the 608px lesson-size render.
- Keep the original JPEG and bounded reference available for auditability.

## Follow-up replacement

The multiple-comparisons asset was regenerated on 2026-09-08 from the original
non-crisp JPEG and the bounded crop above. The previous output was not reused as
an imagegen input and was superseded because it rendered `EURO CENT`, `RIAL`, and
`РУБЛЬ`-style coin content instead of the lesson's required euro, American dollar,
Polish zloty, Russian ruble, and Ukrainian hryvnia examples. The replacement was
copied byte-for-byte from the generated output into the published target. The
five exact visible labels were checked at native resolution and in the 608px
lesson-size render.

## Environment avatar repair

On 2026-09-09, the two environment illustrations were regenerated from their
original non-crisp JPEGs and the pre-existing deterministic bounded crops. The
previous published PNGs were not supplied to imagegen. Imagegen changed only
the human profile/avatar imagery: each affected circle now contains a simple
geometric mark with no face, eyes, portrait, or human features. The webcam
panels present in the original full frames remain excluded by the bounded crops.
Both outputs were inspected at native resolution and as 608px-wide lesson
renders; neither contains a face or camera panel, and both retain C2PA/OpenAI
Media Service metadata.
