FROM python:3.7-alpine

ENV PYHTONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LDFLAGS=-L/usr/lib/x86_64-linux-gnu/

RUN apk --no-cache add python3 \
    build-base \
    python3-dev \
    # wget dependency
    openssl \
    # dev dependencies
    git \
    bash \
    sudo \
    py3-pip \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    postgresql-dev \
    musl-dev

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/