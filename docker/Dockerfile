FROM ubuntu:16.04

# ------------------------------------------------------------------------
# Install tools to build the darknet from the source codes.
# ------------------------------------------------------------------------

RUN apt-get update && \
    apt-get install -y git make gcc g++ wget vim-tiny python3

# ------------------------------------------------------------------------
# Building the Darknet from the source codes.
# ------------------------------------------------------------------------

WORKDIR /root
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR darknet
RUN make

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
    cat 2007_* 2012_train.txt > train.txt

# Modify Cfg for Pascal Data
RUN DATA_FILE="cfg/voc.data" && \
    cat $DATE_FILE | (rm $DATA_FILE; sed -e "s/home\/pjreddie/root\/darknet/g" > $DATA_FILE)

# Download Pretrained Convolutional Weights
RUN wget -q https://pjreddie.com/media/files/darknet53.conv.74

