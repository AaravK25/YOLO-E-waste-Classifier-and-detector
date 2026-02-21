from ultralytics import YOLO
import cv2 as cv

model = YOLO("runs/detect/train5/weights/best.pt")

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