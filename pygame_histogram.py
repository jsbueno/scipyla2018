import csv
import os
from pathlib import Path

import pygame
import data_plot


SIZE=800,600
FILENAME = 'candidatos.csv'

MARGIN = 0.3
BAR_SPACING = 0.2
LABEL_MARGIN = 4

color = (64, 128, 255)
end_color = (0, 64, 64)
border_color = (0, 0, 128)
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


def load_photo(name, width):
    name = name.lower().replace(' ', '_')
    path = Path('resources') / f'{name}.jpg'
    print(path)
    if not os.path.exists(path):
        return None
    img = pygame.image.load(str(path))
    img = pygame.transform.rotozoom(img, 0, width/img.get_width())
    return img


def render_label(label, angle=0):
    img = font.render(label, True, label_color)
    if angle:
        img = pygame.transform.rotozoom(img, angle, 1)
    return img


def fancy_rect(rect):
    color_steps = tuple((end_comp - comp) / rect.width for comp, end_comp in zip(color, end_color))
    advance_color = lambda color: tuple(comp + step_comp for comp, step_comp in zip(color, color_steps))
    color_fix = lambda color: tuple(int(comp) for comp in color)

    tmp_color = color

    for x in range(rect.left, rect.right):
        pygame.draw.rect(screen, color_fix(tmp_color), (x, rect.top, 1, rect.height))
        tmp_color = advance_color(tmp_color)
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

    photo_label = load_photo(label_x, rect.width)
    if photo_label:
        screen.blit(photo_label, (rect.left, rect.bottom + LABEL_MARGIN))


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
