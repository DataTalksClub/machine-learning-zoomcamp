# 2026 homework implementation snapshot

## Scope

This source page records the implementation pass for the four assignments that
were still marked `[DRAFT]` in the 2026 course index: HW5 deployment, HW8 deep
learning, HW9 serverless, and HW10 Kubernetes.

The evidence is local repository state as of 2026-09-14. It is implementation
evidence, not a claim that the external course forms or release assets are
permanent. The relevant directories are
`cohorts/2026/homework/05-deployment/`,
`cohorts/2026/homework/08-deep-learning/`,
`cohorts/2026/homework/09-serverless/`, and
`cohorts/2026/homework/10-kubernetes/`.

## Deployment release

`course_lead_scoring_2026.csv` is the input for `train.py`. The checked-in
`pipeline.bin` has SHA-256
`1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1`, and
`model_metadata.json` records the dataset hash, eight features, Scikit-Learn
1.7.2, and training-set median imputation. `predict.py` exposes `/health` and
`/predict` with a fixed response schema.

The local API smoke test returned `0.769799` for the second exercise lead and
the expected boolean conversion. The canonical container built successfully
from the pinned Python and uv image digests; running it returned the same
probability and health checksum.

## Deep learning release

The hair archive hash is
`9e53453e3017502f22860cb08558f0cdb343e102fb61feab75960616185e7d67`. The
manifest records 1,002 image files, one ignored GIF, and 1,001 images consumed
by `ImageFolder`: 800 train and 201 held-out evaluation examples.

`reference_train.py` fixes Python 3.11 CPU wheels, PyTorch 2.9.0+cpu,
torchvision 0.24.0+cpu, seed 42, deterministic algorithms, two fixed loader
seeds, zero workers, a fixed binary-logit/loss contract, and a non-random
evaluation transform. It writes baseline and augmented histories rather than
asking students to choose a nearest value from unstable options.

The captured CPU reference run produced baseline median training accuracy
`0.808125`, baseline training-loss population standard deviation `0.139341`,
augmented evaluation-loss mean `0.575452`, and augmented last-five evaluation
accuracy `0.723383`. The homework uses tolerances around these values.

## Serverless release

`asset_manifest.json` freezes the ONNX model, external-data file, and sample
image. The model and data hashes are respectively
`2b1adcb51745b73609ac7efebf3b6199483a931ed6dfe35ab925978f4357c2d8` and
`6ba88582d6098a535f918d9a56ad23800f919ad7bd5aad67e5b2bb3e289e5a7e`; the
sample image hash is
`6b3ae4003b5b6d54b51ee4d5fc5f183126bb1be0bf7066e5a846785fdcbfd2f5`.

The direct Lambda handler and a Lambda base-image container both returned
`straight_probability=0.727697` for the sample. The 2026 preprocessing uses
explicit RGB conversion, bilinear resize, ImageNet normalization, NCHW layout,
and float32 values in both paths.

## Kubernetes release

The checked-in manifests use image `zoomcamp-model:2026-hw10`, container port
9696, a `ClusterIP` service, selector `app: subscription`, CPU requests for HPA
metrics, and an `autoscaling/v2` HPA with one to three replicas. The manifests
parse as YAML. `kind` and `kubectl` were unavailable in the verification
environment, so a live cluster rollout remains an explicit external check.

## Residual risks

The external hair archive, ONNX assets, PyTorch wheels, AWS Lambda base image,
and course submission forms are outside this repository. Their checksums or
versions are recorded where possible, but a public release should mirror or
tag them immutably and run the assignments from a clean checkout on at least
one supported CPU platform.
