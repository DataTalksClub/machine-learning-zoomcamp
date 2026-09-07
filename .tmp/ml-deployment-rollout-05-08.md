# Deployment lessons 05–08 screenshot rollout

Scope: every Markdown image reference in `05-pipenv.md`, `06-docker.md`, `07-aws-eb.md`, and `08-summary.md`.

Rules applied: preserve originals; remove webcam/recording chrome; use imagegen only for bounded explanatory illustrations after source inspection; use deterministic crops and sharpening for exact code, commands, URLs, plots, numeric output, live UI, and fidelity-sensitive visuals. Each accepted screenshot gets one focused commit.

## Accepted assets

- `05-pipenv.md` — `05-pipenv-01-title.jpg` → `05-pipenv-01-title-imagegen.png`: imagegen regeneration of the dependency-management title visual; no face, webcam, recording controls, cursor, or watermark.
- `05-pipenv.md` — `05-pipenv-02-version-conflict.jpg` → `05-pipenv-02-version-conflict-imagegen.png`: imagegen regeneration of the shared-system-Python version-conflict diagram; required service/version labels verified; no face, webcam, recording controls, cursor, or watermark.
- `05-pipenv.md` — `05-pipenv-03-isolated-environments.jpg` → `05-pipenv-03-isolated-environments-imagegen.png`: imagegen regeneration of the isolated-environment diagram; required service/environment/dependency labels verified; no face, webcam, recording controls, cursor, or watermark.
- `05-pipenv.md` — `05-pipenv-04-venv-tools.jpg` → `05-pipenv-04-venv-tools-imagegen.png`: imagegen regeneration of the virtual-environment-tools comparison; required tool labels verified and Pipenv highlighted; no face, webcam, recording controls, cursor, or watermark.
- `05-pipenv.md` — `05-pipenv-05-pipenv-install-lock.jpg` → `05-pipenv-05-pipenv-install-lock-cropped.png`: deterministic crop/upscale/sharpen of the exact Pipfile editor; source values preserved and webcam removed.
- `05-pipenv.md` — `05-pipenv-06-shell-path.jpg` → `05-pipenv-06-shell-path-cropped.png`: deterministic crop/upscale/sharpen of the exact terminal commands and PATH; source text and selection highlight preserved, webcam/whiteboard camera overlay removed.
- `06-docker.md` — `06-docker-01-module-plan.jpg` → `06-docker-01-module-plan-cropped.png`: deterministic crop/upscale/sharpen focused on the exact Docker lesson-plan lines; source text preserved and webcam/UI chrome removed.
- `06-docker.md` — `06-docker-02-containers-on-host.jpg` → `06-docker-02-containers-on-host-imagegen.png`: imagegen regeneration of the bounded container-isolation diagram; host/service/runtime/OS labels verified; no face, webcam, recording controls, cursor, or watermark.
- `06-docker.md` — `06-docker-03-base-image-docker-hub.jpg` → `06-docker-03-base-image-docker-hub-cropped.png`: deterministic crop/upscale/sharpen of the exact Docker Hub tag list; selected `3.8.12-slim` entry preserved and webcam/browser chrome removed.
- `06-docker.md` — `06-docker-04-dockerfile.jpg` → `06-docker-04-dockerfile-cropped.png`: deterministic crop/upscale/sharpen of the exact Dockerfile editor; source instructions preserved and webcam/UI chrome removed.
- `06-docker.md` — `06-docker-05-port-mapping.jpg` → `06-docker-05-port-mapping-imagegen.png`: imagegen regeneration of the bounded port-publishing diagram; both `9696` labels and the service/container flow verified; no face, webcam, recording controls, cursor, or watermark.
- `07-aws-eb.md` — `07-aws-eb-01-module-plan.jpg` → `07-aws-eb-01-module-plan-cropped.png`: deterministic crop/upscale/sharpen focused on the exact AWS Elastic Beanstalk lesson-plan lines; source text preserved and webcam/UI chrome removed.
- `07-aws-eb.md` — `07-aws-eb-02-eb-architecture.jpg` → `07-aws-eb-02-eb-architecture-imagegen.png`: imagegen regeneration of the bounded Elastic Beanstalk architecture diagram; required service/container/load-balancer/autoscaling labels verified; no face, webcam, recording controls, cursor, or watermark.
- `07-aws-eb.md` — `07-aws-eb-03-eb-init.jpg` → `07-aws-eb-03-eb-init-cropped.png`: deterministic crop/upscale/sharpen of the exact EB CLI help and `eb init -p docker churn-serving` command; source text preserved and webcam/whiteboard chrome removed.
- `07-aws-eb.md` — `07-aws-eb-04-eb-local-test.jpg` → `07-aws-eb-04-eb-local-test-cropped.png`: deterministic crop/upscale/sharpen of the exact terminal output and prediction test; values preserved and webcam/whiteboard camera overlay removed.
- `07-aws-eb.md` — `07-aws-eb-05-eb-create.jpg` → `07-aws-eb-05-eb-create-cropped.png`: deterministic crop/upscale/sharpen of the exact EB environment-creation output; load-balancer/autoscaling messages and timestamps preserved, webcam removed.
- `07-aws-eb.md` — `07-aws-eb-06-eb-url-test.jpg` → `07-aws-eb-06-eb-url-test-cropped.png`: deterministic crop/upscale/sharpen of the exact host URL and request code; URL and customer fields preserved, webcam removed.
- `07-aws-eb.md` — `07-aws-eb-07-terminate-environment.jpg` → `07-aws-eb-07-terminate-environment-cropped.png`: deterministic crop/upscale/sharpen of the exact EB console action menu; `Terminate environment` action preserved and browser/webcam chrome removed.
- `08-summary.md` — `08-summary-01-module-plan.jpg` → `08-summary-01-module-plan-cropped.png`: deterministic crop/upscale/sharpen of the exact Pipenv/Docker lesson-plan section; source text preserved and webcam/editor chrome removed.
- `08-summary.md` — `08-summary-02-module-plan-continued.jpg` → `08-summary-02-module-plan-continued-cropped.png`: deterministic crop/upscale/sharpen of the exact Docker/AWS lesson-plan continuation; source text preserved and webcam/editor chrome removed.
- `08-summary.md` — `08-summary-03-summary-list.jpg` → `08-summary-03-summary-list-cropped.png`: deterministic crop/upscale/sharpen of the exact summary-list lesson-plan lines; source text preserved and webcam/editor chrome removed.

## Limitations

- Imagegen assets preserve the lesson concepts and required labels, but are polished semantic regenerations rather than pixel-identical copies of the handwritten source.
- Deterministic assets preserve exact technical text, values, URLs, and native selection highlights; a few long terminal lines remain truncated where the original viewport was truncated.
- All original `.jpg` sources remain beside the regenerated/cropped siblings.
