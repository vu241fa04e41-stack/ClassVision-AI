from flask import Flask, render_template
from ultralytics import YOLO
import cv2

app = Flask(__name__)

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

student_count = 0

@app.route("/")
def home():

    global student_count

    ret, frame = cap.read()

    if ret:

        results = model(frame)

        student_count = 0

        for result in results:
            for box in result.boxes:

                if int(box.cls[0]) == 0:
                    student_count += 1

    return render_template("dashboard.html",
                           students=student_count)

app.run(debug=True)