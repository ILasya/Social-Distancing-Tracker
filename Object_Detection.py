import numpy as np
import cv2

def object_detection(Outlayers, labels, frameWidth, frameHeight):
    boxes = []
    conf = []
    IDs = []
    
    #Object detection
    for output in Outlayers:
        for detection in output:
            scores = detection[5:]
            
            #Returns indices of the max element of the array
            ID = np.argmax(scores)
            
            #Assign maximum element in the Scores list into Confidence variable
            confidence = scores[ID]
            
            #If the detected object is a Person,perform the following
            if labels[ID] == "person":

                if confidence > 0.5:
                    
                    #set the boundary for box
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - (width / 2))
                    top = int(center_y - (height / 2))
            
                    #Append the dimensions of the bounding Box
                    boxes.append([left, top, int(width), int(height)])
                    
                    #Append the Confidence value for each object detected
                    conf.append(float(confidence))
                    
                    #Append the maximum score value of each object
                    IDs.append(ID)
                    
    #Perform non maximum suppression with minConfidence = 0.5 and nmsThreshold = 0.5 
    #This method returns all the indicies that correspond to the boxes that have the highest scores and the minimum overlap 
    ids = cv2.dnn.NMSBoxes(boxes, conf, 0.5, 0.5)
    
    return ids,boxes