#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# These are native bounded crops only. No resize, Lanczos, sharpening, or
# other enhancement is permitted: the original JPG and this crop are the
# only source references supplied to imagegen.
crop="475x360+23+0"

for stem in \
  01-overview-01-tf-serving-inference \
  01-overview-02-architecture \
  01-overview-03-grpc \
  01-overview-04-kubernetes \
  05-kubernetes-intro-01-cluster-nodes-pods \
  05-kubernetes-intro-02-deployments
do
  convert "$root/$stem.jpg" -crop "$crop" +repage -quality 100 "$root/$stem-imagegen-crop.jpg"
done
