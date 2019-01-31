import  pygame
import time
from random import*
from tkinter import*


blue = (113,177,227) #valeur max =255.
white = (255,255,255)
black = (0,0,0)
pygame.init()

surfaceW = 500
surfaceH = 500
pacW = 15
pacH = 15


surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()


img = pygame.image.load('pac.gif')



def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYUP:
            continue
        return event.key

    return  None

def creaTexteObjs (texte, font):
    texteSurface = font.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()


    main()

def gameOver():
    msgSurface("Boom!")

def pac(x,y, image):
    surface.blit(image, (x,y))

def main():
    x=250
    y=250
    y_move=0


    score_actuel = 0

    game_over = False

    while not game_over:

        surface.fill(black)
        pac(x,y,img)


      
        pygame.display.update()



main()
pygame.quit()
quit()

