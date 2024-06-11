# -*- coding: utf-8 -*-
"""Problem_B2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13gMSPJr6X_OB-4Wff8o6Olmf9Vfq78Kh
"""

!pip install keras_preprocessing --quiet
!pip install numpy==1.24.3 --quiet
!pip install pandas==2.0.3 --quiet
!pip install Pillow==10.0.0 --quiet
!pip install scipy==1.10.1 --quiet
!pip install tensorflow==2.13.0 --quiet
!pip install tensorflow-datasets==4.9.2 --quiet

# =============================================================================
# PROBLEM B2
#
# Build a classifier for the Fashion MNIST dataset.
# The test will expect it to classify 10 classes.
# The input shape should be 28x28 monochrome. Do not resize the data.
# Your input layer should accept (28, 28) as the input shape.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 83%
# =============================================================================

import tensorflow as tf
import numpy as np

# class myCallback(tf.keras.callbacks.Callback):
#     def on_epoch_end(self, epoch, logs={}):
#         if(logs.get('accuracy')>0.84 and logs.get('val_accuracy')>0.85):
#             print("Training has stopped because the acc and val_acc has reachable!")
#             self.model.stop_training = True

def solution_B2():
    fashion_mnist = tf.keras.datasets.fashion_mnist

    # Load the dataset
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    # Normalize the images to the range [0, 1]
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # Reshape the input to (28, 28, 1)
    x_train = x_train.reshape((-1, 28, 28, 1))
    x_test = x_test.reshape((-1, 28, 28, 1))

    # Define the model
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=10, validation_split=0.2, batch_size=32)

    return model

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_B2()
    model.save("model_B2.h5")

# You can also use this cell as a shortcut for downloading your model
from google.colab import files
files.download("model_B2.h5")