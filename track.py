from ultralytics import YOLO


tracker = YOLO("yolo11n.pt")



def track_people(frame):


    results = tracker.track(

        frame,

        persist=True

    )


    count = 0


    if results[0].boxes.id is not None:

        count = len(
            results[0].boxes.id
        )



    return {

        "tracked_people":count,

        "frame":results[0].plot()

    }