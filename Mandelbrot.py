import sys
import numpy as np
import pygame
from OpenGL.GL import *

# Размер окна
WIDTH, HEIGHT = 800, 800

# Границы Мандельброта
X_MIN, X_MAX = -2.0, 1.0
Y_MIN, Y_MAX = -1.5, 1.5

# Максимальное количество итераций для проверки сходимости
MAX_ITER = 256

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Преобразование координат окна в координаты Мандельброта
            real = X_MIN + (x / WIDTH) * (X_MAX - X_MIN)
            imag = Y_MIN + (y / HEIGHT) * (Y_MAX - Y_MIN)

            c = complex(real, imag)
            color = 1.0 - (mandelbrot(c) / MAX_ITER)  # Инвертируем цвет
            glColor3f(color, color, color)
            glVertex2f(x, y)

    glEnd()
    glFlush()

def main():
    pygame.init()
    display_surf = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glViewport(0, 0, WIDTH, HEIGHT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        display()
        pygame.display.flip()

if __name__ == "__main__":
    main()
