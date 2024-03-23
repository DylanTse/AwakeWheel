from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from threading import Thread
import os
import cv2
import base64
import numpy as np
import time
import logging

logging.basicConfig(level=logging.INFO) 

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
con_str = os.getenv("CONN_STRING")
client = MongoClient(con_str)
db = client['MainDB']
collection = db['Pictures']

def open_close_detection(image64):
    # Convert base64 image to numpy array
    img_data = base64.b64decode(image64)
    nparr = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Load pre-trained face and eye cascade classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # For each face, detect eyes and check if they are open or closed
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # If no eyes are detected, return "unknown"
        if len(eyes) == 0:
            return "unknown"
        
        # Check if any eye is closed
        for (ex, ey, ew, eh) in eyes:
            eye_region = roi_gray[ey:ey+eh, ex:ex+ew]
            _, eye_threshold = cv2.threshold(eye_region, 55, 255, cv2.THRESH_BINARY_INV)
            eye_threshold = cv2.erode(eye_threshold, None, iterations=2)
            eye_threshold = cv2.dilate(eye_threshold, None, iterations=4)
            eye_threshold = cv2.medianBlur(eye_threshold, 5)
            eye_height, eye_width = eye_threshold.shape[:2]
            eye_pixels = cv2.countNonZero(eye_threshold)
            if eye_pixels / float(eye_width * eye_height) < 0.25:
                return "closed"
    
    return "open"

def eye_state_detection():
    while True:
        data = [item['base64Image'] for item in collection.find()][0]
        
        # print(data)

        result = open_close_detection(data)
        # print(result)
        logging.info(result) 
        db["EyeState"].insert_one({"image" : data,
                               "eye_state" : result})
        time.sleep(4)

# Define endpoint to serve data
@app.route('/data', methods=['GET'])
def get_data():
    data = [item["base64Image"] for item in db["EyeState"].find({"eye_state": "open"})]
    return data

# Define route for root URL
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Flask app! Visit /data to access the data."

# Run the Flask app
if __name__ == '__main__':
    eye_detection_thread = Thread(target=eye_state_detection)
    eye_detection_thread.daemon = True
    eye_detection_thread.start()
    app.run(debug=True)


