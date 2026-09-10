# Deep-learning screenshot rollout: lessons 08–14

Worker: Luna Max
Capability: `imagegen` skill available; built-in imagegen used only for bounded explanatory diagrams after local inspection. Exact code, UI, URLs, plots, numeric output, and fidelity-sensitive screenshots use deterministic crops/upscaling.

Each accepted screenshot below records the source, disposition, crop/preparation, invariants checked, and focused commit. Originals are preserved. Temporary crop/contact-sheet directories remain under `.tmp` and are not committed.

## 08-more-layers

- `08-more-layers-01-inner-layer-diagram.jpg` → `08-more-layers-01-inner-layer-diagram-imagegen.jpg`: regenerated as a clean educational network diagram; preserved vector representation → inner dense layer → output dense layer → T-shirt sequence; removed webcam, capture chrome, and handwritten ambiguity.
- `08-more-layers-02-activation-functions.jpg` → `08-more-layers-02-activation-functions-cropped.jpg`: deterministic crop/upscale of the exact CS231n ReLU excerpt, equation, and plots; removed webcam/capture chrome and preserved the source wording and axes.
- `08-more-layers-03-relu-in-code.jpg` → `08-more-layers-03-relu-in-code-cropped.jpg`: deterministic crop/upscale of the exact notebook model definition; preserved `Dense(size_inner, activation='relu')` and surrounding Keras code; removed webcam/browser chrome.
- `08-more-layers-04-tuning-sizes.jpg` → `08-more-layers-04-tuning-sizes-cropped.jpg`: deterministic crop/upscale of the exact size loop and `10, 100, 1000` values; preserved code and lesson heading; removed webcam/browser chrome.
- `08-more-layers-05-nvidia-smi.jpg` → `08-more-layers-05-nvidia-smi-cropped.jpg`: deterministic crop/upscale of the exact terminal output; preserved Tesla K80, 95% utilization, memory, and process values; removed webcam and browser chrome.
- `08-more-layers-06-val-accuracy-plot.jpg` → `08-more-layers-06-val-accuracy-plot-cropped.jpg`: deterministic crop/upscale of the exact validation plot, labels, and tick values; removed webcam/browser chrome without redrawing data.

## 09-dropout

- `09-dropout-01-motivation-logo.jpg` → `09-dropout-01-motivation-logo-imagegen.jpg`: regenerated as a clean ten-card repetition diagram; preserved the 10-epochs/10-sees concept and removed webcam, capture chrome, and handwritten text.
- `09-dropout-02-hiding-input.jpg` → `09-dropout-02-hiding-input-imagegen.jpg`: regenerated as three clean shirt cards with masks in different positions; preserved random input hiding and removed webcam, capture chrome, spinner, and handwritten text.
- `09-dropout-03-frozen-neuron.jpg` → `09-dropout-03-frozen-neuron-imagegen.png`: regenerated as a clean neural-network diagram with exactly one crossed-out hidden neuron and the “NOT UPDATED DURING TRAINING” invariant; removed webcam and capture chrome.
- `09-dropout-04-v3-diagram.jpg` → `09-dropout-04-v3-diagram-imagegen.jpg`: regenerated as a crisp architecture diagram preserving the exact V3 stage order and labels (`BASE MODEL`, `POOLING`, `VECTORS`, `DENSE(100)`, `DROPOUT(0.5)`, `DENSE(10)`); removed webcam, spinner, and capture chrome.
- `09-dropout-05-tuning-dropout.jpg` → `09-dropout-05-tuning-dropout-cropped.jpg`: deterministic crop/upscale of the exact tuning loop; preserved code, dropout values, and training arguments; removed webcam and browser chrome.
- `09-dropout-06-val-accuracy-dropout.jpg` → `09-dropout-06-val-accuracy-dropout-cropped.jpg`: deterministic crop/upscale of the exact validation plot and legend; removed webcam and browser chrome without redrawing values.
- `09-dropout-07-dropout-02-vs-train.jpg` → `09-dropout-07-dropout-02-vs-train-cropped.jpg`: deterministic crop/upscale of the exact dropout-0.2 plot and code; preserved the 0.84 peak and axes; removed webcam and browser chrome.
- `09-dropout-08-no-regularization-overfit.jpg` → `09-dropout-08-no-regularization-overfit-cropped.jpg`: deterministic crop/upscale of the exact no-regularization plot; preserved the 100% training-vs-validation contrast and removed webcam/browser chrome.

## 10-augmentation

- `10-augmentation-01-generate-more-images.jpg` → `10-augmentation-01-generate-more-images-imagegen.jpg`: regenerated as a clean one-to-many data-augmentation diagram; preserved the source-to-variants teaching point and removed webcam, capture chrome, spinner, and handwritten text.
- `10-augmentation-02-flip-rotation-shift-grids.jpg` → `10-augmentation-02-flip-rotation-shift-grids-cropped.jpg`: deterministic crop/upscale of the exact original/horizontal/vertical/both, rotation, and height-shift grids; removed webcam and browser chrome without changing examples or labels.
- `10-augmentation-03-zoom-grid.jpg` → `10-augmentation-03-zoom-grid-cropped.jpg`: deterministic crop/upscale of the exact `zoom_x`/`zoom_y` grid and parameters; preserved values and annotations, removed webcam and browser chrome.
- `10-augmentation-04-keras-parameters.jpg` → `10-augmentation-04-keras-parameters-cropped.jpg`: deterministic crop/upscale of the exact Keras `ImageDataGenerator` code and highlighted ranges; removed webcam and browser chrome without redrawing code.
- `10-augmentation-05-nvidia-smi-cpu-bound.jpg` → `10-augmentation-05-nvidia-smi-cpu-bound-cropped.jpg`: deterministic crop/upscale of the exact GPU terminal output; preserved Tesla K80 and 61% utilization; removed webcam/browser chrome.
- `10-augmentation-06-val-stuck-077.jpg` → `10-augmentation-06-val-stuck-077-cropped.jpg`: deterministic crop/upscale of the exact train/validation plot and lesson heading; preserved the ~0.95 versus ~0.70–0.77 contrast; removed webcam/browser chrome.

