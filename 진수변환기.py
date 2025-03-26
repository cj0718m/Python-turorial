su=int(input("입력한 진수 결정(2/8/10/16) : "))
num = input("값 입력 : ")   

if su == 2:
    num10 = int(num, 2)
if su == 8:
    num10 = int(num, 8)
if su == 10:
    num10 = int(num, 10)
if su == 16:
    num10 = int(num, 16)    
    
print("2진수 ==> ", bin(num10))
print("8진수 ==> ", oct(num10))  
print("10진수 ==> ", num10)
print("16진수 ==> ", hex(num10))