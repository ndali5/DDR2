import pygame
import core
from jeu.fleche import Fleches


def setup ():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1590, 830]

    global fleches
    fleches=Fleches()

def run ():
    fleches.afficher(core)

if __name__ == '__main__':
    core.main(setup,run)

