#!/bin/bash

DOCKER_SETTINGS_FILE="docker_settings.txt"

source $DOCKER_SETTINGS_FILE

[ -z $CONTAINER_NAME ] && echo "Missing CONTAINER_NAME field in $DOCKER_SETTINGS_FILE" && exit
[ -z $PORT ] && echo "Missing PORT field in $DOCKER_SETTINGS_FILE" && exit
[ -z $MODEL_PATH ] && echo "Missing MODEL_PATH field in $DOCKER_SETTINGS_FILE" && exit
[ -z $VERSION ] && echo "Missing VERSION field in $DOCKER_SETTINGS_FILE" && exit

echo You launched an image build with the following settings:
echo + CONTAINER_NAME=$CONTAINER_NAME
echo + PORT=$PORT
echo + MODEL_PATH=$MODEL_PATH
echo + VERSION=$VERSION

MODEL_DIR=$(dirname "$MODEL_PATH")

docker run --name $CONTAINER_NAME \
	   -v $MODEL_DIR:$MODEL_DIR:ro \
           -dti \
           -p $PORT:8123 \
           iris_app_image:$VERSION

# uncomment and add to docker run if in development mode
#-v /home/mremiseaneo/projects/project_template/:/opt/sources/project_template/ \
