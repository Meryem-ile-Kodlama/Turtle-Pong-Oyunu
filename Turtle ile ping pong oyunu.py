import turtle

# OYUN PENCERESİ
pencere = turtle.Screen()
pencere.setup(width=800, height=600)
pencere.title("Ping Pong Oyunu :)")
pencere.bgcolor("Black")
pencere.tracer(0)

# RAKET 1
raket1 = turtle.Turtle()
raket1.speed(0)
raket1.color("White")
raket1.shape("square")
raket1.shapesize(stretch_wid= 5, stretch_len=1)
raket1.penup()
raket1.goto(-350,0)

# RAKET 2
raket2 = turtle.Turtle()
raket2.speed(0)
raket2.color("White")
raket2.shape("square")
raket2.shapesize(stretch_wid= 5, stretch_len=1)
raket2.penup()
raket2.goto(350,0)

# TOP
top = turtle.Turtle()
top.speed(0)
top.color("White")
top.shape("square")
top.penup()
top.goto(0,0)
top.changex = 0.1
top.changey = 0.1

# SKOR 
skor1 = 0
skor2 = 0

# YAZILAR
yazi = turtle.Turtle()
yazi.speed(0)
yazi.color("White")
yazi.penup()
yazi.hideturtle()
yazi.goto(0,260)
yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal"))

# FONKSİYONLAR
def raket1_yukari():
    y = raket1.ycor()
    y += 20
    raket1.sety(y)

def raket1_asagi():
    y = raket1.ycor()
    y -= 20
    raket1.sety(y)

def raket2_yukari():
    y = raket2.ycor()
    y += 20
    raket2.sety(y)

def raket2_asagi():
    y = raket2.ycor()
    y -= 20
    raket2.sety(y)

# KLAVYE
pencere.listen()
pencere.onkeypress(raket1_yukari, "w")
pencere.onkeypress(raket1_asagi, "s")
pencere.onkeypress(raket1_yukari, "W")
pencere.onkeypress(raket1_asagi, "S")
pencere.onkeypress(raket2_yukari, "Up")
pencere.onkeypress(raket2_asagi, "Down")

# OYUN DÖNGÜSÜ
while True:
    try:
        pencere.update()

        # TOPU HAREKET ETTİRME
        top.setx(top.xcor() + top.changex)
        top.sety(top.ycor() + top.changey)

        # TOP KENARA DEĞERSE 
        if top.ycor() > 290:
            top.sety(290)
            top.changey *= -1
        if top.ycor() < -290:
            top.sety(-290)
            top.changey *= -1
        if top.xcor() > 390:
            top.goto(0,0)
            top.changex *= -1
            skor1 += 1
            yazi.clear()
            yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal"))
        if top.xcor() < -390:
            top.goto(0,0)
            top.changex *= -1
            skor2 += 1
            yazi.clear()
            yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal"))

        # RAKET VE TOP ETKİLEŞİMİ 
        if (top.xcor() > 330) and (top.ycor() < raket2.ycor() + 50 and top.ycor() > raket2.ycor() - 50):
            top.changex *= -1
        if (top.xcor() < -330) and (top.ycor() < raket1.ycor() + 50 and top.ycor() > raket1.ycor() - 50):
            top.changex *= -1
    except:
        break