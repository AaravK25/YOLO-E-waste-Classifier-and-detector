from ultralytics import YOLO
import torch

model = YOLO("yolo26n.pt")  

results = model.train(data="D:/Datasets/E-waste-Detect-modified-yolo26/data.yaml", epochs=100, imgsz=512, device='cuda')