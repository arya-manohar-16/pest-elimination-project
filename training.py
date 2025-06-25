# train_model.py
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Or yolov8s.pt for more accuracy
model.train(data='pest_data/pest.yaml', epochs=50, imgsz=640, batch=16)
