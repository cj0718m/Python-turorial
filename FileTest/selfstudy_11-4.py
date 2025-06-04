inFp,outFp = None, None 
inStr,fName,fName2 = "","",""

fName = input("소스 파일명을 입력하세요: ")
fName2 = input("타깃 파일명을 입력하세요: ")
inFp = open(fName, "r")
outFp = open(fName2, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()

print("파일을 복사했습니다.")
