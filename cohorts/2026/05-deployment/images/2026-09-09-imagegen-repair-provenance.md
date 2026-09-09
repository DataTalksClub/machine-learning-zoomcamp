# Imagegen repair provenance — deployment

## `05-pipenv-02-version-conflict-imagegen.png`

- Lesson reference: `cohorts/2026/05-deployment/05-pipenv.md:21`
- Repair reason: the previous redraw contained an unlabeled yellow mark and omitted the source annotation `INSTALLS THE LATEST`.
- Original source JPG: `05-pipenv-02-version-conflict.jpg`
- Source dimensions: `598x360`
- Source SHA-256: `6f579e3ac4154e9aeb56536e6b29f001b3be442fafd7bbd66270902ce195910c`
- Retained bounded crop: `05-pipenv-02-version-conflict-imagegen-crop.jpg`
- Crop coordinates: `555x300+23+0` (`x=23`, `y=0`, `width=555`, `height=300`)
- Crop SHA-256: `e5f10b6ee2f18f6857129841a068b4be888c63dad18966f89ff944536e3bb231`
- Imagegen output: `05-pipenv-02-version-conflict-imagegen.png`
- Output dimensions: `1706x922`
- Output SHA-256: `64e6751a8bd29772b7209767927ba47b98c899ea7ab9433312d974544a11fce3`
- C2PA metadata: present; URN `urn:c2pa:8cfcb601-1235-4936-bfed-e98bb58fbe30`
- Generation method: built-in imagegen with the original JPG and the retained bounded crop supplied as references. This is a redraw, not an upscale or sharpened crop.
- Resize-only comparison: normalized RMSE `0.349921` against the bounded crop resized to `1706x922`, confirming that the output is materially regenerated rather than a resize-only copy.

### Preserved invariants

- The shared system-Python dependency conflict remains explicit: `CHURN SERVICE` uses `scikit-learn == 0.24.2`, while `LEAD SCORING SERVICE` uses `scikit-learn == 1.0`.
- The shared installation path and package flow remain visible: `$PATH`, `~/anaconda3/bin/pip`, `python`, `pypi.org`, and `.wheel`.
- The source annotation `INSTALLS THE LATEST` is restored verbatim.
- The title `5.5 ENVIRONMENT & DEPENDENCY MANAGEMENT` is retained.

### Removed artifacts

- Presenter face/camera inset
- Screen-recording cursor and controls
- Black frame borders and lower-right gauge
- Unexplained yellow scribble/mark

### Verification

- Native output inspected at `1706x922`.
- Lesson-width render inspected at `608x329`.
- Required labels and version values were checked in both views.
- No face, camera inset, browser/recording chrome, cursor, watermark, or unlabeled yellow mark remains.
