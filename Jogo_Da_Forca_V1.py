palavras=open('entrada.txt','r+',encoding='utf-8')
import turtle



forca = turtle.Screen()
forca.screensize(canvwidth=800,canvheight=600,bg='orange')
forca.title("Jogo Da Forca")

lapis= turtle.Turtle()           #Desenha a forca
lapis.speed(8)
lapis.penup()
lapis.setpos(-300,-200)
lapis.pendown()
lapis.color("darkblue")
lapis.width(width=4)

lapis.backward(150)
lapis.right(90)
lapis.forward(50)
lapis.left(90)
lapis.forward(150)
lapis.left(90)
lapis.forward(50)
lapis.penup()

lapis.setpos(-400,-200)
lapis.pendown()
lapis.forward(500)
lapis.right(90)
lapis.forward(200)
lapis.right(90)
lapis.forward(100)
lapis.penup()
lapis.setheading(270)
lapis.setpos(0,399)

def cabeca():                  #Desenha a cabeça
    lapis.setpos(-200,200)    
    lapis.width(width=2)
    lapis.pendown()
    lapis.color('darkred')
    lapis.speed(11)
    lapis.right(90)
    lapis.circle(30)
    lapis.penup()
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def tronco():                 #Desenha o tronco
    lapis.setpos(-200,140)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.forward(120)
    lapis.penup()
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def braco1():                 #Desenha o braço direito
    lapis.setpos(-200,130)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.right(35)
    lapis.forward(50)
    lapis.left(35)
    lapis.forward(40)
    lapis.penup()
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def braco2():                  #Desenha o braço esquerdo
    lapis.setpos(-200,130)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.left(35)
    lapis.forward(50)
    lapis.right(35)
    lapis.forward(40)
    lapis.penup()
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def perna1():                 #Desenha a perna direita 
    lapis.setpos(-200,20)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.right(20)
    lapis.forward(100)
    lapis.penup()
    lapis.left(20)
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def perna2():              #Desenha a perna esquerda  
    lapis.setpos(-200,20)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.left(20)
    lapis.forward(100)
    lapis.penup()
    lapis.right(20)
    lapis.setheading(270)
    lapis.setpos(0,399)
    
def rosto():                 #Dsenha o rosto
    lapis.setpos(-205,182)
    lapis.width(width=2)
    lapis.color('darkred')
    lapis.pendown()
    lapis.right(45)
    lapis.forward(15)
    lapis.penup()
    lapis.setpos(-215,182)
    lapis.pendown()
    lapis.left(90)
    lapis.forward(15)
    lapis.penup()
    lapis.setpos(-195,182)
    lapis.pendown()
    lapis.forward(15)
    lapis.penup()
    lapis.setpos(-185,182)
    lapis.pendown()
    lapis.right(90)
    lapis.forward(15)
    lapis.penup()
    lapis.setpos(-190,150)
    lapis.pendown()
    lapis.setheading(90)
    lapis.circle(10,180)
    lapis.penup()
    lapis.setheading(270)
    lapis.setpos(0,399)

def lacunas(numero_de_palavras,numero_de_letras):
    b=0
    lapis.setpos(-300,-120)
    lapis.width(3)
    lapis.color('black')
    lapis.left(90)
    while(b<numero_de_palavras):
        c=0
        while(c<numero_de_letras):
            lapis.pendown()
            lapis.forward(20)
            lapis.penup()
            lapis.forward(15) 
            c=c+1
        lapis.forward(20)
        b=b+1
        numero_de_letras=
        


letra_inserida=forca.textinput('Letra','Insira uma letra:')
forca.exitonclick()
palavras.close