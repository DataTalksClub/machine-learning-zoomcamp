# Imagegen provenance: regression screenshot batch

This batch replaces exactly ten published screenshot-derived assets. Each
redraw was sent to the built-in imagegen tool with the unchanged original JPG
and the explicit bounded `-imagegen-crop.jpg` reference. The crop is a
composition/reference input, not the final asset and not a resize or sharpening
derivative. The original JPGs remain unchanged.

All final PNGs were inspected at native resolution and after resizing to 608px
wide, the lesson display-size check used for this batch. Browser, webcam,
cursor, selection, playback, and handwritten overlays were removed. Code,
labels, values, axes, curves, and diagram relationships were checked against
the source references.

| Target | Original source | Crop coordinates in original (x, y, width, height) | Crop reference | Final imagegen output ID |
|---|---|---:|---|---|
| `01-car-price-intro-01-select-best-price-crisp.jpg` | `01-car-price-intro-01-select-best-price.jpg` | `(90, 70, 450, 240)` | `01-car-price-intro-01-select-best-price-imagegen-crop.jpg` | `exec-03448b54-7beb-45ee-8b27-2f4078ab88e5` |
| `01-car-price-intro-02-kaggle-dataset-crisp.jpg` | `01-car-price-intro-02-kaggle-dataset.jpg` | `(15, 50, 570, 280)` | `01-car-price-intro-02-kaggle-dataset-imagegen-crop.jpg` | `exec-e8d79784-b4b7-4735-88f0-1d414800768b` |
| `01-car-price-intro-03-kaggle-data-explorer-crisp.jpg` | `01-car-price-intro-03-kaggle-data-explorer.jpg` | `(0, 65, 598, 285)` | `01-car-price-intro-03-kaggle-data-explorer-imagegen-crop.jpg` | `exec-2d6a0af7-ba01-42a9-b7a1-87d9071f1a56` |
| `01-car-price-intro-04-msrp-column-crisp.jpg` | `01-car-price-intro-04-msrp-column.jpg` | `(0, 50, 598, 300)` | `01-car-price-intro-04-msrp-column-imagegen-crop.jpg` plus the legacy clarity crop | `exec-f77aeb51-4dbe-4612-b5c0-e980999e927d` |
| `01-car-price-intro-06-github-repo-crisp.jpg` | `01-car-price-intro-06-github-repo.jpg` | `(0, 50, 598, 285)` | `01-car-price-intro-06-github-repo-imagegen-crop.jpg` | `exec-ce9d07be-34ce-439b-8d07-1aff25a68d7e` |
| `01-car-price-intro-07-chapter-files-crisp.jpg` | `01-car-price-intro-07-chapter-files.jpg` | `(0, 175, 598, 95)` | `01-car-price-intro-07-chapter-files-imagegen-crop.jpg` | `exec-cff023f5-31d4-4eae-a892-b2d4d84f5b99` |
| `03-eda-03-long-tail-distribution-crisp.jpg` | `03-eda-03-long-tail-distribution.jpg` | `(0, 90, 598, 270)` | `03-eda-03-long-tail-distribution-imagegen-crop.jpg` | `exec-8d3c75e9-6545-4806-b3b4-81f76c042425` |
| `03-eda-04-zoom-below-100k-crisp.jpg` | `03-eda-04-zoom-below-100k.jpg` | `(0, 150, 598, 210)` | `03-eda-04-zoom-below-100k-imagegen-crop.jpg` | `exec-3902e0e0-f706-461e-9a35-86bba0476ef8` |
| `03-eda-06-log1p-normal-distribution-crisp.jpg` | `03-eda-06-log1p-normal-distribution.jpg` | `(0, 95, 598, 265)` | `03-eda-06-log1p-normal-distribution-imagegen-crop.jpg` | `exec-84d080e6-1f37-497f-96e1-4319c09e5a53` |
| `04-validation-framework-01-train-val-test-split-crisp.jpg` | `04-validation-framework-01-train-val-test-split.jpg` | `(0, 60, 570, 300)` | `04-validation-framework-01-train-val-test-split-imagegen-crop.jpg` | `exec-e2875f78-747b-4437-aa19-5a68c32b082a` |

## Source integrity

The original non-crisp source JPGs were retained byte-for-byte. Their SHA-256
hashes before and after this batch are recorded here:

| Source | SHA-256 |
|---|---|
| `01-car-price-intro-01-select-best-price.jpg` | `ecef46bc06c7c0bf5a74b18f96997fef75649d6bd6ac498e0313dc0b86ce802e` |
| `01-car-price-intro-02-kaggle-dataset.jpg` | `8afdab00cde83da167e7b9a07072d693da3c02f98c62a568204e6a76ed8fc4c2` |
| `01-car-price-intro-03-kaggle-data-explorer.jpg` | `38cfc8b184356e53aac1f8efeda9614cd1cc33bfe4e139e902624f70d97d841b` |
| `01-car-price-intro-04-msrp-column.jpg` | `ad9207ebeb9bb73756d48d30409d2e3ac3141b98f7778b1aa12d6a422acd4c51` |
| `01-car-price-intro-06-github-repo.jpg` | `2ec66758aebaec9ed51e7777e116caf93bdf39402415520d4897d96252f0ab2d` |
| `01-car-price-intro-07-chapter-files.jpg` | `ac98f22d1ced6008328b07c7826e89a5f1d6a30040f4ff3fb5ffa7de8f1409ea` |
| `03-eda-03-long-tail-distribution.jpg` | `2e958c803ca9dbaee1ba93b68c6eefea1f306661ce958aeef8526cbd3b938c0e` |
| `03-eda-04-zoom-below-100k.jpg` | `23d4513b8d37850ae4051abef5958451aed6d22451a3f24382df182a69750874` |
| `03-eda-06-log1p-normal-distribution.jpg` | `3d02d0d251ae1cfb570268559e4a1461cb4263a2f0d58c5b58a34bc8f5437fe5` |
| `04-validation-framework-01-train-val-test-split.jpg` | `41ea5bba9757bbcabfa249a5521ae3756a2e8f04bd5ddfcb034cffe32cc14a45` |

