# -*- coding: utf-8 -*-
"""Problem_B1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qkpNDvtPnNbEiNy6nWnL2NKtuzNECUOx
"""

!pip install keras_preprocessing --quiet
!pip install numpy==1.24.3 --quiet
!pip install pandas==2.0.3 --quiet
!pip install Pillow==10.0.0 --quiet
!pip install scipy==1.10.1 --quiet
!pip install tensorflow==2.13.0 --quiet
!pip install tensorflow-datasets==4.9.2 --quiet

# =============================================================================
# PROBLEM B1
#
# Given two arrays, train a neural network model to match the X to the Y.
# Predict the model with new values of X [-2.0, 10.0]
# We provide the model prediction, do not change the code.
#
# The test infrastructure expects a trained model that accepts
# an input shape of [1]
# Do not use lambda layers in your model.
#
# Please be aware that this is a linear model.
# We will test your model with values in a range as defined in the array to make sure your model is linear.
#
# Desired loss (MSE) < 1e-3
# =============================================================================

import numpy as np
import tensorflow as tf
from tensorflow import keras

# class myCallback(tf.keras.callbacks.Callback):
#     def on_epoch_end(self, epoch, logs={}):
#         if(logs.get('loss')<1e-3):
#             print("Training has stopped because the loss (MSE) has reachable!")
#             self.model.stop_training = True

def solution_B1():
    # DO NOT CHANGE THIS CODE
    X = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], dtype=float)
    Y = np.array([5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0], dtype=float)

    # YOUR CODE HERE
    # Define the model
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

    # Compile the model with a smaller learning rate
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01), loss='mean_squared_error')

    # Train the model with more epochs
    model.fit(X, Y, epochs=10050, verbose=0)

    print(model.predict([-2.0, 10.0]))
    return model

# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_B1()
    model.save("model_B1.h5")

# You can also use this cell as a shortcut for downloading your model
from google.colab import files
files.download("model_B1.h5")