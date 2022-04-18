#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 22:55
# @Author  : 章
# @File    : snake_v2.py
# @Software: PyCharm
import time
import pygame, random
from pygame.locals import *
# 定义要用到的颜色，方便输入
pink = (255, 182, 193)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

def snake_food():
    pygame.init()
    wid, hei = 600, 500
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("贪吃蛇")
    # 蛇头,蛇，食物初始位置
    snakehead = [100, 100]  # 蛇头位置

    snake = [[100, 100]]

    foodpostion = [300, 300]
    # 食物状态 1为没有被吃掉，0 为被吃掉了
    foodstate =1
    # 初始默认方向
    direction = 'right'
    # 定义改变方向
    changeDirection = direction

    speed = 20
    def paused():
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type ==KEYDOWN:
                    if event.key == K_p:
                        # is_paused = False
                        is_paused == False
                        # return False
                        return
            pygame.display.update()
            time.sleep(0.3)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    paused()

                if event.key == K_RIGHT:
                    changeDirection = 'right'

                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'

        # 确认方向，限定反方向运动无效

        if changeDirection == 'right' and direction != 'left':
            direction = changeDirection
        if changeDirection == 'left' and direction != 'right':
            direction = changeDirection
        if changeDirection == 'up' and direction != 'down':
            direction = changeDirection
        if changeDirection == 'down' and direction != 'up':
            direction = changeDirection

        # 让柁根据方向动起来， 得到新的蛇头位置
        if direction == 'right':
            snakehead[0] += speed
        if direction == 'left':
            snakehead[0] -= speed
        if direction == 'up':
            snakehead[1] -= speed
        if direction == 'down':
            snakehead[1] += speed

        if snakehead == foodpostion:  # 吃掉食物则增加新的蛇头到身体
            snake.insert(0, snakehead[:])  # 深拷贝切记
            foodstate = 0  # 吃掉后，食物状态改成0 然后随机生成新的食物
            foodpostion = [random.randint(1, 29) * 20, random.randint(1, 24) * 20]
            if foodpostion not in snake:
                foodstate = 1  # 生成之后状态继续恢复为1
        else:  # 没有吃掉，则头加尾减
            snake.insert(0, snakehead[:])
            snake.pop()  # 每次将最后一单位蛇身剔除列表

        def draw_snake_food():
            screen.fill(black)
            # 食物随机生成的位置不能与蛇的位置干扰 需要完善
            pygame.draw.rect(screen, white, (foodpostion[0], foodpostion[1], 20, 20))
            # 先画蛇头，颜色分开来画蛇身
            pygame.draw.rect(screen, yellow, (snakehead[0], snakehead[1], 20, 20))
            for i in snake[1:]:
                pygame.draw.rect(screen, pink, (i[0], i[1], 20, 20))

            pygame.display.flip()
            time.sleep(0.3)

        def game_over():
            # 结束条件，到屏幕外了，头和器官相撞了
            if snakehead[0] > wid or snakehead[0] < 0:
                return False
            elif snakehead[1] > hei or snakehead[1] < 0:
                return False
            for j in snake[1:]:
                if j == snakehead:
                    return False

        draw_snake_food()
        if game_over() == False:

            break


if __name__ == '__main__':
    snake_food()

