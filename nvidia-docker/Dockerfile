FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# ------------------------------------------------------------------------
# Install tools to build the darknet from the source codes.
# ------------------------------------------------------------------------

RUN apt-get update && \
    apt-get install -y git build-essential cmake wget vim-tiny python3 \
                       tmux unzip pkg-config libgtk2.0-dev libavcodec-dev \
                       libavformat-dev libswscale-dev && \
    apt-get clean
# FIX ME: apt-get returns "Failed to fetch", I don't know why...
# RUN apt-get install -y --fix-missing gdb

# ------------------------------------------------------------------------
# Installing OpenCV
# This operation is based on: 
#    https://github.com/takuya-takeuchi/Demo/blob/master/Dockerfiles/yolo-darknet/9.1-cudnn7-devel-ubuntu16.04/Dockerfile
# ------------------------------------------------------------------------
WORKDIR /tmp
RUN wget -q https://github.com/opencv/opencv/archive/3.4.0.zip && \
    unzip 3.4.0.zip && \
    mkdir opencv-3.4.0/build
WORKDIR opencv-3.4.0/build
RUN cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local \
-D BUILD_CUDA_STUBS=OFF \
-D BUILD_DOCS=OFF \
-D BUILD_EXAMPLES=OFF \
-D BUILD_JASPER=OFF \
-D BUILD_JPEG=OFF \
-D BUILD_OPENEXR=OFF \
-D BUILD_PACKAGE=ON \
-D BUILD_PERF_TESTS=OFF \
-D BUILD_PNG=OFF \
-D BUILD_SHARED_LIBS=ON \
-D BUILD_TBB=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_TIFF=OFF \
-D BUILD_WITH_DEBUG_INFO=ON \
-D BUILD_ZLIB=OFF \
-D BUILD_WEBP=OFF \
-D BUILD_opencv_apps=ON \
-D BUILD_opencv_calib3d=ON \
-D BUILD_opencv_core=ON \
-D BUILD_opencv_cudaarithm=OFF \
-D BUILD_opencv_cudabgsegm=OFF \
-D BUILD_opencv_cudacodec=OFF \
-D BUILD_opencv_cudafeatures2d=OFF \
-D BUILD_opencv_cudafilters=OFF \
-D BUILD_opencv_cudaimgproc=OFF \
-D BUILD_opencv_cudalegacy=OFF \
-D BUILD_opencv_cudaobjdetect=OFF \
-D BUILD_opencv_cudaoptflow=OFF \
-D BUILD_opencv_cudastereo=OFF \
-D BUILD_opencv_cudawarping=OFF \
-D BUILD_opencv_cudev=OFF \
-D BUILD_opencv_features2d=ON \
-D BUILD_opencv_flann=ON \
-D BUILD_opencv_highgui=ON \
-D BUILD_opencv_imgcodecs=ON \
-D BUILD_opencv_imgproc=ON \
-D BUILD_opencv_java=OFF \
-D BUILD_opencv_ml=ON \
-D BUILD_opencv_objdetect=ON \
-D BUILD_opencv_photo=ON \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_python3=ON \
-D BUILD_opencv_shape=ON \
-D BUILD_opencv_stitching=ON \
-D BUILD_opencv_superres=ON \
-D BUILD_opencv_ts=ON \
-D BUILD_opencv_video=ON \
-D BUILD_opencv_videoio=ON \
-D BUILD_opencv_videostab=ON \
-D BUILD_opencv_viz=OFF \
-D BUILD_opencv_world=OFF \
-D CMAKE_BUILD_TYPE=RELEASE \
-D WITH_1394=ON \
-D WITH_CUBLAS=OFF \
-D WITH_CUDA=OFF \
-D WITH_CUFFT=OFF \
-D WITH_EIGEN=ON \
-D WITH_FFMPEG=OFF \
-D WITH_GDAL=OFF \
-D WITH_GPHOTO2=OFF \
-D WITH_GIGEAPI=ON \
-D WITH_GSTREAMER=ON \
-D WITH_GTK=ON \
-D WITH_INTELPERC=OFF \
-D WITH_IPP=ON \
-D WITH_IPP_A=OFF \
-D WITH_JASPER=OFF \
-D WITH_JPEG=ON \
-D WITH_LIBV4L=OFF \
-D WITH_OPENCL=ON \
-D WITH_OPENCLAMDBLAS=OFF \
-D WITH_OPENCLAMDFFT=OFF \
-D WITH_OPENCL_SVM=OFF \
-D WITH_OPENEXR=OFF \
-D WITH_OPENGL=ON \
-D WITH_OPENMP=OFF \
-D WITH_OPENNI=OFF \
-D WITH_PNG=ON \
-D WITH_PTHREADS_PF=OFF \
-D WITH_PVAPI=ON \
-D WITH_QT=OFF \
-D WITH_TBB=ON \
-D WITH_TIFF=OFF \
-D WITH_UNICAP=OFF \
-D WITH_V4L=OFF \
-D WITH_VTK=OFF \
-D WITH_WEBP=OFF \
-D WITH_XIMEA=OFF \
-D WITH_XINE=OFF \
..
RUN cmake --build . --config Release && \
    make install
RUN cd ~ && rm -rf /tmp/*

ENV LD_LIBRARY_PATH /usr/local/lib:/usr/lib:$LD_LIBRARY_PATH
RUN ldconfig

# ------------------------------------------------------------------------
# Building the Darknet from the source codes.
# ------------------------------------------------------------------------

WORKDIR /root
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR darknet
# Building the darknet as debug mode
RUN cat Makefile | (rm Makefile; sed -e "1 s/GPU=0/GPU=1/g" > Makefile) && \
    cat Makefile | (rm Makefile; sed -e "2 s/CUDNN=0/CUDNN=1/g" > Makefile) && \
    cat Makefile | (rm Makefile; sed -e "3 s/OPENCV=0/OPENCV=1/g" > Makefile) && \
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
