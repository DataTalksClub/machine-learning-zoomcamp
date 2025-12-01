from tensorflow import keras

model = keras.models.load_model('clothing-model-new.keras')
model.export("clothing-model-new_savedmodel")
