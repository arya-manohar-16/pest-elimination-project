# main.py

import cv2
import serial
import time
from detect import get_detections_from_frame
from count import count_pests
from density import calculate_density

# Initialize serial connection to Arduino
arduino = serial.Serial('COM3', 9600)  # Update COM port as needed
time.sleep(2)  # Wait for Arduino to initialize

# Parameters
GRID_ROWS = 3
GRID_COLS = 3
ZONE_AREA = 1.0  # in square meters
DENSITY_THRESHOLD = 10  # example threshold

def get_zone(x_center, y_center, frame_width, frame_height):
    zone_width = frame_width // GRID_COLS
    zone_height = frame_height // GRID_ROWS
    col = min(x_center // zone_width, GRID_COLS - 1)
    row = min(y_center // zone_height, GRID_ROWS - 1)
    return int(row), int(col)

cap = cv2.VideoCapture("video.mp4")  # or 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]
    detections = get_detections_from_frame(frame)
    pest_count = count_pests(detections)
    density = calculate_density(pest_count, ZONE_AREA)

    print(f"Total Pests: {pest_count} | Density: {density:.2f} per sq.m.")

    for det in detections:
        x1, y1, x2, y2 = map(int, det[:4])
        x_center = (x1 + x2) // 2
        y_center = (y1 + y2) // 2

        row, col = get_zone(x_center, y_center, frame_width, frame_height)
        command = f"MOVE X{col} Y{row} SPRAY\n"
        print(f"Sending to Arduino: {command.strip()}")
        arduino.write(command.encode())

        # Optional drawing
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Zone: {row},{col}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    cv2.imshow("Pest Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
