# Pest Sprayer YOLOv8 Project

This project detects pests using a YOLOv8 model and sprays pesticide based on pest density.

## Folder Structure

- `pest_data/`: Contains training and validation images/labels
- `train_model.py`: Trains the YOLOv8 model
- `main.py`: Runs pest detection + spraying
- `arduino_relay.ino`: Arduino sketch for spraying