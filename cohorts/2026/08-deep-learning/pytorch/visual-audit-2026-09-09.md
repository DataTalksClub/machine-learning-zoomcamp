# PyTorch workshop visual audit

Date: 2026-09-09
Scope: [PyTorch workshop README](README.md) and source video `Ne25VujHRLA` only

## Result

No image is published. The README had no image references before this audit and
still has none. Six transcript-backed moments were worth checking, but no frame
could be acquired for visual review, so none can pass the rubric's readability,
fidelity, or caption hard gates. No imagegen regeneration was run without an
original frame and native crop.

## Source and temporary provenance

- Source: `https://www.youtube.com/watch?v=Ne25VujHRLA`
- Transcript: `/home/alexey/.cache/youtube_transcripts/Ne25VujHRLA.txt`
- Temporary source/candidate workspace: `/home/alexey/git/.tmp/mlzoomcamp-pytorch-audit/`
- Local source video: not acquired; no source video or candidate frame was copied into the repository.
- Route A (`yt-dlp` through the documented sticky Oxylabs session): unavailable with the documented `407 Proxy Authentication Required` quota response.
- Route B (the documented Piped/Invidious mirror rotation): no usable stream metadata; Piped returned bot-block/error responses and the available Invidious endpoints were disabled, blocked, or challenge pages. The browser embed also returned `LOGIN_REQUIRED`.

The strict `0/12` scores below mean “not reviewable and therefore rejected,”
not that the transcript-backed teaching point is inherently worthless. Crop
coordinates are `—` because no source frame exists to crop.

## Candidate ledger

| Timestamp | Workshop section | Teaching point | Score | Crop coordinates | Disposition |
| --- | --- | --- | ---: | --- | --- |
| 18:30 | 3. Pre-trained Models | A pretrained ImageNet model produces ranked class predictions for a clothing image before task-specific training. | 0/12 | — | Reject: no frame to verify the output or readability; exact output would require native source rendering. |
| 31:16 | 5. Transfer Learning | Freeze the pretrained feature extractor, pool its 1,280 features, and replace the original head with 10 clothing outputs. | 0/12 | — | Reject: no frame to inspect; if recovered, this conceptual relationship is eligible for crop plus imagegen regeneration. |
| 41:18 | 5. Transfer Learning | The manual PyTorch loop reports train/validation loss and accuracy across epochs. | 0/12 | — | Reject: no frame to verify the measured result; exact logs are source data, not imagegen material. |
| 45:42 | 6. Tuning the Learning Rate | The reading-speed analogy explains why an overly high or low learning rate can hurt training. | 0/12 | — | Reject: no frame to inspect; if the drawn analogy is present, it is eligible for crop plus imagegen regeneration. |
| 67:45 | 10. Data Augmentation | Rotation, cropping, flipping, zooming, and related variants create new training views from one image. | 0/12 | — | Reject: no frame to inspect; if the transformation visual is present, it is eligible for crop plus imagegen regeneration. |
| 79:24 | 11. Using the Trained Model | The final model maps a preprocessed image to clothing-class scores, with pants as the winning class. | 0/12 | — | Reject: no frame to verify the exact scores; exact values must remain native/deterministic. |

These are the minimum plausible candidates from the transcript. Setup screens,
browser/Colab navigation, repeated code cells, checkpoint filenames, and the
ONNX export cell were excluded because they are already expressible in the
README or fail the rubric's complementarity hard gate.

## Reopening this audit

When a local source becomes available, extract only the six timestamps above
plus nearby `±3 s` candidates under `.tmp`, inspect every frame at lesson size,
record real source dimensions and crop coordinates here, and publish only a
candidate that scores at least 7/12 without a hard-gate violation. Preserve
exact code, UI, plots, numbers, and outputs deterministically; use imagegen
only for a bounded conceptual diagram after retaining both the original frame
and native crop.
