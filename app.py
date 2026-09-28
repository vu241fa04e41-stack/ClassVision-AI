from flask import Flask, render_template, Response, jsonify
from ultralytics import YOLO
import cv2

app = Flask(__name__)

# Use medium model for enhanced accuracy
model = YOLO("yolo11m.pt")

cameras = {}
for i in range(25):
    cameras[i + 1] = cv2.VideoCapture(i)

def generate(camera_id):
    camera = cameras[camera_id]

    while True:
        success, frame = camera.read()
        if not success:
            continue

        # Run inference with higher confidence threshold & non-max suppression
        results = model(frame, conf=0.5, iou=0.45, verbose=False)
        student_count = 0

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                if cls == 0:  # Class 0 = Person
                    student_count += 1

        annotated_frame = results[0].plot()

        cv2.putText(
            annotated_frame,
            f"Students Detected: {student_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        ret, buffer = cv2.imencode(".jpg", annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/video/<int:id>")
def video(id):
    if id not in cameras:
        return "Camera Not Found"
    return Response(
        generate(id),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)