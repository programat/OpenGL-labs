import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

rotation_speed = 1  # Скорость вращения
auto_rotation_speed = 0.2

snowflakes = []


def draw_tree():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # Зеленый цвет
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glEnd()


def draw_trunk():
    glPushMatrix()
    glTranslatef(0.0, -0.2, 0.0)
    glColor3f(0.5, 0.3, 0.0)  # Коричневый цвет
    glScalef(0.2, 0.2, 0.2)
    glutSolidCube(1.0)
    glPopMatrix()


def draw_star():
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)  # Желтый цвет
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 2.2, 0.0)
    glVertex3f(-0.1, 2.0, 0.0)
    glVertex3f(0.1, 2.0, 0.0)

    glVertex3f(0.0, 2.1, 0.0)
    glVertex3f(-0.1, 1.9, 0.0)
    glVertex3f(0.1, 1.9, 0.0)
    glEnd()
    glPopMatrix()


def draw_balls():
    glColor3f(1.0, 0.0, 0.0)  # Красный цвет
    glPushMatrix()
    glTranslatef(0.0, 1.7, 0.0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.2, 1.3, 0.0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.2, 1.3, 0.0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()


def generate_snowflake():
    x = random.uniform(-2, 2)  # Случайные координаты снежинки по X
    y = 2.0  # Снежинка начинает с верхней части экрана
    z = random.uniform(-2, 2)  # Случайные координаты снежинки по Z
    size = random.uniform(0.03, 0.08)  # Случайный размер снежинки
    speed = random.uniform(0.002, 0.008)  # Случайная скорость падения снежинки
    return [x, y, z, size, speed]


def draw_snowflake(snowflake):
    x, y, z, size, speed = snowflake
    glColor3f(1.0, 1.0, 1.0)  # Белый цвет
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidSphere(size, 10, 10)
    glPopMatrix()

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Mariah Carey.mp3")  # Укажите путь к вашему аудиофайлу
    pygame.mixer.music.play(-1, start=46000)  # -1 означает бесконечное воспроизведение

def main():
    pygame.init()
    pygame.display.set_caption("Happy New Year 🎅")
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glFrustum(-1, 1, -1, 1, 2, 10)  # Устанавливаем матрицу проекции

    glTranslatef(0.0, 0.0, -5.0)

    auto_rotate = False
    is_music_playing = False  # Флаг для отслеживания воспроизведения музыки

    for _ in range(100):  # Генерируем начальное количество снежинок
        snowflakes.append(generate_snowflake())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    auto_rotate = not auto_rotate
                    if auto_rotate:
                        if not is_music_playing:
                            play_music()
                            is_music_playing = True
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glRotatef(rotation_speed, 0, 1, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(-rotation_speed, 0, 1, 0)
        if keys[pygame.K_UP]:
            glRotatef(rotation_speed, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(-rotation_speed, 1, 0, 0)

        if auto_rotate:
            glRotatef(auto_rotation_speed, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_tree()
        draw_trunk()
        draw_star()
        draw_balls()

        for i, snowflake in enumerate(snowflakes):
            x, y, z, size, speed = snowflake
            y -= speed
            if y < -2.0:  # Если снежинка упала ниже нижней границы экрана, создаем новую
                snowflakes[i] = generate_snowflake()
            else:
                snowflakes[i] = [x, y, z, size, speed]
                if auto_rotate:
                    draw_snowflake(snowflake)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
