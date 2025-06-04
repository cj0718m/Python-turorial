inFp = None
inStr = ""
lineNum = 1  

inFp = open("C:\\Users\\cj071\\OneDrive\\바탕 화면\\파이썬실습\\Python-turorial\\FileTest\\cookbook.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="") 
    lineNum += 1  

inFp.close()