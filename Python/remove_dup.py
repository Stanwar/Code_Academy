def remove_duplicates(integers):
    result = []
    for i in integers:
        
        if i in result:
            print "duplicate"
        else :
            result.append(i)
    return result