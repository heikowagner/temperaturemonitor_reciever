FROM python:slim

RUN apt-get -y update
RUN apt-get -y install python3-pip
RUN pip3 install RPi.GPIO
RUN pip3 install spidev
RUN pip3 install numpy

RUN apt-get update && apt-get install -y \
        python-dev python-pip python-setuptools \
        libffi-dev libxml2-dev libxslt1-dev \
         zlib1g-dev libfreetype6-dev \
        liblcms2-dev libwebp-dev python-tk

RUN apt-get -y install python-pil python3-pil


RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y \
    install xvfb sudo \
    git wget python3-numpy python3-scipy netpbm \
    python3-pyqt5 ghostscript libffi-dev libjpeg-turbo-progs \
    python3-setuptools virtualenv \
    python3-dev cmake \
    libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev \
    python3-tk \
    libharfbuzz-dev libfribidi-dev && apt-get clean
    
    
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow

RUN apt-get -y install p7zip-full
ADD waveshare_2inch_LCD ./src/waveshare_2inch_LCD
ADD pic /pic

RUN pip3 install sanic
RUN pip3 install pandas

COPY src/ ./src
RUN chmod 777 ./src/entrypoint.sh
CMD ./src/entrypoint.sh
