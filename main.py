import core
from jeu.fleche import Fleches

fleches = Fleches()
vitesse = 10

def setup ():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [500, 500]

def run ():
    fleches.afficher(core)
    while fleches.position.y < core.WINDOW_SIZE[1]:
        fleches.position.y += vitesse
        print (fleches.position)
    print (core.WINDOW_SIZE[1])

if __name__ == '__main__':
    core.main(setup,run)

