from ultralytics import YOLO
import multiprocessing
from multiprocessing import freeze_support

model = YOLO("D:/Codes/YOLO-E-waste-Classifier-and-detector/runs/detect/train3/weights/last.pt")  

def train():

    results = model.train(resume=True)
    return "Model Trained Successfully" , results

if __name__ == "__main__":
    freeze_support()
    train() 