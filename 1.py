from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")
camera = cv2.VideoCapture(0)

while True:

    ok, frame = camera.read()

    if not ok:
        break

    results = model(frame)

    for result in results:

        for box in result.boxes:

            if int(box.cls[0]) == 0:   # Person

                x1, y1, x2, y2 = map(int, box.xy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                cv2.putText(frame,"Person",(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,(0,255,0),2)

    cv2.imshow("Person Detection",frame)

    if cv2.waitKey(1)==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()