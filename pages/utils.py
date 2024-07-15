import cv2
import numpy as np
import torch
from ultralytics import YOLO

def load_model(model_path):
    model = YOLO(model_path)
    return model

def get_predictions(model, image):
    results = model(image)
    return results

def draw_boxes(image, results, width=640, height=640):
    boxes = results[0].boxes.xyxy  # Bounding boxes
    confs = results[0].boxes.conf  # Confidence scores
    classes = results[0].boxes.cls  # Class predictions
    count = 0
    for box, conf, cls in zip(boxes, confs, classes):
        x1, y1, x2, y2 = map(int, box)
        if cls == 0: 
            color = (0, 255, 0)   # Green for cars, Red for empty spaces
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            count=count+1
    return image, count