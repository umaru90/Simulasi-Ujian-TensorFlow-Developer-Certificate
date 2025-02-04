# -*- coding: utf-8 -*-
"""Problem_A2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fX8h07IDFlzRQfz4P0wNga1S2lPlAGbT
"""

!pip install keras_preprocessing --quiet
!pip install numpy==1.24.3 --quiet
!pip install pandas==2.0.3 --quiet
!pip install Pillow==10.0.0 --quiet
!pip install scipy==1.10.1 --quiet
!pip install tensorflow==2.13.0 --quiet
!pip install tensorflow-datasets==4.9.2 --quiet

# =====================================================================================
# PROBLEM A2
#
# Build a Neural Network Model for Horse or Human Dataset.
# The test will expect it to classify binary classes.
# Your input layer should accept 150x150 with 3 bytes color as the input shape.
# Don't use lambda layers in your model.
#
# The dataset used in this problem is created by Laurence Moroney (laurencemoroney.com).
#
# Desired accuracy and validation_accuracy > 83%
# ======================================================================================

import urllib.request
import zipfile
import tensorflow as tf
import os
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop

class MyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('val_accuracy')>0.85):
            print("\nTraining has complete because the accuracy has reacable")
            self.model.stop_training = True

def solution_A2():
    data_url_1 = 'https://github.com/dicodingacademy/assets/releases/download/release-horse-or-human/horse-or-human.zip'
    urllib.request.urlretrieve(data_url_1, 'horse-or-human.zip')
    local_file = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/horse-or-human')

    data_url_2 = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/validation-horse-or-human.zip'
    urllib.request.urlretrieve(data_url_2, 'validation-horse-or-human.zip')
    local_file = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/validation-horse-or-human')
    zip_ref.close()


    TRAINING_DIR = 'data/horse-or-human'
    VALIDATION_DIR = 'data/validation-horse-or-human'
    train_datagen = ImageDataGenerator(
        # YOUR CODE HERE
        rescale=1./255)

    # YOUR IMAGE SIZE SHOULD BE 150x150
    train_generator = train_datagen.flow_from_directory( # YOUR CODE HERE
        TRAINING_DIR,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

    validation_datagen = ImageDataGenerator(rescale=1./255)
    validation_generator = validation_datagen.flow_from_directory(
        VALIDATION_DIR,
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

    model = tf.keras.models.Sequential([
        # YOUR CODE HERE, end with a Neuron Dense, activated by sigmoid
        tf.keras.layers.Conv2D(8, (3,3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile and train the model
    callback = MyCallback()  # Initialize the custom callback
    model.compile(optimizer=RMSprop(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(train_generator, validation_data=validation_generator, epochs=20, verbose=2, callbacks=callback)

    return model

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    model = solution_A2()
    model.save("model_A2.h5")

import tensorflow as tf

# Check if you have the correct Tensorflow version
assert tf.__version__ == '2.13.0', f'You have TF{tf.__version__}. Please install the grader-compatible Tensorflow and select Runtime > Restart Session'

# Load the model you saved earlier
model = tf.keras.models.load_model("model_A2.h5", compile=False)

# Save the model with the compatible TF version
model.save("final_model_A2.h5")

# You can also use this cell as a shortcut for downloading your model
from google.colab import files
files.download("final_model_A2.h5")