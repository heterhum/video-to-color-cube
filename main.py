import time
from mp4toimg import video_to_frames
from colorliste import colorliste
import os
import pygame
import random as rd

video="C:/Users/xoxar/Downloads/bad_apple.mp4" #path to your mp4
path_to_folder='video-to-color-cube/imgfolder'
wanted_fps=15
extention=".jpeg" 
longueur=720
hauteur=500
STEP=3
ftime=True
it=0

def dessin(liste): 
    for i in liste:
        pygame.draw.rect(screen,(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)),pygame.Rect(i[0]*STEP, i[1]*STEP, STEP, STEP))
def colorlistefirst():
    for i in range(hauteur): 
        for e in range(longueur):
            x = e * STEP
            y = i * STEP
            pygame.draw.rect(screen,(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)),pygame.Rect(x, y, STEP, STEP))

#video_to_frames(video, path_to_folder, wanted_fps, extention)

y=colorliste(extention,longueur,hauteur,path_to_folder)


screen = pygame.display.set_mode((longueur*STEP, hauteur*STEP))
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    if ftime:
        colorlistefirst()
        ftime=False

    dessin(y[it])
    it+=1
    pygame.time.wait(66)
    pygame.display.update()
quit()

