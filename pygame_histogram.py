import csv
import os

import pygame
import data_plot


SIZE=800,600
FILENAME = 'candidatos.csv'

MARGIN = 0.3
BAR_SPACING = 0.2
LABEL_MARGIN = 4

color = (0, 128, 255)
border_color = (0, 0, 192)
background_color = (255, 255, 255)
label_color = (0, 0, 0)

def read():
    with open(FILENAME) as f:
        reader  = csv.reader(f)
        candidates = next(reader)
        with_l = next(reader)
        without_l = next(reader)

    return candidates, with_l, without_l


def init():
    global screen, font

    pygame.init()
    flags = 0
    if os.environ.get('FULLSCREEN', False):
        flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode(SIZE, flags)

    font = pygame.font.SysFont('Sans', 16, bold=True)
    clear_screen()


def wait_click():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.time.delay(50)


def clear_screen():
    screen.fill(background_color)
    pygame.display.flip()


def main():
    candidates, with_l, without_l = read()
    plot_hist(candidates, with_l)
    wait_click()
    clear_screen()
    plot_hist(candidates, without_l)
    wait_click()


def clean_data(raw_labels, raw_data):
    data = []
    labels = []
    for label, raw_point in zip(raw_labels, raw_data):
        # Skip lael with empty data cell
        if not raw_point.strip():
            continue
        labels.append(label)
        data.append(float(raw_point))

    usefull_height = SIZE[1] * (1 - MARGIN)
    scaled_data = list(data_plot.NormalIter(data, usefull_height, normalize_min=False))

    return labels, data, scaled_data

def render_label(label, angle=0):
    img = font.render(label, True, label_color)
    if angle:
        img = pygame.transform.rotozoom(img, angle, 1)
    return img


def fancy_rect(rect):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, border_color, rect, 3)


def draw_bar(label_x, label_y, rect):

    rect = pygame.Rect(rect)

    fancy_rect(rect)

    img_label = render_label(label_x, 45)
    screen.blit(img_label, (rect.left, rect.top - img_label.get_height() - LABEL_MARGIN))

    img_label = render_label(f'{int(label_y)}%')

    x = rect.left + (rect.width - img_label.get_width()) // 2
    y = rect.top + LABEL_MARGIN
    screen.blit(img_label, (x, y))



def plot_hist(raw_labels, raw_data):

    labels, data, scaled_data = clean_data(raw_labels, raw_data)

    usefull_width = SIZE[0] * (1 - MARGIN)
    bar_width = usefull_width / len(data)
    bar_net_width = int(bar_width * (1 - BAR_SPACING))

    bar_offset =  (SIZE[0] * MARGIN / 2) + (bar_width * BAR_SPACING / 2)

    base_line = SIZE[1] - (SIZE[1] * MARGIN) / 2

    x = int(bar_offset)

    for label_x, label_y, point in zip(labels, data, scaled_data):
        y  = int(base_line - point)
        height = int(point)

        draw_bar(label_x, label_y, (x, y, bar_net_width, height))

        x += int(bar_width)

        pygame.display.flip()
        pygame.time.delay(200)


if __name__ == '__main__':
    try:
        init()
        main()
    finally:
        pygame.quit()
