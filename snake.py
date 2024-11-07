
import pygame as pg

"""
le snake - v0
on repeint l'écran à une période de 1 seconde
et on a du mal à sortir du programme



# les imports standard en premier
from random import randint

import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))

# on crée aussi un objet "horloge"
clock = pg.time.Clock()

# enfin on boucle à l'infini pour faire le rendu de chaque image
while True:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(1)

    # il faut traiter les événements a minima
    # pour que la fenêtre s'affiche
    for event in pg.event.get():
        pass

    # on génère une couleur (Rouge, Vert, Bleu) au hasard
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # et on colorie l'écran avec cette couleur
    screen.fill(random_color)

    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()
"""



"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

"""from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 300))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
"""


from random import randint
pg.init()


def random_cell():
    return (randint(0,19),randint(0,19))



directions=[(0,1),(1,0),(-1,0),(0,-1)]
SNAKE=[
    (240,300),
    (260,300),
    (280,300)
]

screen = pg.display.set_mode((400,400))
width = 20 # largeur du rectangle en pixels
height = 20 # hauteur du rectangle en pixels
color = (255,255,255)
for x in range(0,400,20):
    for y in range(0,400,20):
        if abs(x-y)%40==0:
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)

clock = pg.time.Clock()
r=400,399
f=(randint(0,19),randint(0,19))
fruit=(f[0]*20,f[1]*20)
running=True
dir=(1,0)
score = 0
pg.display.set_caption(f"Score: {score}")


while running:
    clock.tick(10)
    rouge = (255,0,0)
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


    if ((SNAKE[-1][0]+20*dir[0])%400,(SNAKE[-1][1]+20*dir[1])%400) in SNAKE:
        running=False
    else:
        SNAKE.append(((SNAKE[-1][0]+20*dir[0])%400,(SNAKE[-1][1]+20*dir[1])%400))
        if SNAKE[-1]==fruit:
            f=random_cell()
            fruit=(f[0]*20,f[1]*20)
            r=(400,399)
            score+=1
        else:
            r=SNAKE.pop(0)



    rect = pg.Rect(r[0]%400,r[1]%400, width, height)
    if abs(r[0]-r[1])%40==0:
        pg.draw.rect(screen, (255,255,255), rect)
    else:
        pg.draw.rect(screen, (0,0,0), rect)
    rect = pg.Rect(fruit[0],fruit[1], width, height)
    pg.draw.rect(screen, (0,255,0), rect)
    for k in SNAKE:
        rect = pg.Rect(k[0]%400,k[1]%400, width, height)
        pg.draw.rect(screen, rouge, rect)
    pg.display.set_caption(f"Score: {score}")
    pg.display.update()



"""snake.append((snake[-1][0]+20*dir[0],snake[-1][1]+20*dir[1]))
                if snake[-1]==fruit:
                    f=(randint(0,30),randint(0,30))
                    fruit=(f[0]*20,f[1]*20)
                    r=(600,599)
                else:
                    r=snake.pop(0)"""