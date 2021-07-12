import turtle

# Define

# Window
wn = turtle.Screen()
wn.title('Drawing Board by supercoding')

# pen
pen = turtle.Turtle()
pen.pensize(2)





color='black'
#####Functions#####

#####Moving#####
def move_forward():
   pen.forward(5)

def move_backward():
   pen.backward(5)

def move_left():
   pen.left(5)

def left90 ():        
   pen.left(90)       

def right90 ():
   pen.right(90)

def move_right():
   pen.right(5)

#####Other#####

# Eraser
def eraser():
   pen.color('white')
   pen.pensize(5)

# Pen(Back)
def neraser():
   pen.color(color)
   pen.pensize(2)

# Penup
def up():
   pen.penup()

# Pendown
def down():
   pen.pendown()



# Go to (0,0)
def _00():
   pen.penup()
   pen.goto(0,0)
   pen.pendown()

#####Sizes#####
# 1
def size1():
   pen.pensize(2)
# 2
def size2():
   pen.pensize(4)
# 3
def size3():
   pen.pensize(6)
# 4
def size4():
   pen.pensize(8)
# 5
def size5():
   pen.pensize(10)
# 6
def size6():
   pen.pensize(12)
# 7
def size7():
   pen.pensize(14)
# 8
def size8():
   pen.pensize(16)
# 9 
def size9():
   pen.pensize(18)
# 10 
def size10():
   pen.pensize(20)

# Circles
def circle():
   circle=int(input('Name a size: '))
   pen.circle(circle)

# Colors
def color():
   color=input('Name a color: ')
   pen.color(color)

# Background color
def bgcolor():
   bgcolor=input('Name a color: ')
   wn.bgcolor(bgcolor)


# Onkeypress
turtle.listen()
turtle.onkeypress(right90,'r')
turtle.onkeypress(left90,'l')
turtle.onkeypress(move_forward,'Up')
turtle.onkeypress(move_left,'Left')
turtle.onkeypress(move_backward,'Down')
turtle.onkeypress(move_right,'Right')
turtle.onkeypress(_00,'z')
turtle.onkeypress(up,'u')
turtle.onkeypress(down,'d')
turtle.onkeypress(eraser,'e')
turtle.onkeypress(neraser,'E')
turtle.onkeypress(size1,'1')
turtle.onkeypress(size2,'2')
turtle.onkeypress(size3,'3')
turtle.onkeypress(size4,'4')
turtle.onkeypress(size5,'5')
turtle.onkeypress(size6,'6')
turtle.onkeypress(size7,'7')
turtle.onkeypress(size8,'8')
turtle.onkeypress(size9,'9')
turtle.onkeypress(size10,'0')
turtle.onkeypress(color,'c')
turtle.onkeypress(bgcolor,'C')
turtle.onkeypress(circle,'s')


wn.mainloop()