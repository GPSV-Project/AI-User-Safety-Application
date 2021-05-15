# from __future__ import division, print_function
# coding=utf-8
# import sys
# import os
# import glob
# import re
import pandas as pd
from PIL import Image
# import detect_predict
# from shutil import copyfile
import shutil
# from distutils.dir_util import copy_tree
import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
# import cv2
import numpy as np
import tensorflow as tf
# from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.utils import detect_image, Load_Yolo_model
from yolov3.configs import *

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer
import base64
# from image_capture_from_url import get_screen_shot

# from flask_socketio import SocketIO

# from flask_script import Manager
# from flask_bootstrap import Bootstrap


# Define a flask app
app = Flask(__name__)

# app.config.from_object(__name__) # load config from this file , objetc.py

# # Load default config and override config from an environment variable
# app.config.update(dict(
#     # DATABASE=os.path.join(app.root_path, 'flaskr.db'),
#     SECRET_KEY='development key',
#     USERNAME='admin',
#     PASSWORD='default'
# ))
# app.config.from_envvar('OBJECT_SETTINGS', silent=True)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        
        # Read File and file data
        im_data = request.get_data()
        
        with open("capture.jpg", "wb") as im:
            im.write (base64.decodebytes(im_data)) 

        # image_path = file_path
        image_path = 'capture.jpg'

        

        # Model expects a 4 dimensional Tensor that has the layout: [Batch index,Width,Height,Channel]
        # Make prediction
        yolo = Load_Yolo_model()
        image, score, label = detect_image(yolo, image_path, "detect.jpg", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
        label = str(label)
        score = str(score)
        result = str([score,label])
        return result
        
            # detect_predict(data)
        
        # return get_detected_object
        
    return None

# # # Testing to check POSTMAN output cases and frame inputs
# # def predict():
# #     data = request.get_data()
# #     # data = 
# #     # url = data[1]
# #     return data

if __name__ == '__main__':
    
    app.run(debug=False)
    
    # Uncomment below line and comment above line for AWS Usgae

    # app.run(host='0.0.0.0', port=80)