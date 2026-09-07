# Regression intro screenshot rollout

## 01 — select best price

- Disposition: `keep` via deterministic crop/export; the image teaches the user-facing price-entry problem that motivates the car-price model.
- Source/context: `cohorts/2026/02-regression/images/01-car-price-intro-01-select-best-price.jpg`; caption: “How can we help our user select the best price”.
- Crop coordinates: source `598x360`; `504x336+0+24` (`x=0, y=24, width=504, height=336`). The crop removes the DataTalks.Club watermark, top-left recording marker, webcam tile, right black bar, and keeps the slide content.
- Invariants: preserve the title “How can we help our user select the best price?”, the thinking figure with phone, the Price/Exchange control, the `$0000?` field, the `UAH` selector, and the red “Required field” state.
- Path: deterministic crop/export from the original; final asset `cohorts/2026/02-regression/images/01-car-price-intro-01-select-best-price-cropped.jpg`.
- QA: source inspected in lesson context; exact UI/text preserved; no face, webcam, browser/Zoom chrome, cursor, watermark, or black border remains; final dimensions `504x336`; lesson reference resolves; `git diff --check` passes before commit.
