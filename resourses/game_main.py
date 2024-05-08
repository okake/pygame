import pygame
from pygame.locals import *
import sys
import pop_class

import numpy as np
import random

screen_w,screen_h = 1200,800
genome_length = 19
id = 0

def main():
    pygame.init()
    pygame.display.get_surface()
    screen = pygame.display.set_mode((screen_w,screen_h),0,32)
    #screen = pygame.display.set_mode((screen_w,screen_h),FULLSCREEN)

    init_pop_num = 3
    childs = []
    for i in range(init_pop_num):
        genome,pos = pop_class.define_init_genome()
        child = pop_class.individual(id,genome,pos)
        childs.append(child)
        id += 1
    pop = pop_class.population(childs)

    while (1):
        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,20,0,0))

        pygame.draw.circle(screen,(0,200,0),(x,y),5)

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEMOTION:
                x,y = event.pos


if __name__ == "__main__":
    main()