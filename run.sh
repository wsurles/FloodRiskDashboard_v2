#!/usr/bin/env bash

IMAGE_NAME=floodrisk

echo "|----------------------"
echo "| Running Docker Image"
echo "|----------------------"

docker run -p 8050:8050 -v /Users/wsurles/personal_projects/FloodRiskDashboard_v2/app:/app $IMAGE_NAME 