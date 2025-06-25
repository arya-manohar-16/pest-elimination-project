from ultralytics import YOLO

# Load your trained model
model = YOLO("model.pt")  # Replace with actual path to your .pt file

def get_detections_from_frame(frame):
    results = model(frame)
    return results[0].boxes.data.cpu().numpy()  # x1, y1, x2, y2, conf, class_id
