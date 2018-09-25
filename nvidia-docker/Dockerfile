FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# ------------------------------------------------------------------------
# Install tools to build the darknet from the source codes.
# ------------------------------------------------------------------------

RUN apt-get update && \
    apt-get install -y git make gcc g++ wget vim-tiny python3 tmux
# FIX ME: apt-get returns "Failed to fetch", I don't know why...
# RUN apt-get install -y --fix-missing gdb

# ------------------------------------------------------------------------
# Building the Darknet from the source codes.
# ------------------------------------------------------------------------

WORKDIR /root
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR darknet
# Building the darknet as debug mode
RUN cat Makefile | (rm Makefile; sed -e "1 s/GPU=0/GPU=1/g" > Makefile) && \
    cat Makefile | (rm Makefile; sed -e "5 s/DEBUG=0/DEBUG=1/g" > Makefile) && \
    cat Makefile | (rm Makefile; sed -e "37 s/$/ -pg/g" > Makefile) && \
    make

# Comment out downloading weights file of YOLOv1 when debugging
# because its size is 753MB.
# RUN wget -q https://pjreddie.com/media/files/yolov1.weights

# ------------------------------------------------------------------------
# Training YOLO on VOC
# ------------------------------------------------------------------------

# Get The Pascal VOC Data
RUN wget -q https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar && \
    wget -q https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar && \
    wget -q https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar && \
    tar xf VOCtrainval_11-May-2012.tar && \
    tar xf VOCtrainval_06-Nov-2007.tar && \
    tar xf VOCtest_06-Nov-2007.tar

# Generate Labels for VOC
RUN wget -q https://pjreddie.com/media/files/voc_label.py && \
    python3 voc_label.py && \
    mkdir data/voc && \
    cat 2007_* 2012_train.txt > data/voc/train.txt

# Modify Cfg for Pascal Data
RUN cat cfg/voc.data | (rm cfg/voc.data; sed -e "s/home\/pjreddie/root\/darknet/g" > cfg/voc.data)

# Download Pretrained Convolutional Weights
RUN wget -q https://pjreddie.com/media/files/darknet53.conv.74

# Display row numbers to use when debugging
RUN echo "set number" > ~/.vimrc
