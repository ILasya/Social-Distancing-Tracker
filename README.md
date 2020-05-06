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
1) Run.ipynb - This is the main file that you must run to get the output

2) videos - This folder contains the input video that has to be processed. This video is called to the Run.ipynb file

3) distance_Estimation.py - This file contains the function distance() that determines the distance between two humans in a frame                                   (Distance between centres of two bounding boxes) This file is imported to the Distance_Detection.py file.

4) Object_Detection.py - This file contains the object_detection() function that takes Output Layers of the YOLO network as one of its                            parameters and performs YOLO Object detection over each frame to identify if the frame contains humans and                              marks each human with a bounding box. This file is called to the Run.ipynb file. 
5) Distance_Detection.py - This file contains the distance_detection() function that takes the bounding boxes as one of its parameters                              and identifies if two bounding boxes are maintaining distance or if they are close to each other. The                                    function returns the value of number of humans maintaining social distance and number of people who are at a                            risk of getting Coronavirus due to close contact with the other person. This file is imported to the                                    Run.ipynb file.

6) coco.names - This file contains the labels of the various objects in the COCO dataset. This file is called by the Run.ipynb for YOLO                 object detection

7) yolov3.cfg - This is the configuration file for YOLOv3 Object detection model.

8) yolov3.weights - (NOT INCLUDED IN THIS REPOSITORY) This file has to be downloaded in order to run YOLO object detection. The                             procedure for the download is explained YOLO3 - Real-Time Object Detection section.

9) outputClip1.mp4 - This is the processed video and the output of the Application. Please view this video to get a better idea of how                        Social-Distancing-Tracker works



