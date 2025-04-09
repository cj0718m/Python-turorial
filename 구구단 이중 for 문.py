i,k,gugudan = 0,0,""



for i in range(2,10):
    gugudan = gugudan +("# %d단 #" % i)
    
print(gugudan)

for i in range(1,10):
    gugudan = ""
    for k in range(2,10):
        gugudan = gugudan +str("%2dX %2d=%2d" % (k,i,k*i))
    print(gugudan)