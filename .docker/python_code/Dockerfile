FROM ubuntu:latest as alpha
ENV BUILD_DEPS="build-essential" \
    APP_DEPS="python3 python3-dev python3-venv python3-pip curl git ssh gcc openssh-client supervisor wget python3-setuptools python3-pip"
RUN export DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get install -y tzdata
RUN apt-get update && apt-get install -y ${BUILD_DEPS} ${APP_DEPS}

FROM alpha as bravo
WORKDIR /tmp
COPY .docker/python_code/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && rm -rf /tmp/requirements.txt

FROM bravo as charlie
COPY . /opt/app

FROM  charlie as delta
COPY .docker/python_code/docker-entrypoint.sh /bin/docker-entrypoint.sh
RUN chmod +x /bin/docker-entrypoint.sh
ENTRYPOINT ["/bin/docker-entrypoint.sh"]
