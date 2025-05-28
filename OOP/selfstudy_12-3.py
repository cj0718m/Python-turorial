import threading

class RacingCar : 
    carName = "" 
    def __init__(self, name) :
        self.carName = name
    
    def runCar(self) : 
        print("1+2+3+.....%d=" % int(self.carName), end = "")
        b = 0
        for _ in range(0, int(self.carName) + 1) : 
            b += _
        print("%d" % b)
            
car1 = RacingCar('1000')
car2 = RacingCar('10000')
car3 = RacingCar('100000')

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()