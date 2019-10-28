#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#		It's my first actual game-making attempt. I know code could be much better 
#		with classes or defs but I tried to make it short and understandable with very 
#		little knowledge of python and pygame(I'm one of them). Enjoy.

import pygame
from pygame.locals import *
from sys import exit
import random
import time

#Define some colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 200, 0)
red = (200, 0, 0)

bright_red = (255,0,0)
bright_green = (0,255,0)

display_width = 640
display_height = 480

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def Pong_single():
    #Creating 2 bars, a ball and background.
    back = pygame.Surface((display_width,display_height))
    background = back.convert()
    background.fill((0,0,0))
    bar = pygame.Surface((10,50))
    bar1 = bar.convert()
    bar1.fill((0,0,255))
    bar2 = bar.convert()
    bar2.fill((255,0,0))
    circ_sur = pygame.Surface((15,15))
    circ = pygame.draw.circle(circ_sur,(0,255,0),(int(15/2),int(15/2)),int(15/2))
    circle = circ_sur.convert()
    circle.set_colorkey((0,0,0))
    
    # some definitions
    bar1_x, bar2_x = 10. , 620.
    bar1_y, bar2_y = 215. , 215.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.
    speed_x, speed_y, speed_circ = 150., 150., 250.
    bar1_score, bar2_score = 0,0
    #font objects 
    font = pygame.font.SysFont("times new roman",40)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    bar1_move = -ai_speed
                elif event.key == K_DOWN:
                    bar1_move = ai_speed
                elif event.key == K_ESCAPE:
                    exit()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    bar1_move = 0.
                elif event.key == K_DOWN:
                    bar1_move = 0.
        
        score1 = font.render(str(bar1_score), True,(255,255,255))
        score2 = font.render(str(bar2_score), True,(255,255,255))
    
        screen.blit(background,(0,0))
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))
        screen.blit(score1,(250.,210.))
        screen.blit(score2,(380.,210.))
    
        bar1_y += bar1_move
        
    # movement of circle
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        
        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec
    #AI of the computer.
        if circle_x >= 305.:
            if not bar2_y == circle_y + 7.5:
                if bar2_y < circle_y + 7.5:
                    bar2_y += ai_speed
                if  bar2_y > circle_y - 42.5:
                    bar2_y -= ai_speed
            else:
                bar2_y == circle_y + 7.5
        
        if bar1_y >= 420.: bar1_y = 420.
        elif bar1_y <= 10. : bar1_y = 10.
        if bar2_y >= 420.: bar2_y = 420.
        elif bar2_y <= 10.: bar2_y = 10.
    #since i don't know anything about collision, ball hitting bars goes like this.
        if circle_x <= bar1_x + 10.:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20.
                speed_x = -speed_x
        if circle_x >= bar2_x - 15.:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605.
                speed_x = -speed_x
        if circle_x < 5.:
            bar2_score += 1
            circle_x, circle_y = 320., 232.5
            bar1_y,bar_2_y = 215., 215.
        elif circle_x > 620.:
            bar1_score += 1
            circle_x, circle_y = 307.5, 232.5
            bar1_y, bar2_y = 215., 215.
        if circle_y <= 10.:
            speed_y = -speed_y
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y
            circle_y = 457.5
    
        pygame.display.update()


def Pong_multi():
    #Creating 2 bars, a ball and background.
    back = pygame.Surface((display_width,display_height))
    background = back.convert()
    background.fill((0,0,0))
    bar = pygame.Surface((10,50))
    bar1 = bar.convert()
    bar1.fill((0,0,255))
    bar2 = bar.convert()
    bar2.fill((255,0,0))
    circ_sur = pygame.Surface((15,15))
    circ = pygame.draw.circle(circ_sur,(0,255,0),(int(15/2),int(15/2)),int(15/2))
    circle = circ_sur.convert()
    circle.set_colorkey((0,0,0))
    
    # some definitions
    bar1_x, bar2_x = 10. , 620.
    bar1_y, bar2_y = 215. , 215.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.
    speed_x, speed_y, speed_circ = 150., 150., 250.
    bar1_score, bar2_score = 0,0
    #font objects
    font = pygame.font.SysFont("times new roman",40)
    
    while True:
        
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    bar1_move = -ai_speed
                    print(bar1_move)
                elif event.key == K_s:
                    bar1_move = ai_speed
                elif event.key == K_ESCAPE:
                    exit()
            elif event.type == KEYUP:
                if event.key == K_w:
                    bar1_move = 0.
                elif event.key == K_s:
                    bar1_move = 0.
        
        #for event in pygame.event.get():
        #    print(event)
        #    if event.type == QUIT:
        #        exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    bar2_move = -ai_speed
                    print(bar2_move)
                elif event.key == K_DOWN:
                    bar2_move = ai_speed
                elif event.key == K_ESCAPE:
                    exit()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    bar2_move = 0.
                elif event.key == K_DOWN:
                    bar2_move = 0.

        
        score1 = font.render(str(bar1_score), True,(255,255,255))
        score2 = font.render(str(bar2_score), True,(255,255,255))
    
        screen.blit(background,(0,0))
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))
        screen.blit(score1,(250.,210.))
        screen.blit(score2,(380.,210.))
    
        bar1_y += bar1_move
        bar2_y += bar2_move

    # movement of circle
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        
        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec
    
    
    #AI of the computer.
    #    if circle_x >= 305.:
    #        if not bar2_y == circle_y + 7.5:
    #            if bar2_y < circle_y + 7.5:
    #                bar2_y += ai_speed
    #            if  bar2_y > circle_y - 42.5:
    #                bar2_y -= ai_speed
    #        else:
    #            bar2_y == circle_y + 7.5
    #    
        if bar1_y >= 420.: bar1_y = 420.
        elif bar1_y <= 10. : bar1_y = 10.
        if bar2_y >= 420.: bar2_y = 420.
        elif bar2_y <= 10.: bar2_y = 10.
    #since i don't know anything about collision, ball hitting bars goes like this.
        if circle_x <= bar1_x + 10.:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20.
                speed_x = -speed_x
        if circle_x >= bar2_x - 15.:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605.
                speed_x = -speed_x
        if circle_x < 5.:
            bar2_score += 1
            circle_x, circle_y = 320., 232.5
            bar1_y,bar_2_y = 215., 215.
        elif circle_x > 620.:
            bar1_score += 1
            circle_x, circle_y = 307.5, 232.5
            bar1_y, bar2_y = 215., 215.
        if circle_y <= 10.:
            speed_y = -speed_y
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y
            circle_y = 457.5
    
        pygame.display.update()

pygame.init()

screen=pygame.display.set_mode((display_width,display_height),0,32)
pygame.display.set_caption("Pong Pong!")
intro = True
clock = pygame.time.Clock()

while intro:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           pygame.quit()
           quit()
               
    screen.fill(black)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Pong Pong!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 150+150 > mouse[0] > 150 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, bright_green,(150,350,150,50))
        if click[0] == 1:
            intro = False
            Pong_single()
    else:
        pygame.draw.rect(screen, green,(150,350,150,50))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("Single Player", smallText)
    textRect.center = ( (150+(150/2)), (350+(50/2)) )
    screen.blit(textSurf, textRect)
    if 350+150 > mouse[0] > 350 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, bright_red,(350,350,150,50))
        if click[0] == 1:
            intro = False
            Pong_multi()
    else:
        pygame.draw.rect(screen, red,(350,350,150,50))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("Multiplayer", smallText)
    textRect.center = ( (350+(150/2)), (350+(50/2)) )
    screen.blit(textSurf, textRect)
        
    pygame.display.update()
    clock.tick(15)