Rejected during visual review: the first validation redraw used subscript-like
labels; an MSRP redraw changed visible table values; and two under-100,000
histogram redraws contained stray punctuation/line artifacts. None of those
outputs is published.

## Focused current-reference audit: 2026-09-09

The current `*imagegen*.png` reference set contains exactly twelve published
targets across modules 02 and 03. This section records the four regression
targets; the eight classification targets are recorded in the corresponding
classification ledger. The three rows marked `REGENERATED` now have durable
target-specific evidence from the unchanged original JPG, a bounded native
crop, and a fresh built-in imagegen output. The previous published PNG was not
used as an imagegen input.

| Published target | Original source | Crop `(x,y,width,height)` | Retained crop | Imagegen output | Source SHA-256 | Crop SHA-256 | Final SHA-256 | Final dimensions | Disposition |
|---|---|---:|---|---|---|---|---|---:|---|
| `05-linear-regression-simple-01-one-car-one-price-imagegen-pilot.jpg` | `05-linear-regression-simple-01-one-car-one-price.jpg` | `(25,0,470,340)` | `05-linear-regression-simple-01-one-car-one-price-imagegen-crop.jpg` | `exec-65bf2408-9fe3-4f95-aaae-1a171db00530` | `194180f3da215af459ed369029319d44d309ebb4559aaac314c6d39510b20d91` | `61a5b901691f74323965cea5284ac9e785c6fcb21bf02d419b1bda9ea3ea7752` | `88953eb79f8c0ca8eb7a35b6f8f0259ef71c716ac36004356cdc74bb13bb7daf` | `1475x1067` | **REGENERATED / ACCEPT** |
| `11-feature-engineering-01-feature-engineering-imagegen.jpg` | `11-feature-engineering-01-year-column.jpg` | `(15,80,480,260)` | `11-feature-engineering-01-feature-engineering-imagegen-crop.jpg` | `exec-30b04bdd-9000-45de-b5c6-b42035e2e835` | `f5df307802221f1da8e1fc9537db31d8e578584cdb6c07b19ee18c75be22d737` | `13dec6cff48bc8c60cee880aa031de9b29a618c94a526c5d7668bbf63445f18d` | `09eb22ad57c57f260cf95296f8d45908ab04cf6e90fe0218acf1688a23e24f98` | `1942x809` | **REGENERATED / ACCEPT** |
| `15-using-model-05-website-request-diagram-imagegen.jpg` | `15-using-model-05-website-request-diagram.jpg` | `(20,5,485,330)` | `15-using-model-05-website-request-diagram-imagegen-crop.jpg` | `exec-a898c763-66c5-4454-bd0c-998124bb9591` | `745465a2ca409edfc6fdaca5602d1a2fe98c8d35f7a9590fec0ec5182ce09c32` | `fdd65bee01a701c29481c290985c1e845c86247dcc6f0271de71dac03352f9ec` | `384bc5828616c1e4814d1a83c31d733f0cd2588e22369991317e4e39bab04fc0` | `1677x938` | **REGENERATED / ACCEPT** |
| `17-explore-more-01-feature-experiments-imagegen.jpg` | `N/A — standalone generated asset; no target-specific source JPG exists` | `N/A` | `N/A — no source crop exists` | `C2PA claim `urn:c2pa:97ea80b6-608a-4041-97f5-334a5122b325`; execution ID not retained | `N/A` | `N/A` | `2a61cbd5a94153f2d5d1a6a7999890eb657e3ec576e1355dbf3b5149998d382e` | `1672x941` | **UNCHANGED / ACCEPT** — existing OpenAI C2PA imagegen output; no prior target was used |

### Inspection and invariants

- The three regenerated outputs were copied byte-for-byte from the built-in
  imagegen results. They were inspected at native size and at simulated 608px
  lesson width: `05` at `608x440`, `11` at `608x253`, and `15` at `608x340`.
- `05` preserves `g(x_i) ≈ y_i`, the `A CAR` and `ITS PRICE` labels, arrows,
  and the visible lower fragment `x_i = (x_i1`. `11` preserves `year` with
  `2008`, `2012`, `2016`, the exact `2017 − year` transformation, `age` with
  `9`, `5`, `1`, and the `Model` / `Input Matrix` endpoint. `15` preserves
  `TOYOTA`, `SIENNA`, the empty form fields, arrow, braces, and ellipsis.
- Face, camera, browser/editor chrome, cursor, playback, selection, black
  border, and watermark overlays were removed. No upscale, Lanczos resize, or
  sharpening was used to create a published target.
- `17` was already a valid standalone built-in imagegen output with OpenAI
  C2PA metadata, so it was left byte-identical. Its existing native and 608px
  inspections passed; no original JPG or bounded crop is available for this
  standalone illustration by design.
- The three original JPGs and three bounded native crops remain in this
  directory. Their source and crop hashes above provide the reproducible
  input chain for the regenerated targets.
