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
| `01-car-price-intro-01-select-best-price-crisp.png` | `01-car-price-intro-01-select-best-price.jpg` | `(90, 70, 450, 240)` | `01-car-price-intro-01-select-best-price-imagegen-crop.jpg` | `exec-03448b54-7beb-45ee-8b27-2f4078ab88e5` |
| `01-car-price-intro-02-kaggle-dataset-crisp.png` | `01-car-price-intro-02-kaggle-dataset.jpg` | `(15, 50, 570, 280)` | `01-car-price-intro-02-kaggle-dataset-imagegen-crop.jpg` | `exec-e8d79784-b4b7-4735-88f0-1d414800768b` |
| `01-car-price-intro-03-kaggle-data-explorer-crisp.png` | `01-car-price-intro-03-kaggle-data-explorer.jpg` | `(0, 65, 598, 285)` | `01-car-price-intro-03-kaggle-data-explorer-imagegen-crop.jpg` | `exec-2d6a0af7-ba01-42a9-b7a1-87d9071f1a56` |
| `01-car-price-intro-04-msrp-column-crisp.png` | `01-car-price-intro-04-msrp-column.jpg` | `(0, 50, 598, 300)` | `01-car-price-intro-04-msrp-column-imagegen-crop.jpg` plus the legacy clarity crop | `exec-f77aeb51-4dbe-4612-b5c0-e980999e927d` |
| `01-car-price-intro-06-github-repo-crisp.png` | `01-car-price-intro-06-github-repo.jpg` | `(0, 50, 598, 285)` | `01-car-price-intro-06-github-repo-imagegen-crop.jpg` | `exec-ce9d07be-34ce-439b-8d07-1aff25a68d7e` |
| `01-car-price-intro-07-chapter-files-crisp.png` | `01-car-price-intro-07-chapter-files.jpg` | `(0, 175, 598, 95)` | `01-car-price-intro-07-chapter-files-imagegen-crop.jpg` | `exec-cff023f5-31d4-4eae-a892-b2d4d84f5b99` |
| `03-eda-03-long-tail-distribution-crisp.png` | `03-eda-03-long-tail-distribution.jpg` | `(0, 90, 598, 270)` | `03-eda-03-long-tail-distribution-imagegen-crop.jpg` | `exec-8d3c75e9-6545-4806-b3b4-81f76c042425` |
| `03-eda-04-zoom-below-100k-crisp.png` | `03-eda-04-zoom-below-100k.jpg` | `(0, 150, 598, 210)` | `03-eda-04-zoom-below-100k-imagegen-crop.jpg` | `exec-3902e0e0-f706-461e-9a35-86bba0476ef8` |
| `03-eda-06-log1p-normal-distribution-crisp.png` | `03-eda-06-log1p-normal-distribution.jpg` | `(0, 95, 598, 265)` | `03-eda-06-log1p-normal-distribution-imagegen-crop.jpg` | `exec-84d080e6-1f37-497f-96e1-4319c09e5a53` |
| `04-validation-framework-01-train-val-test-split-crisp.png` | `04-validation-framework-01-train-val-test-split.jpg` | `(0, 60, 570, 300)` | `04-validation-framework-01-train-val-test-split-imagegen-crop.jpg` | `exec-e2875f78-747b-4437-aa19-5a68c32b082a` |

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
