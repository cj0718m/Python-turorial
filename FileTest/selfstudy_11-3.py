inFp = None
fName,inList,inStr = "",[],""

fName = input("읽을 파일 이름을 입력하시오: ")
inFp = open(fName, "r")

outFp = None
outStr = "" 

outFp = open(fName, "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break
    
outFp.close()
print("파일에 저장되었습니다.")