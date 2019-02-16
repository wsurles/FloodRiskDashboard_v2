#!/usr/bin/env bash

## This will get used alot so lets parametize it
IMAGE_NAME=floodrisk

## build my docker file. this creates an image with a tag
echo "|----------------------"
echo "| Building docker image:" $IMAGE_NAME
echo "|----------------------"

#docker build --no-cache -t $IMAGE_NAME .
docker build -t $IMAGE_NAME .