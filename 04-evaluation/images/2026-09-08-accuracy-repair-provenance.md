# Evaluation illustration repair provenance — 2026-09-08

## Scope

This record covers one published illustration and one Markdown reference:

- `02-accuracy-01-accuracy-vs-threshold-crisp.png` was rebuilt from the 21 values printed in `../02-accuracy.md`.
- The image reference to `03-confusion-table-07-accuracy-from-table-crisp.jpg` was removed from `../03-confusion-table.md` because the lesson already contains the native confusion table/output and the screenshot contains the incorrect `FP 8%` value. The JPG and PNG source assets were intentionally left in place.

The other 16 unresolved evaluation assets are out of scope and are not being marked complete by this repair.

## Accuracy plot source data

The source of truth is the lesson output block in `../02-accuracy.md` (the `np.linspace(0, 1, 21)` loop), not the previous screenshot or its old curve:

```text
threshold: 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
accuracy:  0.274 0.509 0.591 0.666 0.710 0.739 0.760 0.772 0.785 0.793 0.803 0.801 0.795 0.786 0.766 0.744 0.735 0.726 0.726 0.726 0.726
```

The previous PNG peaked around `0.76`; the repaired curve peaks at exactly `0.803` for threshold `0.50`.

## Reproducible render

`02-accuracy-01-accuracy-vs-threshold-source.svg` is a native deterministic SVG. Its comment and `data-*` attributes contain the exact values, and its path uses this explicit transform:

```text
x = 130 + 1300 * threshold
y = 870 - (accuracy - 0.2) * 830 / 0.62
```

The published PNG was rendered from that SVG with ImageMagick:

```bash
convert -background white -alpha remove -alpha off \
  02-accuracy-01-accuracy-vs-threshold-source.svg \
  -depth 8 02-accuracy-01-accuracy-vs-threshold-crisp.png
```

No imagegen, enlargement, sharpening, or screenshot-derived curve was used. The original JPG remains preserved for historical/source comparison.

## Validation

- The source SVG and published PNG are both `1488×992`.
- The path has 21 points at thresholds `0.00` through `1.00` in `0.05` increments.
- The rendered path coordinates were checked against the 21 values above using the documented transform; the highest point is `0.803` at `0.50`.
- The published PNG was inspected at native resolution and at the 608px lesson display width; axes, labels, curve, and peak remain crisp and readable.
- `03-confusion-table.md` now retains the native code, output array, and Markdown table; only the duplicate image reference was removed.
