#!/bin/bash

DOCKER_SETTINGS_FILE="docker_settings.txt"

source $DOCKER_SETTINGS_FILE

[ -z $VERSION ] && echo "Missing VERSION field in $DOCKER_SETTINGS_FILE" && exit

echo You launched an image build with the following settings:
echo + VERSION=$VERSION


docker build -t iris_app_image:$VERSION -f Dockerfile ../../../

