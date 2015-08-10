import re

def censor(text,word):
    tee = re.split(' ',text)
    print tee
    print len(str(tee))
    sent = []
    asterix = ""
    for i in tee:
        asterix = ""
        if i == word:
            asterix =  "*" * len(i)
            sent.append(asterix)
        else :
            sent.append(i)
    return " ".join(sent)
