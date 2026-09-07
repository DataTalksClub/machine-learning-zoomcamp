# Deep-learning screenshot rollout: lessons 01–07

Worker: Luna Max
Capability: `imagegen` skill available; built-in imagegen used only for bounded explanatory diagrams after local inspection. Exact code, UI, URLs, plots, numeric output, and fidelity-sensitive screenshots use deterministic crops/upscaling.

Each accepted screenshot below records the source, disposition, crop/preparation, invariants checked, and focused commit. Originals are preserved.

## 01-fashion-classification

- `01-fashion-classification-01-tabular-vs-images.jpg` → `01-fashion-classification-01-tabular-vs-images-imagegen.png`: imagegen illustration. Source inspected and cropped to `+22+0 478x360` before generation; preserved CSV/table versus black t-shirt teaching point, exact `model`, `make`, `mpg`, blank column, `MSRP` order, and removed presenter/camera/recording chrome. Accepted after a targeted correction from an incorrect `gender` label to the source's `make` label.
- `01-fashion-classification-02-upload-service.jpg` → `01-fashion-classification-02-upload-service-imagegen.png`: imagegen illustration. Source inspected and cropped to `+22+0 478x360`; preserved user → upload box → fashion classification service → `T-SHIRT` flow, the `CATEGORY: T-SHIRT` result, `FINISH` control, and removed presenter/camera/recording chrome.
- `01-fashion-classification-03-clothing-dataset.jpg` → `01-fashion-classification-03-clothing-dataset-cropped.png`: deterministic exact-UI crop `+0+0 500x360`, upscaled 2× with Lanczos and mild sharpening. Preserved the GitHub dataset title, 5,000+ image count, 20 classes, clothing grid, and contributor panel; removed the webcam/black recording strip without regenerating browser text.
- `01-fashion-classification-04-dataset-small-train.jpg` → `01-fashion-classification-04-dataset-small-train-cropped.png`: deterministic exact-UI crop `+0+0 500x360`, upscaled 2× with Lanczos and mild sharpening. Preserved the repository, `train` path, and visible category folders; removed webcam/black recording chrome and kept the exact GitHub labels.
- `01-fashion-classification-05-cs231n.jpg` → `01-fashion-classification-05-cs231n-cropped.png`: deterministic exact-UI crop `+0+0 500x360`, upscaled 2× with Lanczos and mild sharpening. Preserved the CS231n course heading, course-site button, assignments, and module list; removed the recording strip without approximating webpage text.
- `01-fashion-classification-06-notebook-plan.jpg` → `01-fashion-classification-06-notebook-plan-cropped.png`: deterministic notebook crop `+0+0 500x360`, upscaled 2× with Lanczos and mild sharpening. Preserved the fashion-classification heading, dataset links, CS231n link, clone command, and TensorFlow/Keras section; removed webcam/black recording chrome and retained exact URLs/code.
- `01-fashion-classification-07-notebook-plan-2.jpg` → `01-fashion-classification-07-notebook-plan-2-cropped.png`: deterministic notebook crop `+0+0 500x360`, upscaled 2× with Lanczos and mild sharpening. Preserved the exact experiment, data-augmentation, and 299×299 training-plan text/cells; removed webcam/black recording chrome without regenerating notebook UI.
