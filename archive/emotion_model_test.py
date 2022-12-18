#!/usr/bin/env python
# coding: utf-8

# Prepare the image:

# In[1]:


#!python -V


# In[2]:


#!pip install tensorflow


# In[3]:


import tensorflow as tf
from tensorflow import _keras
tf.__version__


# In[4]:


#!pip install keras_image_helper


# In[5]:


from keras_image_helper import create_preprocessor


# https://i.pinimg.com/originals/6a/ef/bb/6aefbbc556900e05a336d8a616a310d6.jpg:
# 
# <img src="https://i.pinimg.com/originals/6a/ef/bb/6aefbbc556900e05a336d8a616a310d6.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" style="max-height: 300px" />

# In[7]:


preprocessor = create_preprocessor('xception', target_size=(150, 150))


# In[8]:


image_url = 'https://i.pinimg.com/originals/6a/ef/bb/6aefbbc556900e05a336d8a616a310d6.jpg'
X = preprocessor.from_url(image_url)


# X.shape

# Load the TF-lite model

# In[9]:


#!pip install tflite_runtime


# In[10]:


# import tensorflow.lite as tflite # this also works locally, but it won't work in Lambda
import tflite_runtime.interpreter as tflite


# In[11]:


interpreter = tflite.Interpreter(model_path='emotion-model.tflite')
interpreter.allocate_tensors()


# Get the input and the output to the model. We'll need them for putting in the array (input) and getting out the prediction (output):

# In[12]:


input_details = interpreter.get_input_details()
input_index = input_details[0]['index']

output_details = interpreter.get_output_details()
output_index = output_details[0]['index']


# Let's make the predictions:

# In[13]:


interpreter.set_tensor(input_index, X)
interpreter.invoke()

preds = interpreter.get_tensor(output_index)


# The `preds` array contains the predictions:

# In[14]:


preds


# Let's convert these raw predictions to something more readable:

# In[15]:


labels = [
    'anger',
    'contempt',
    'disgust',
    'fear',
    'happiness',
    'neutrality',
    'sadness',
    'surprise'
]


# In[16]:


results = dict(zip(labels, preds[0]))
results


# In[ ]:





# In[ ]:




