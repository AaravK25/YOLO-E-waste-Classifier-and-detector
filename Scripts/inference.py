# from ultralytics import solutions

# inf = solutions.Inference(
#     model="runs/detect/train3/weights/best.pt",  # you can use any model that Ultralytics supports, e.g., YOLO26, or a custom-trained model
# )

# inf.inference()

# # YOU MUST RUN THE FILE using command `streamlit run path/to/file.py`

from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov26n.pt")

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame, imgsz=640, device=0)
    annotated = results[0].plot()
    cv.imshow("Detection", annotated)
    
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()