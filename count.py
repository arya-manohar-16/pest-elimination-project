def count_pests(detections, class_ids=None):
    if class_ids is None:
        return len(detections)
    return sum(int(det[5] in class_ids) for det in detections)
