import tensorflow as tf
import config as cfg
import data_prep as dp


def run(im, save_path):
    model = tf.keras.models.load_model(cfg.MODEL_PATH)
    im = dp.prepare_image(im)
    res = model(im)
    dp.save_separated(res, save_path)
