#!/usr/bin/env bash
set -euo pipefail

# Reproduce the bounded native crops used for the remaining deployment
# redraws. Coordinates are ImageMagick's x,y,width,height format. The source
# JPGs and published PNGs are never modified by this script.

output_dir="${1:-.}"
mkdir -p "$output_dir"

convert 01-intro-02-model-deployment-diagram.jpg \
  -crop 430x330+20+10 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/01-intro-02-model-deployment-diagram-imagegen-crop.jpg"

convert 01-intro-05-environments.jpg \
  -crop 430x330+20+10 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/01-intro-05-environments-imagegen-crop.jpg"

convert 03-flask-intro-02-request-response.jpg \
  -crop 450x330+25+10 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/03-flask-intro-02-request-response-imagegen-crop.jpg"

convert 05-pipenv-03-isolated-environments.jpg \
  -crop 475x335+8+5 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/05-pipenv-03-isolated-environments-imagegen-crop.jpg"

convert 06-docker-02-containers-on-host.jpg \
  -crop 455x335+15+5 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/06-docker-02-containers-on-host-imagegen-crop.jpg"

convert 06-docker-05-port-mapping.jpg \
  -crop 430x320+25+10 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/06-docker-05-port-mapping-imagegen-crop.jpg"

convert 07-aws-eb-02-eb-architecture.jpg \
  -crop 430x340+25+0 +repage \
  -sampling-factor 2x2,1x1,1x1 -quality 92 \
  "$output_dir/07-aws-eb-02-eb-architecture-imagegen-crop.jpg"
