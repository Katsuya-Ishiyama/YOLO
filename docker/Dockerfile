FROM ubuntu:16.04

# Install tools to build the darknet from the source codes.
RUN apt-get update && \
    apt-get install -y git make gcc g++

# Build the darknet.
WORKDIR ~
RUN git clone https://github.com/pjreddie/darknet.git

WORKDIR darknet
RUN make

# Download pretrained weights of YOLOv3
RUN apt-get install -y wget
# Comment out downloading weights file of YOLOv1 when debugging
# because its size is 753MB.
# RUN wget -q https://pjreddie.com/media/files/yolov1.weights

RUN apt-get install -y python3 && \
    wget -q https://pjreddie.com/media/files/voc_label.py && \
    python3 voc_label.py

