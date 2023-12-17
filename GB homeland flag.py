import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Размеры флага
flag_width = 600
flag_height = 300

# Цвета флага
white = np.array([255, 255, 255]) / 255
red = np.array([200, 16, 46]) / 255
blue = np.array([1, 33, 105]) / 255

# Функция для вычисления координат конца линии на основе угла и длины
def compute_endpoint(angle_degrees, length):
    angle_radians = angle_degrees * (3.141592653589793 / 180.0)
    x = length * math.cos(angle_radians)
    y = length * math.sin(angle_radians)
    return x, y

def draw_union_jack():
    # Отрисовка синего фона (часть флага Шотландии)
    glBegin(GL_QUADS)
    glColor3fv(white)
    glVertex2fv((0, 0))
    glVertex2fv((flag_width, 0))
    glVertex2fv((flag_width, flag_height))
    glVertex2fv((0, flag_height))
    glEnd()

    # Отрисовка Георгиевского креста (флаг Англии)
    glBegin(GL_QUADS)
    glColor3fv(red)
    glVertex2fv((0, flag_height * .4))
    glVertex2fv((flag_width, flag_height * .4))
    glVertex2fv((flag_width, flag_height * .6))
    glVertex2fv((0, flag_height * .6))
    glVertex2fv((flag_width*.44, 0))
    glVertex2fv((flag_width * .44, flag_height))
    glVertex2fv((flag_width * .56, flag_height))
    glVertex2fv((flag_width * .56, 0))
    glEnd()


    # первая четверть
    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((0, 2/3 * flag_height))
    glVertex2fv((0, .885 * flag_height))
    glVertex2fv((.216 * flag_width,  2/3 * flag_height))
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(red)
    glVertex2fv((0, .92*flag_height))
    glVertex2fv((.255 * flag_width, 2/3 * flag_height))
    glVertex2fv((.337 * flag_width, 2/3 * flag_height))
    glVertex2fv((0, flag_height))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((.121 * flag_width, flag_height))
    glVertex2fv((.403 * flag_width, .712 * flag_height))
    glVertex2fv((.403 * flag_width, flag_height))
    glEnd()

    # вторая четверть
    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((flag_width, 2 / 3 * flag_height))
    glVertex2fv((flag_width, .885 * flag_height))
    glVertex2fv((((1-.216) * flag_width, 2 / 3 * flag_height)))
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(red)
    glVertex2fv((.92 * flag_width, flag_height))
    glVertex2fv((.60173* flag_width, 2 / 3 * flag_height))
    glVertex2fv((2 / 3* flag_width, 2 / 3 * flag_height))
    glVertex2fv((flag_width, flag_height))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((.60173 * flag_width, flag_height))
    glVertex2fv((.60173 * flag_width, .712 * flag_height))
    glVertex2fv((.885 * flag_width, flag_height))
    glEnd()


    # третья четверть
    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((flag_width, (1-2 / 3) * flag_height))
    glVertex2fv((flag_width, (1-.885 )* flag_height))
    glVertex2fv(((1-.216 )* flag_width, (1-2 / 3) * flag_height))
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(red)
    glVertex2fv((flag_width, (1-.92) * flag_height))
    glVertex2fv(((1-.255) * flag_width, (1- 2 / 3) * flag_height))
    glVertex2fv(((1-.337) * flag_width, (1- 2 / 3) * flag_height))
    glVertex2fv((flag_width, 0))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv(((1-.121) * flag_width, 0))
    glVertex2fv(((1-.403) * flag_width, (1-.712) * flag_height))
    glVertex2fv(((1-.403) * flag_width, 0))
    glEnd()

    #четвертая четверть
    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv((0, (1-2 / 3) * flag_height))
    glVertex2fv((0, (1-.885 )* flag_height))
    glVertex2fv(((.216 * flag_width, (1-2 / 3) * flag_height)))
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(red)
    glVertex2fv(((1-.92) * flag_width, 0))
    glVertex2fv(((1-.60173) * flag_width, (1-2 / 3) * flag_height))
    glVertex2fv(((1-2 / 3) * flag_width, (1-2 / 3) * flag_height))
    glVertex2fv((0, 0))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(blue)
    glVertex2fv(((1-.60173) * flag_width, 0))
    glVertex2fv(((1-.60173) * flag_width, (1-.712) * flag_height))
    glVertex2fv(((1-.885) * flag_width, 0))
    glEnd()

# Инициализация Pygame.mixer (модуль для звука)
pygame.mixer.init()
pygame.mixer.music.load('British Grenadiers.mp3')
pygame.mixer.music.play()
pygame.mixer.music.pause()

def main():
    pygame.init()
    display = (flag_width, flag_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, flag_width, 0, flag_height, -1, 1)

    music_playing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # Воспроизвести музыку при наведении мыши на приложение
        if pygame.mouse.get_focused() and not music_playing:
            pygame.mixer.music.unpause()
            music_playing = True
        elif not pygame.mouse.get_focused() and music_playing:
            pygame.mixer.music.pause()
            music_playing = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_union_jack()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
