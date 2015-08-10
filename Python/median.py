def median(integers):
    integers = sorted(integers)
    length = len(integers)
    avg = 0
    
    if length%2==0 :
        
        avg = float((integers[(length/2)-1] + integers[length/2])/2.0)
        print avg
        return avg
    else:
        print integers[length/2]
        return integers[length/2]
        
