
import pygame as pg
from collections import deque
from collections import namedtuple
from random import randint



pg.init()

Cell = namedtuple( 'Cell', ['x','y'])

def random_cell():
    return Cell(randint(0,19),randint(0,19))

def random_fruit():
    f=random_cell()
    return Cell(f[0]*20,f[1]*20),(400,399)

def prochaine_cell(SNAKE, dir, ):
    return Cell((SNAKE[-1][0]+20*dir[0])%400,(SNAKE[-1][1]+20*dir[1])%400)

def dessiner_rectangle(coord, screen, couleur, width, height):
    rect = pg.Rect(coord[0],coord[1], width, height)
    pg.draw.rect(screen, couleur, rect)




directions=[Cell(0,1),Cell(1,0),Cell(-1,0),Cell(0,-1)]

SNAKE= deque([
    Cell(240,300),
    Cell(260,300),
    Cell(280,300)
])

screen = pg.display.set_mode((400,400))
width = 20 # largeur du rectangle en pixels
height = 20 # hauteur du rectangle en pixels
blanc = (255,255,255)
noir = (0,0,0)
rouge = (255,0,0)
vert=(0,255,0)

for x in range(0,400,20):
    for y in range(0,400,20):
        if abs(x-y)%40==0:
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, blanc, rect)

clock = pg.time.Clock()
fruit, bout = random_fruit()
running=True
dir=(1,0)
score = 0
pg.display.set_caption(f"Score: {score}")


while running:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                dir=directions[1]
            elif event.key == pg.K_s:
                dir=directions[0]
            elif event.key == pg.K_z:
                dir=directions[3]
            elif event.key == pg.K_q:
                dir=directions[2]

    next_cell = prochaine_cell(SNAKE, dir)
    if next_cell in SNAKE:
        running=False
    else:
        SNAKE.append(next_cell)
        if SNAKE[-1]==fruit:
            fruit, bout= random_fruit()
            score+=1
        else:
            bout=SNAKE.popleft()

    if abs(bout[0]-bout[1])%40==0:
        dessiner_rectangle(bout,screen, blanc, width, height)
    else:
        dessiner_rectangle(bout,screen, noir, width, height)
    
    dessiner_rectangle(fruit, screen, vert, width, height)

    for k in SNAKE:
        dessiner_rectangle(k,screen,rouge,width,height) 
    
    pg.display.set_caption(f"Score: {score}")
    pg.display.update()



"""snake.append((snake[-1][0]+20*dir[0],snake[-1][1]+20*dir[1]))
                if snake[-1]==fruit:
                    f=(randint(0,30),randint(0,30))
                    fruit=(f[0]*20,f[1]*20)
                    r=(600,599)
                else:
                    r=snake.pop(0)"""