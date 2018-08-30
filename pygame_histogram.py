import csv

import pygame
import data_plot


SIZE=800,600
FILENAME = 'candidatos.csv'

MARGIN = 0.3
BAR_SPACING = 0.2


color = (0, 128, 255)

def read():
    with open(FILENAME) as f:
        reader  = csv.reader(f)
        candidates = next(reader)
        with_l = next(reader)
        without_l = next(reader)

    return candidates, with_l, without_l


def init():
    global screen
    screen = pygame.display.set_mode(SIZE)


def main():
    candidates, with_l, without_l = read()
    plot_hist(candidates, with_l)
    input()
    plot_hist(candidates, without_l)
    input()


def plot_hist(raw_labels, raw_data):
    data = []
    labels = []
    for label, raw_point in zip(raw_labels, raw_data):
        # Skip lael with empty data cell
        if not raw_point.strip():
            continue
        labels.append(label)
        data.append(float(raw_point))

    usefull_height = SIZE[1] * (1 - MARGIN)
    scaled_data = list(data_plot.NormalIter(data, usefull_height))
    usefull_width = SIZE[0] * (1 - MARGIN)


    bar_width = usefull_width / len(data)
    bar_net_width = int(bar_width * (1 - BAR_SPACING))

    bar_offset =  (SIZE[0] * MARGIN / 2) + (bar_width * BAR_SPACING / 2)

    base_line = SIZE[1] - (SIZE[1] * MARGIN) / 2

    x = int(bar_offset)

    for point in scaled_data:
        y  = int(base_line - point)
        height = int(point)

        print(x,y, bar_net_width, height)
        pygame.draw.rect(screen, color, (x, y, bar_net_width, height))

        x += int(bar_width)

        pygame.display.flip()
        pygame.time.delay(200)


if __name__ == '__main__':
    try:
        init()
        main()
    finally:
        pygame.quit()
