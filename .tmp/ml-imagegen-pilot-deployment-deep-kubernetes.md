# ML imagegen pilot: deployment / deep learning / Kubernetes

## Implemented pilot

### Deployment architecture overview

- **Source path:** `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/05-deployment/images/01-intro-02-model-deployment-diagram.jpg`
- **Lesson/unit:** `cohorts/2026/05-deployment/01-intro.md`, immediately after the explanation that a marketing service calls a deployed churn-model API.
- **Learner should notice:** A model trained in a Jupyter notebook is saved as `model.bin`; the churn service loads the model; the marketing service sends customer requests to the churn service and receives predictions.
- **Source inspection:** The source is a 540×360 workshop frame with a warm whiteboard, handwritten architecture sketch, webcam inset at the top-right, Zoom controls, and a color-wheel overlay at the bottom-right.
- **Crop first:** Yes. Crop coordinates were `x=25, y=10, width=465, height=250` in source pixels. This isolates the title and the main boxes/arrows while removing the bottom controls/overlay; the remaining small webcam fragment was removed during regeneration.
- **Imagegen prompt:**

  ```text
  Use case: scientific-educational
  Asset type: crisp course illustration for an ML deployment lesson
  Input images: Image 1 is the cropped source sketch and the sole edit/reference target. Reconstruct its instructional diagram faithfully.
  Primary request: Create a clean, crisp, high-resolution educational diagram based on the source whiteboard sketch. Show the deployment flow: a Jupyter Notebook containing a model, an arrow to a saved model.bin file, a marketing service sending requests to a churn service, and the churn service containing a model. Remove all webcam, Zoom controls, browser chrome, overlays, and black borders.
  Scene/backdrop: uncluttered warm off-white canvas
  Subject: a simple architecture flow diagram with three outlined boxes and clear directional arrows
  Style/medium: polished hand-drawn educational infographic, restrained marker-like lines, visually faithful to the original layout but cleaner and more legible
  Composition/framing: landscape aspect ratio; Jupyter Notebook box upper-left, model.bin file upper-middle/right, Marketing Service lower-left, Churn Service right; preserve the source arrows and hierarchy; generous margins
  Text (verbatim): "5.1 OVERVIEW", "JUPYTER NOTEBOOK", "model", "model.bin", "MARKETING SERVICE", "CHURN SERVICE", "MODEL"
  Constraints: preserve these labels exactly, preserve the relationships and arrow directions, do not invent any numeric results or additional components, no people, no webcam, no Zoom/browser UI, no watermark.
  Avoid: photorealism, decorative icons, extra text, altered architecture, code blocks, fake metrics, illegible typography.
  ```

- **Invariants / QA:** The output keeps all seven required labels verbatim; keeps the notebook→`model.bin` arrow and marketing→churn request flow; keeps the churn-service model box; does not introduce numeric results, code, extra services, people, browser/Zoom UI, or watermark. The generated labels and arrows are readable at normal display size. The source lesson Markdown now points to the regenerated sibling asset; the original JPEG remains untouched.
- **Output path:** `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/05-deployment/images/01-intro-02-model-deployment-diagram-imagegen-pilot.png`
- **Why this is a good pilot:** It has high instructional contribution and durability: the architecture is the conceptual entry point for deployment, and the diagram communicates relationships better than prose alone. It is a safe regeneration target because the source is mostly a diagram rather than exact code or a data plot, and the distracting workshop chrome can be removed without changing the concept. Rubric decision: `crop/replace` (pilot replacement), expected to score strongly on contribution, relevance, complementarity, durability, and accessibility once the regenerated asset is used.
- **Risks:** Imagegen can still misspell short technical labels or subtly change arrow semantics. Reviewers should recheck `model.bin`, the direction of both flows, and the distinction between the saved artifact and the loaded model. Do not use this workflow for exact code, commands, URLs, or numeric results.

## Do not regenerate with imagegen

- `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/05-deployment/images/04-flask-deployment-02-predict-py.jpg` — code-heavy editor screenshot. Exact Python syntax, field names, and URL construction are the instructional content; generated text is not reliable enough. Keep the code in Markdown or replace it with a deterministic code-rendered image.
- `/home/alexey/git/machine-learning-zoomcamp/cohorts/2026/08-deep-learning/images/05-transfer-learning-08-history-plot.jpg` — the plot is evidence for exact train/validation behavior. A regenerated plot could invent or smooth points and alter the learner’s quantitative conclusion; reproduce it deterministically from the notebook instead.
