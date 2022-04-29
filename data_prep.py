import tensorflow as tf
import numpy as np
import config as cfg
import cv2


def prepare_image(im: str):
    im = cv2.imread(im)
    im = tf.image.resize(
        im, (cfg.IMAGE_SIZE, cfg.IMAGE_SIZE), method="nearest")
    im = tf.cast(im, tf.float32) / 255.0
    im = tf.expand_dims(im, axis=0)
    return im


def visualize(im):
    pass


def save_separated(im, save_path):
    pass
