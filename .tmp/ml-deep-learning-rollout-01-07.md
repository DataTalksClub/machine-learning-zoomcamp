# Deep-learning screenshot rollout: lessons 01–07

Worker: Luna Max
Capability: `imagegen` skill available; built-in imagegen used only for bounded explanatory diagrams after local inspection. Exact code, UI, URLs, plots, numeric output, and fidelity-sensitive screenshots use deterministic crops/upscaling.

Each accepted screenshot below records the source, disposition, crop/preparation, invariants checked, and focused commit. Originals are preserved.

## 01-fashion-classification

- `01-fashion-classification-01-tabular-vs-images.jpg` → `01-fashion-classification-01-tabular-vs-images-imagegen.png`: imagegen illustration. Source inspected and cropped to `+22+0 478x360` before generation; preserved CSV/table versus black t-shirt teaching point, exact `model`, `make`, `mpg`, blank column, `MSRP` order, and removed presenter/camera/recording chrome. Accepted after a targeted correction from an incorrect `gender` label to the source's `make` label.
