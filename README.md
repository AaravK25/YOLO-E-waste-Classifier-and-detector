This repository is for developing my understanding in the fields of Computer Vision and YOLO models.
Dataset Details:

Dataset Split
Train Set
88%
7644
Images
Valid Set
8%
728
Images
Test Set
4%
364
Images
Preprocessing
Auto-Orient: Applied
Resize: Fill (with center crop) in 512x512
Augmentations
Outputs per training example: 3
Flip: Horizontal, Vertical
Saturation: Between -25% and +25%
Brightness: Between -23% and +23%
Noise: Up to 0.1% of pixels


Ultralytics 8.4.14  Python-3.10.19 torch-2.11.0.dev20260209+cu128 CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
YOLO26n summary (fused): 122 layers, 2,389,850 parameters, 0 gradients, 5.3 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 23/23 4.8it/s 4.8s
                   all        728        728      0.681      0.763      0.752      0.641
  BasePanel_Recyclable          7          7      0.359      0.429      0.512      0.481
  BasePanel_Repairable         10         10        0.7        0.7      0.627      0.627
    BasePanel_Reusable          6          6      0.569      0.833      0.674      0.646
    Battery_Recyclable          5          5      0.792      0.767      0.656      0.584
    Battery_Repairable          9          9      0.576      0.307      0.583      0.515
      Battery_Reusable         15         15      0.599      0.867      0.763      0.673
      Bezel_Recyclable          3          3          1          0      0.345      0.295
      Bezel_Repairable          6          6      0.256        0.5      0.404        0.4
        Bezel_Reusable         15         15      0.655      0.733      0.735      0.735
CMOSBattery_Recyclable         27         27      0.949          1      0.995      0.723
     CPUFan_Recyclable         15         15      0.745      0.781        0.8      0.711
     CPUFan_Repairable         17         17      0.682      0.647      0.711      0.636
       CPUFan_Reusable          1          1      0.195          1      0.995      0.895
    DCCable_Recyclable         10         10      0.556        0.7      0.518      0.393
    DCCable_Repairable         17         17      0.662      0.882      0.861      0.736
      DCCable_Reusable          2          2          1          0      0.092     0.0736
     DVDRom_Recyclable          8          8      0.647          1      0.907       0.87
     DVDRom_Repairable          8          8      0.638        0.5      0.513      0.486
       DVDRom_Reusable          9          9      0.595      0.778      0.623      0.614
HardDiskDrive_Repairable         25         25      0.907       0.96      0.974      0.908
HardDiskDrive_Reusable          2          2      0.294      0.442      0.197      0.197
   HeatSink_Recyclable         26         26      0.925      0.954      0.978       0.87
     HeatSink_Reusable          4          4      0.682       0.75      0.773      0.597
      Hinge_Recyclable          5          5      0.755          1      0.895      0.684
      Hinge_Repairable         15         17      0.753      0.897      0.925      0.653
        Hinge_Reusable          7          7      0.601      0.649      0.659      0.508
   Keyboard_Recyclable          1          1          0          0          0          0
   Keyboard_Repairable         17         17      0.578      0.724      0.637      0.603
     Keyboard_Reusable         16         16      0.665      0.688      0.756      0.706
  LCDScreen_Recyclable          2          2      0.253        0.7      0.662      0.548
  LCDScreen_Repairable         17         17      0.837          1      0.977      0.945
    LCDScreen_Reusable          3          3      0.324      0.667      0.645      0.645
  LVDSCable_Repairable         24         24      0.958      0.955      0.989      0.854
Motherboard_Recyclable         20         20      0.862      0.939      0.953      0.869
Motherboard_Repairable          1          1      0.195          1      0.199      0.179
  Motherboard_Reusable          3          3          1      0.471      0.749      0.749
PowerSwitch_Recyclable          2          2      0.738          1      0.995      0.432
  PowerSwitch_Reusable         25         25      0.865          1      0.995      0.778
  Processor_Repairable         15         15      0.852          1      0.995      0.854
    Processor_Reusable         13         13      0.958          1      0.995      0.834
   RAMCover_Repairable         12         12      0.843      0.898      0.929      0.862
     RAMCover_Reusable         17         17      0.766      0.941      0.948      0.844
        RAM_Repairable          2          2       0.59       0.77      0.828      0.745
          RAM_Reusable         27         27      0.917          1      0.993      0.878
        SSD_Recyclable          8          8      0.859       0.75      0.967      0.894
        SSD_Repairable          1          1       0.58          1      0.995      0.796
          SSD_Reusable         23         23      0.824          1      0.995      0.872
     ScrewKit_Reusable         26         26      0.861      0.962      0.975      0.581
    Speaker_Recyclable          2          2      0.745          1      0.995      0.752
    Speaker_Repairable          4          4      0.342       0.25      0.356      0.297
      Speaker_Reusable         19         19      0.768      0.947      0.888      0.773
   TopPanel_Repairable          8          8      0.507      0.625      0.461      0.448
     TopPanel_Reusable         27         27       0.83      0.704      0.801      0.778
   TouchPad_Recyclable          8          8       0.84          1      0.995      0.837
   TouchPad_Repairable          3          3      0.591      0.333      0.418      0.376
     TouchPad_Reusable         19         19      0.903      0.976        0.9      0.827
    USBPort_Repairable          3          3      0.799          1      0.995      0.664
      USBPort_Reusable         27         27      0.862          1      0.986       0.78
     WebCam_Recyclable          1          1          0          0          0          0
       WebCam_Reusable         28         28      0.906      0.964      0.957      0.712
   WifiCard_Recyclable          7          7      0.787          1      0.995      0.744
     WifiCard_Reusable         21         21      0.936      0.952       0.99      0.761
Speed: 0.3ms preprocess, 2.3ms inference, 0.0ms loss, 0.2ms postprocess per image