## 11-large-model

- `11-large-model-01-input-size-parameter.jpg` → `11-large-model-01-input-size-parameter-cropped.jpg`: deterministic crop/upscale of the exact `make_model` code; preserved `input_size` usage and input shape; removed webcam/browser chrome.
- `11-large-model-02-generators-shear-zoom-flip.jpg` → `11-large-model-02-generators-shear-zoom-flip-cropped.jpg`: deterministic crop/upscale of the exact generator code; preserved `shear_range=10`, `zoom_range=0.1`, and `horizontal_flip=True`; removed webcam/browser chrome.
- `11-large-model-03-checkpoint-callback.jpg` → `11-large-model-03-checkpoint-callback-cropped.jpg`: deterministic crop/upscale of the exact Keras checkpoint callback and filename template; preserved validation-accuracy monitoring and `save_best_only=True`; removed webcam/browser chrome.
- `11-large-model-04-first-run-step-time.jpg` → `11-large-model-04-first-run-step-time-cropped.jpg`: deterministic crop/upscale of the exact first-run training output; preserved step timing, epoch counts, loss, and accuracy values; removed webcam/browser chrome.
- `11-large-model-05-training-output.jpg` → `11-large-model-05-training-output-cropped.jpg`: deterministic crop/upscale of the exact later training output; preserved epoch metrics and the 0.86–0.89 validation range; removed webcam/browser chrome.
- `11-large-model-06-checkpoint-files.jpg` → `11-large-model-06-checkpoint-files-cropped.jpg`: deterministic crop/upscale of the exact Jupyter file listing; preserved checkpoint filenames and sizes, including `xception_v4_1_13_0.903.h5`; removed webcam/browser chrome.

## 12-using-model

- `12-using-model-01-fresh-notebook-imports.jpg` → `12-using-model-01-fresh-notebook-imports-cropped.jpg`: deterministic crop/upscale of the exact import and test-generator cells; preserved TensorFlow/Keras imports and removed webcam/browser capture chrome.
- `12-using-model-02-load-model-evaluate.jpg` → `12-using-model-02-load-model-evaluate-cropped.jpg`: deterministic crop/upscale of the exact model-loading/evaluation output; preserved checkpoint name, accuracy value, and result array; removed webcam/browser capture chrome.
- `12-using-model-03-load-img-pants.jpg` → `12-using-model-03-load-img-pants-cropped.jpg`: deterministic crop/upscale of the exact `load_img(..., target_size=(299, 299))` cell and pants image; preserved the loaded image and target size; removed webcam/browser capture chrome.
- `12-using-model-04-numpy-batch-shape.jpg` → `12-using-model-04-numpy-batch-shape-cropped.jpg`: deterministic crop/upscale of the exact NumPy conversion and `(1, 299, 299, 3)` output; removed webcam/browser capture chrome.
- `12-using-model-05-classes-prediction-zip.jpg` → `12-using-model-05-classes-prediction-zip-cropped.jpg`: deterministic crop/upscale of the exact `dict(zip(classes, pred[0]))` output; preserved the class scores and pants maximum; removed webcam/browser capture chrome.

## 13-summary

- `13-summary-01-use-case-diagram.jpg` → `13-summary-01-use-case-diagram-imagegen.jpg`: regenerated as a clean upload → fashion-classification-service → T-shirt result diagram; preserved the one-of-ten-category use case and removed webcam, capture chrome, spinner, and handwritten text.
- `13-summary-02-final-predictions.jpg` → `13-summary-02-final-predictions-cropped.jpg`: deterministic crop/upscale of the exact final class-score dictionary; preserved class names and numeric scores; removed webcam/browser capture chrome.
- `13-summary-03-explore-more.jpg` → `13-summary-03-explore-more-cropped.jpg`: deterministic crop/upscale of the exact summary and explore-more bullets; preserved lesson text and removed webcam/browser capture chrome.

## 14-explore-more

- No Markdown image references found.

## Validation

- 34/34 Markdown image references resolve; 34/34 original source files remain; 34/34 report entries exist.
- 6 bounded explanatory diagrams used built-in imagegen after local inspection; 28 exact code/UI/plot/terminal assets used deterministic crop, 2× Lanczos upscale, and light sharpening.
- `git diff --check` passes. Every accepted asset has its own focused commit; no push was performed.
- Limitation: deterministic preparation improves framing and display size but cannot recover detail absent from the 592×360 originals; exact source truncation and relevant notebook UI remain where fidelity requires them.
