import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Student Detection", annotated)

    if cv2.waitKey(1) == 27:
        break
camera.release()
cv2.destroyAllWindows()