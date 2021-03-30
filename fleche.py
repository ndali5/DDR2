

import pygame
from pygame.math import Vector2, Vector3

class Fleches:
    def __init__ (self):
        self.orientation = 5
        self.nom = ""
        self.taille = Vector2(5, 5)
        self.position = Vector2(10, 15)
        self.couleur = Vector3(255, 255, 0)


    def afficher(self,core):
        pygame.draw.polygon(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)),((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

    def defiler(self):
        pass

    def disparaitre(self):
        pass

    pass

pass
