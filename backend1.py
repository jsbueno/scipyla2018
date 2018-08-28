from pathlib import Path

import pygame
import pandas as pd

import data_plot


SIZE = WIDTH, HEIGHT = 800,800

DATA_FILE = Path("SDSS_stars.csv")

def init():
    global screen
    screen = pygame.display.set_mode(SIZE)

def plt_func(x, y, color=(255, 255, 255)):
    screen.set_at((int(x), HEIGHT - int(y)), color)

def main():
    data = pd.read_csv(DATA_FILE)
    data_plot.scatter(plt_func, SIZE, data['z_mag'], data['i_mag'])
    pygame.display.flip()

    input()


if __name__ == "__main__":
    try:
        init()
        main()
    finally:
        pygame.quit()
