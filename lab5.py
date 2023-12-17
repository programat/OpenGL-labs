import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glutInit()

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)


def draw_cube(x_translation, y_translation):
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
        (0, 4),
        (1, 5),
        (2, 3),  # Добавляем рёбра, которые соединяют вершины куба по задней стороне
        (6, 7),
        (0, 1),
        (5, 4)
    )

    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


x_rotation = 0
y_rotation = 0
x_translation = 0
y_translation = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        y_rotation += 1
    if keys[pygame.K_RIGHT]:
        y_rotation -= 1
    if keys[pygame.K_UP]:
        x_rotation += 1
    if keys[pygame.K_DOWN]:
        x_rotation -= 1
    if keys[pygame.K_w]:
        y_translation += 0.1
    if keys[pygame.K_s]:
        y_translation -= 0.1
    if keys[pygame.K_a]:
        x_translation -= 0.1
    if keys[pygame.K_d]:
        x_translation += 0.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(x_translation, y_translation, -5)
    glRotatef(x_rotation, 1, 0, 0)
    glRotatef(y_rotation, 0, 1, 0)

    draw_cube(x_translation, y_translation)

    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)
