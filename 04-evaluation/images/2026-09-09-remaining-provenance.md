# 04-evaluation remaining strict-audit provenance — 2026-09-09

This ledger closes the two `04-evaluation` entries classified
`PROVENANCE-BLOCKED` by the strict audit. The accuracy example was regenerated
with built-in imagegen from its original non-crisp JPG and a bounded native
crop. The threshold/precision/recall infographic was already a direct,
clean imagegen asset with a C2PA manifest and no underlying JPG source; its
bytes are therefore retained unchanged and that exception is recorded below.

## Method

The original JPG is the source of truth for the redraw. The checked-in
[`2026-09-09-remaining-provenance-crops.sh`](2026-09-09-remaining-provenance-crops.sh)
script makes the crop directly with ImageMagick's native
`-crop WIDTHxHEIGHT+X+Y` operation. It performs no resize, Lanczos pass,
sharpening, or other enhancement. The crop script SHA-256 is
`3f93a6c84628f0a4ed584df9e5c3830e5720fab5f33f3428ab1fa2836488be9f`.

The regenerated PNG was supplied only the original JPG and its matching
bounded crop as imagegen references. The prior crisp PNG was not supplied as
an input. Native output and a temporary simulated 608px lesson-width render
were inspected; the 608px files are inspection-only and are not published.

## Source-backed redraw

| Published PNG | Lesson reference | Source JPG | Source crop | Crop `(x, y, width, height)` | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Current PNG SHA-256 | Native | 608px | Imagegen execution | C2PA | RMSE vs resized crop |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|---:|
| `02-accuracy-02-accuracy-example-crisp.jpg` | `02-accuracy.md:15` | `02-accuracy-02-accuracy-example.jpg` | `02-accuracy-02-accuracy-example-imagegen-crop.jpg` | `(27, 0, 450, 330)` | `6809d80b03d165a91f90ca10a051df398eee07cbc2cea7434fbd331601108d12` | `7d8f11b9c795bb28bdfb761a55f417d4933a50a3db37b379dc19273542ec2568` | `ef3c83fcd69c4d82fa71a688d683cc689e3fd95a734f088fa3218bfdf21099f3` | `541a544e2c7740596ef6ee75611f6948595ad49ac8f664fd832a662ec14e142f` | `1617x973` | `608x366` | `exec-c21c61b9-e26d-49d1-9fbf-cf50d97fc1bd` | `urn:c2pa:1be2c010-c039-48e0-82aa-243e7eb47c6c` | `0.246923` |

### Preserved semantics and removed artifacts

- The six score labels remain exactly `0.2`, `0.3`, `0.4`, `0.45`, `0.55`,
  and `0.7`; the result remains `3/6 = 50%` and the threshold remains
  `t > 0.5`.
- Green checks, red crosses, grouping boxes, arrows, and the threshold divider
  remain part of the lesson illustration.
- The webcam tile, recorder wheel, editor controls, cursor, and screenshot
  framing were not carried into the redraw.

## Retained direct imagegen output

| Published PNG | Lesson reference | Current PNG SHA-256 | Native | 608px | C2PA | Decision |
|---|---|---|---:|---:|---|---|
| `09-explore-more-01-threshold-precision-recall-imagegen.jpg` | `09-explore-more.md:6` | `2fad10c2e0fa0ec22048ca3db939ccbe53fabee1f45fe8d4e4398582f82d89bd` | `1672x941` | `608x342` | `urn:c2pa:a71a7ae7-27fe-4d6a-b655-a09148eb7257` | Retained byte-for-byte. This is a brand-new conceptual infographic, not a redraw of a source screenshot; no original non-crisp JPG exists in the module. The embedded C2PA record proves direct imagegen, and native/608px inspection found no face, camera tile, browser/editor chrome, cursor, play control, or selection overlay. |

No source/crop pair is fabricated for this direct imagegen asset. Its content
and lesson semantics remain unchanged.

## Verification

- The two current blocked refs were audited at native size and simulated 608px.
- The source-backed output has embedded C2PA metadata identifying imagegen and
  a material normalized RMSE against the crop resized only for comparison;
  the comparison is not a generation step.
- The retained direct imagegen output remains unchanged and is documented as
  the no-JPG exception above.
