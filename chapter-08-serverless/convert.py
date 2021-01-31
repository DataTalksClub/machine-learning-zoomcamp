import tensorflow as tf
from tensorflow import keras


model = keras.models.load_model('xception_v4_large_08_0.894.h5')


converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with tf.io.gfile.GFile('clothing-model-v4.tflite', 'wb') as f:
    f.write(tflite_model)
