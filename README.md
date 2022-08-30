# Attendance-Using-Facial-Recognition
This is an Artificial Intelligence - Machine Learning Project "Attendance using Facial-Recognition"

# Benifits - 
As we all know that many Machine-Learnig based project reqiures altest 2-3 similar kind of images to train & ofcourse a lot of time to train all the things BUT here it requires just one good* image of the person and thats all needed for recognition. 

This itself updates attendance of the person recognized.

This model can't be fooled using any fake image or a photo of the respective person, attendance will only be counted for a real face.

Emotions can be detected using this model (This feature is optional as the main purpose of this model is attendance).

Gender can be classified (Male/Female) (This feature is optional as the main purpose of this model is attendance).


# This Project Uses:-
Language --> Python=3.8 
System --> Nvidia Jetson-nano
Operating System --> Ubuntu
CSI-Camera (USB Camera is also Perfect)


# Prerequisite Libraries

1. face_recognition
install using - pip install face_recognition
import using - import face_recognition

2. cv2
install using - pip install opencv-python
import using - import cv2

3. os
install using - "Usually Preinstalled"
import using - import os

4. pandas
install using - pip install pandas
import using - import pandas as pd

5. datetime
install using - pip install datetime
import using - from datetime import datetime

6. tkinter
install using - pip install tinkter
import using - from tkinter import *

7. tesorflow 2.0 (If GPU is used Verson of CUDA can create exceptions, so try to install the same version on tensorflow_gpu)
 install using - pip install tensorflow (For GPU users use - pip install tensorflow_gpu
 import using - import tensorflow as tf
