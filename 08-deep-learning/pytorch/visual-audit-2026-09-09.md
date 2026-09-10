# Workshop illustration audit — Deep Learning / PyTorch

Audit date: 2026-09-09

The source video was sampled for durable teaching moments. Direct screenshots
were rejected because the 640x360 recording includes presenter, Zoom, browser,
editor, play-button, and exact-code artifacts. The accepted visual is a
conceptual imagegen redraw of the strongest candidate, using the original frame
and a focused crop as imagegen references. It is not an enlarged screenshot.

## Source and accepted asset

- YouTube video: `Ne25VujHRLA`
- Source: `/home/alexey/git/.tmp/ml-workshop-videos/Ne25VujHRLA.mp4`
- Source SHA-256:
  `bb1f04ece85783fd25fe8b72923e2dcb84c0401ffc5a8c00b2919c684d12538`
- Source properties: `640x360`, `5114.984490` seconds
- Timestamp: approximately `01:08:00` (coarse sample, C05)
- Original frame: `source-frames/coarse/frame-0069.jpg`
- Original frame SHA-256:
  `71e595ac7da2d2b3d342efecf4d457782d6dd4d1f52d4c1496dfd5990c73c485`
- Focused crop: `crops/c05-augmentation-rotation-clean.jpg`,
  `(x=201, y=47, width=270, height=250)`
- Focused crop SHA-256:
  `f0d81013a38246ef5ebc44912b63909fc14a3d2b8f15c6929c4186eb0e553923`
- Published asset:
  `images/training-time-augmentation-imagegen.jpg`
- Published asset SHA-256:
  `492853fe5b868aa37e5d6e51b1ba347949ea21aeedffdd5ebeb50be46592d996`

Both the original frame and the focused crop were supplied to imagegen. The
redraw preserves only the supported relationship: rotation, cropping, and
flipping produce varied training views of the same pants image while retaining
the class label. It removes the presenter, camera/Zoom overlay, editor canvas,
checkerboard residue, exact code, and invented numeric values.

## Review decision

The raw C05 screenshot scored `23/30` as a redraw seed but failed direct
publication because it was an editor screenshot with residue and showed only a
single transformed view. The conceptual redraw passed the independent review:
it is crisp and legible at normal lesson width, accurately complements the
transformation list, contains no faces or transient UI, and is recommended for
publication immediately after the list of common transformations.

Independent review: `/home/alexey/git/.tmp/workshop-processing/ml-2026-deep-learning/INDEPENDENT-REVIEW.md`.
