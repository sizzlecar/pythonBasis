import random
import pygame
from pygame.locals import *

WIDTH = 500
HEIGHT = 400
unlike_pos_x = 100
unlike_pos_y = 200
unlike_pos_width = 100
unlike_pos_height = 50


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    return x, y


# 获取鼠标位置
# 若鼠标位置位于按钮区域内
# 则随机生成按钮位置进行显示
pygame.init()
pygame.display.set_mode([1000, 700])
flag = 1
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 0

mouse_pos = pygame.mouse.get_pos()
print(mouse_pos[0], mouse_pos[1])
if mouse_pos[0] < unlike_pos_x + unlike_pos_width and mouse_pos[0] > unlike_pos_x and \
        mouse_pos[1] < unlike_pos_y + unlike_pos_height and mouse_pos[1] > unlike_pos_y:

    while True:
        unlike_pos_x, unlike_pos_y = get_random_pos()
        if mouse_pos[0] < unlike_pos_x + unlike_pos_width and mouse_pos[0] > unlike_pos_x and \
                mouse_pos[1] < unlike_pos_y + unlike_pos_height and mouse_pos[1] > unlike_pos_y:
            continue
        break

print("exit ....")
