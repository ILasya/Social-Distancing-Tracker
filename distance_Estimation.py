import math

def distance(w1,h1,c1,w2,h2,c2):
    #Distance between two centres
    dc = ((w1 - w2) ** 2 + (h1 - h2) ** 2) ** 0.5

    #if height of p1< height of p2
    if(h1<h2):
        W,H = w1,h1
    else:
        W,H = w2,h2
    q=0
    try:
        q=(c2[1]-c1[1])/(c2[0]-c1[0])
    except ZeroDivisionError:
        q = 1.633123e+16
    
    # Measure the horizontal and vertical distance 
    horizontal = abs(1/((1+q**2)**0.5))*dc
    vertical = abs(q/((1+q**2)**0.5))*dc
    
    # Caliberating    
    chor = W*1.3
    cver = H*0.4*0.9
    
    if chor > horizontal > 0 and cver > vertical > 0:
        return True
    else:
        return False