FROM python:latest as alpha
ENV BUILD_DEPS="build-essential" \
    APP_DEPS="python3 python3-dev python3-venv python3-pip curl git ssh gcc openssh-client supervisor wget python3-setuptools python3-pip"

RUN export DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get install -y tzdata
RUN apt-get update && apt-get install -y ${BUILD_DEPS} ${APP_DEPS}

