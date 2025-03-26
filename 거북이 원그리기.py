import turtle

swudth,sheight = 500,500

turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width=swudth+50,height=sheight+50)
turtle.screensize(swudth,sheight)
turtle.penup()
turtle.goto(0,-sheight / 2)
turtle.pendown()
turtle.speed(10)

for radius in range(1,250):
    if radius % 6 == 0:
        turtle.color('red') 
    elif radius % 5 == 0:
        turtle.color('orange')
    elif radius % 4 == 0:
        turtle.color('yellow')
    elif radius % 3 == 0:
        turtle.color('green')   
    elif radius % 2 == 0:
        turtle.color('blue')
    elif radius % 1 == 0:
        turtle.color('navyblue')
    else:
        turtle.color('purple')
        
    turtle.circle(radius)
    
turtle.done()