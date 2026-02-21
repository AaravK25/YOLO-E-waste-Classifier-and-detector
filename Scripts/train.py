from ultralytics import YOLO
import multiprocessing
from multiprocessing import freeze_support

model = YOLO("yolo26n.pt")  

def train():

    results = model.train(data="D:/Datasets/E-waste-Detect-modified-yolo26/data.yaml", epochs=100, imgsz=512, device='cuda')
    return "Model Trained Successfully" , results

if __name__ == "__main__":
    freeze_support()
    train() 