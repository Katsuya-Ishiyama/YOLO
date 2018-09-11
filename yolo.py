# -*- coding: utf-8 -*-

import keras
from keras.layers import Input, Conv2D, Dense, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.models import Model


def LeakyReLU():
    return keras.layers.LeakyReLU(alpha=0.1)


def build_model(inputs: Input):
    # -----------------------------------------------------
    # Block 1
    # -----------------------------------------------------
    x = Conv2D(kernel_size=(7, 7), filters=64, strides=2, padding='same')(inputs)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = LeakyReLU()(x)

    # -----------------------------------------------------
    # Block 2
    # -----------------------------------------------------
    x = Conv2D(kernal_size=(3, 3), filters=192, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = LeakyReLU()(x)

    # -----------------------------------------------------
    # Block 3
    # -----------------------------------------------------
    x = Conv2D(kernel_size=(1, 1), filters=128, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(1, 1), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = LeakyReLU()(x)

    # -----------------------------------------------------
    # Block 4
    # -----------------------------------------------------
    x = Conv2D(kernel_size=(1, 1), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(1, 1), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(1, 1), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(1, 1), filters=256, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)

    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = LeakyReLU()(x)

    # -----------------------------------------------------
    # Block 5
    # -----------------------------------------------------
    x = Conv2D(kernel_size=(1, 1), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(1, 1), filters=512, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=1, padding='same')(x)
    x = BatchNormalization()(x)

    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=2, padding='same')(x)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)

    # -----------------------------------------------------
    # Block 6
    # -----------------------------------------------------
    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = Conv2D(kernel_size=(3, 3), filters=1024, strides=1, padding='same')(x)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)

    x = Dense(units=4096, activation=LeakyReLU)
    x = Dense(units=7*7*30, activation=LeakyReLU)

