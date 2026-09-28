from ultralytics import YOLO

# Use a larger model (yolo11m.pt or yolo11l.pt) for better precision
model = YOLO("yolo11m.pt")

def detect_objects(frame, conf_threshold=0.5):
    """
    Detects students/persons in a frame with high accuracy settings.
    """
    # conf: confidence threshold, iou: NMS overlap threshold
    results = model(frame, conf=conf_threshold, iou=0.45)

    persons = 0
    objects = []

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            conf = float(box.conf[0])

            objects.append(name)

            # COCO Person class detection
            if name == "person":
                persons += 1

    return {
        "persons": persons,
        "objects": objects,
        "result": results[0].plot()
    }