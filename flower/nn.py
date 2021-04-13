import numpy as nu
import tensorflow as tf
import os
import PIL
import PIL.Image
import tensorflow_datasets as tfds
import pathlib

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='flower_photos',
                                   untar=True)
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))

roses = list(data_dir.glob('roses'))

PIL.Image.open(str(roses[0]))
