FROM --platform=linux/amd64 ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Manila

# https://docs.gauge.org/howto/ci_cd/docker.html?os=null&language=python&ide=vscode

# Install dependencies - java, python, etc.
RUN apt-get update && apt-get install -q -y \
    curl \
    zip \
    unzip \
    apt-transport-https \
    gnupg2 \
    ca-certificates \
    openjdk-8-jdk \
    python3.9 \
    python-is-python3 \
    python3-pip \
    docker*

WORKDIR /workspace/unwritten-api

COPY requirements.txt requirements.txt
COPY gauge-docker-compose.sh /gauge-docker-compose.sh

RUN pip3 install --upgrade pip && \
    pip3 install colorama && \
    pip3 install -r requirements.txt

# Install gauge and plugins
RUN curl -SsL https://downloads.gauge.org/stable | sh && \
    gauge -v && \
    gauge install java && \
    gauge install python && \
    gauge install screenshot && \
    gauge install html-report

ENV PATH=$HOME/.gauge:$PATH