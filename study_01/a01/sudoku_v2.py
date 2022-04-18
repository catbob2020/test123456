#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 16:27
# @Author  : 章
# @File    : sudoku_v2.py
# @Software: PyCharm

import pygame as p
import numpy as np

class Win:
    w, h = 490, 490  # 设置窗口大小

    def __init__(self):  # 定义实例属性  方便Game中调用
        self.screen = p.display.set_mode((Win.w, Win.h))  # 建立窗口

    @classmethod
    def drawwin(cls):
        p.init()  # 初始化pygame
        p.display.set_caption('sudoku')  # 设置标题
        screen = p.display.set_mode((Win.w, Win.h))  # 建立窗口
        screen.fill((255, 255, 255))  # 背景颜色

        for i in range(9):  # 绘制格子
            p.draw.rect(screen, (255, 0, 0), (0, Win.h / 9 * i, Win.w, Win.h / 9), 1)
        for j in range(9):
            p.draw.rect(screen, (255, 0, 0), (Win.w / 9 * j, 0, Win.h / 9, Win.w), 1)
        # 把九宫格加粗显示,右自行选择是否开启，  方便观看
        # p.draw.rect(screen, (255, 0, 0), (0, Win.h / 3, Win.w, Win.h / 3), 10)
        # p.draw.rect(screen, (255, 0, 0), (Win.w / 3, 0, Win.w / 3, Win.h), 10)


# w1 = Win()  # 实例化Win 给Game调用


class Game:

    def __init__(self):

        # 游戏开始之前，请从外部写入一个9*9数独列表并且命名为K
        self.k = [[col for col in row] for row in k]  # ->list[list[int]]

        self.emptyk = []  # 读取实例对象数独列表中所有原始已有数字的行列位置
        for mi in range(0, 9):
            for mj in range(0, 9):
                if self.k[mi][mj] != 0:
                    self.emptyk.append([mi, mj])
                    self.emptyk = self.emptyk[:]

        # Win.drawwin()  # 调用Win类的动态方法建立游戏窗口页面

    def start(self):
        p.init()

        pgx, pgy = 0, 0
        while True:

            for event in p.event.get():
                if event.type == p.QUIT:
                    exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    pgx, pgy = int(event.pos[0] // (Win.w / 9)), int(event.pos[1] // (Win.h / 9))
                if event.type == p.KEYUP:
                    if int(chr(event.key)) in [xx for xx in range(1, 10)] and [pgy, pgx] not in self.emptyk:
                        self.k[pgy][pgx] = int(chr(event.key))
                        print(np.matrix(self.k))
            Win.drawwin()
            p.draw.rect(w1.screen, (0, 0, 255),
                        (pgx * int(Win.w / 9), pgy * int(Win.h / 9), int(Win.w / 9), int(Win.h / 9)), 10)  # 覆盖刷新
            Game.drawnum(self)  # 写入新数独状态
            if self.check_done():
                w1.screen.fill((0,0,0))
                gameoverimg = p.image.load('gameoverpic.jpeg')
                w1.screen.blit(gameoverimg, (250, 250))
                p.display.update()
                p.time.wait(5000)
                print('Game over')
                break
            p.display.flip()

    @staticmethod  # 静态方法用来检查填充数字是否合法
    def check_torf(k2, i, j, number):
        if number in k2[i]:
            return False
        if number in list(set(list(zip(*k2))[j])):
            return False
        nii, njj = i // 3, j // 3
        if number in [k2[i][j] for i in range(nii * 3, (nii + 1) * 3) for j in
                      range(njj * 3, (njj + 1) * 3)]:
            return False
        return True

    def part_color(self, _k, ii, jj):  # 检查颜色
        _k = [[num for num in row] for row in self.k]
        _k[ii][jj] = 0  # 针对检查原来的空位
        if Game.check_torf(_k, ii, jj, self.k[ii][jj]):
            return (0, 255, 0)
        return (255, 0, 0)

    def drawnum(self):  # 把列表中的数字填写到Pygamwe画面
        for _i in range(9):
            for _j in range(9):
                font = p.font.Font(None, 100)
                _color = self.part_color(self.k, _i, _j) if [_i, _j] not in self.emptyk else (128, 128, 128)
                textImage = font.render(str(self.k[_i][_j] if self.k[_i][_j] != 0 else ''), True, _color, (255, 215, 0))
                newtxt = p.transform.scale(textImage, (int(Win.w / 9) - 20, int(Win.w / 9) - 20))
                xg, yg = _j * int(Win.w / 9) + 10, _i * int(Win.h / 9) + 10
                w1.screen.blit(newtxt, (xg, yg))

    def check_done(self):  # 检查出局退出
        kdone = [[jjj for jjj in iii] for iii in self.k]
        check = list(range(1, 10))
        kdone2 = list(zip(*kdone))
        for i in range(9):
            check_i = kdone[i]
            if sorted(check_i) != check:
                return False
        for j in range(9):
            check_j = list(kdone2[j])
            if sorted(check_j) != check:
                return False
        for _i in range(3):
            for _j in range(3):
                box = [kdone[_i * 3 + r][_j * 3 + c] for r in range(3) for c in range(3)]
                if sorted(box) != check:
                    return False
        return True

    def check(self):  # 检查初始给出的数独列表是否存在明显问题
        global box
        kj = list(zip(*self.k))  # 数独行列互换得到的以无组为元素的列表
        for i in range(9):
            numlist = [num for num in self.k[i] if num != 0]
            numset = {num for num in self.k[i] if num != 0}
            if len(numlist) != len(numset):
                return False

        for j in range(9):
            numlist = [num for num in list(kj[j]) if num != 0]
            numset = {num for num in list(kj[j]) if num != 0}
            if len(numlist) != len(numset):
                return False
        for _i in range(3):
            for _j in range(3):
                box = [self.k[_i * 3 + r][_j * 3 + c] for r in range(3) for c in range(3)]
            numlist = [num for num in box if num != 0]
            numset = {num for num in box if num != 0}
            if len(numlist) != len(numset):
                return False

        return True

if __name__ == '__main__':
    k = [
        [0, 0, 0, 9, 3, 4, 8, 2, 5],
        [3, 5, 4, 6, 2, 8, 1, 9, 7],
        [9, 2, 8, 1, 5, 7, 6, 3, 4],
        [2, 1, 9, 5, 4, 6, 3, 7, 8],
        [4, 8, 3, 2, 7, 9, 5, 1, 6],
        [5, 7, 6, 3, 8, 1, 9, 4, 2],
        [1, 9, 5, 7, 6, 2, 4, 8, 3],
        [8, 3, 2, 4, 9, 5, 7, 6, 1],
        [6, 4, 7, 8, 1, 3, 2, 5, 9]]
    # k = [
    #     [0, 6, 1, 0, 3, 0, 0, 2, 0],
    #     [0, 5, 0, 0, 0, 8, 1, 0, 7],
    #     [0, 0, 0, 0, 0, 7, 0, 3, 4],
    #     [0, 0, 9, 0, 0, 6, 0, 7, 8],
    #     [0, 0, 3, 2, 0, 9, 5, 0, 0],
    #     [5, 7, 0, 3, 0, 0, 9, 0, 0],
    #     [1, 9, 0, 7, 0, 0, 0, 0, 0],
    #     [8, 0, 2, 4, 0, 0, 0, 6, 0],
    #     [0, 4, 0, 0, 1, 0, 2, 5, 0]
    # ]
    w1 = Win()
    g1 = Game()
    if g1.check():
        print('题目合法,请开心的玩')
        g1.start()
    else:
        print('题目不合法，退出游戏')




