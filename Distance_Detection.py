from distance_Estimation import distance
import cv2
def distance_detection(ids,boxes):
    state = []
    center = []
    closep=[]
    x=[]
    y=[]
    if len(ids)>0:
        flt=ids.flatten()
        for i in flt:
            
            #Getting the coordinames of the boxes
            left=boxes[i][0]
            top=boxes[i][1]
            width=boxes[i][2]
            height=boxes[i][3]
            
            #Identifying the centre of the box
            c = [int(left + width / 2), int(top + height / 2)]
            
            #Cetre of each box
            center.append(c)
            
            #dimentions of each box
            x.append(width)
            y.append(height)
            state.append(0)
            
        for i in range(len(center)):
            for j in range(len(center)):
                
                #Calling the distance() function from Distance_Detection.py file
                cls = distance(x[i],y[i],center[i],x[j],y[j],center[j])
                
                #If two neighboring boxes are at close distance, change state to 1 
                #i,e. ALERT!! People are not maintaining social distance
                if cls == True:
                    closep.append([center[i], center[j]])
                    state[i] = 1
                    state[j] = 1
                    
        #store count of number of people not maintaining social distance in alert variable and the numbe of people safe in the safe variable 
        alert = state.count(1)
        safe=state.count(0)
        
        return state,alert,safe
    
    