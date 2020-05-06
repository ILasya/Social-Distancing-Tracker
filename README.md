# Social-Distancing-Tracker

Social distancing is a method of infection prevention implemented to avoid/decrease contact between people so as to stop or slow down 
the rate and extent of disease transmission in a community. Coronavirus is one such disease that can be transmitted from person to person 
if proper Social Distancing is not maintained. According to the government, a minimum of 3 feet distance must be maintained between people.

But, making sure that social distancing is maintained in public places becomes a challenging task. This project helps in tracking if people are maintaining social distance. This AI system tracks and send an alert if someone is not following social distancing.

# YOLO3 - Real-Time Object Detection

You only look once (YOLO) is a state-of-the-art, real-time object detection system.YOLOv3 is extremely fast and accurate. 
YOLOv3 uses a totally different approach. Here, a single neural network is applied to the full image. This network divides the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities.

In our application we are using YOLOv3 for Human Detection.

A detailed explanation of all the steps followed is given as comments in the .py and .ipynb files.

The Pretrained weights and the configuration file for YOLOv3 are provided in the yolo_weights folder in this repository. The folder contains:
1) coco.names 
2) yolov3.cfg
3) yolov3.weights

To download the YOLOv3 files you can use there commands in command line:

pip install wget

wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg

wget https://pjreddie.com/media/files/yolov3.weights

# Libraries used

1) cv2
2) numpy
3) math

# Procedure to use Repository
1) Clone this repository
2) Install all the required libraries
3) run the Run.ipynb file in Jupyter Notebook

# Uploaded Files Information



