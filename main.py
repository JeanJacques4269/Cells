from constants import *
from game import Game

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Cell simulation")
    print(WIDTH, HEIGHT)
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(win)
    game.run()