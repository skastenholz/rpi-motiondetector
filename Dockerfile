FROM resin/rpi-raspbian:jessie
MAINTAINER Stefan Kastenholz <stefan.kastenholz@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends python-dev python-pip build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install paho-mqtt pyyaml RPi.GPIO

COPY MotionDetector.py .
COPY MotionDetector.yml .

CMD ["/usr/bin/python","MotionDetector.py"]
