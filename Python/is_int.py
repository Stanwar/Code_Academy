import math

def is_int(x):
    if x > 0 : 
        if ( math.ceil(x) - x) != 0:
            return False
        else : 
            return True
    elif x < 0 : 
        if (x -  math.ceil(x)) != 0 : 
            return False
        else : 
            return True
    else:
        return True
        