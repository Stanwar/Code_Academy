def reverse(text):
    result = ""
    for i in range(1,len(text)+1):
        result = result + (text[len(text)-i])
    print result
    return str(result)
    
reverse('abcd')