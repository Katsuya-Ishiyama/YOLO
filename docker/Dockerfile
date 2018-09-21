FROM ubuntu:16.04

# Install tools to build the darknet from the source codes.
RUN apt-get update && \
    apt-get install -y git make gcc g++

# Build the darknet.
WORKDIR /root
RUN git clone https://github.com/pjreddie/darknet.git

WORKDIR darknet
RUN make

# Download pretrained weights of YOLOv3
RUN apt-get install -y wget
# Comment out downloading weights file of YOLOv1 when debugging
# because its size is 753MB.
# RUN wget -q https://pjreddie.com/media/files/yolov1.weights

RUN wget -q https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar && \
    wget -q https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar && \
    wget -q https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar && \
    tar xf VOCtrainval_11-May-2012.tar && \
    tar xf VOCtrainval_06-Nov-2007.tar && \
    tar xf VOCtest_06-Nov-2007.tar

RUN apt-get install -y python3 && \
    wget -q https://pjreddie.com/media/files/voc_label.py && \
    python3 voc_label.py && \
    cat 2007_* 2012_train.txt > train.txt && \
    cat examples/yolo.c | (rm examples/yolo.c; sed -e "7 s/data/root\/darknet\/data/g" > examples/yolo.c) && \
    cat examples/yolo.c | (rm examples/yolo.c; sed -e "8 s/home\/pjreddie/root\/darknet/g" > examples/yolo.c)

