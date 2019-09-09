from random import randint
import pygame
from pygame.locals import *

from constants import *


pygame.init()

class Maze:
    
    def __init__(self):
        self.file = "Maze.txt"
        self.player = Player
    def load(self):
        structure_maze = []
        with open(self.file, "r") as filename:
            for line in filename:
                line_maze = []
                for letter in line:
                    if letter != "\n":
                        line_maze.append(letter)
                structure_maze.append(line_maze)
                self.structure = structure_maze
            #return structure_maze
        
    def display(self, window):
        window = pygame.display.set_mode((450, 450))
        pygame.display.set_caption(window_title)
        WALL = pygame.image.load("images/wall.png").convert()
        MG = pygame.image.load("images/macgyver.png").convert_alpha() 
        GOAL = pygame.image.load("images/gardian.png").convert_alpha()
        FLOOR = pygame.image.load("images/floor.png").convert()
        ETHER = pygame.image.load("images/ethertest.png").convert()
        ETHER.set_colorkey(BLACK)
        NEEDLE = pygame.image.load("images/needletest.png").convert()
        NEEDLE.set_colorkey(BLACK)
        PIPE = pygame.image.load("images/pipetest.png").convert()
        PIPE.set_colorkey(WHITE)
        accueil = pygame.image.load("images/title.PNG").convert()
        SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()
        SYRINGE.set_colorkey(WHITE)

        num_line = 0
        for line in self.structure:
            num_col = 0
            for letter in line:     
                x = num_col * letter_size
                y = num_line * letter_size
                if letter == '#':
                    window.blit(WALL, (x,y))
                elif letter == 'p'or letter == "M":
                    window.blit(MG, (x,y))
                elif letter == 'g':
                    window.blit(GOAL, (x,y))
                elif letter == " ":
                    window.blit(FLOOR, (x,y))
                elif letter == "E":
                    window.blit(ETHER, (x,y))
                elif letter == "N":
                    window.blit(NEEDLE, (x,y))  
                elif letter == "T":
                    window.blit(PIPE, (x,y))      
                num_col += 1
            num_line += 1   
               
  
    def display_status(structure_maze, x, y, object_inventory):       
        if len(object_inventory) == 3:
            window.blit(SYRINGE, (0,0))
        if "E" in object_inventory:
            window.blit(ETHER,(35, 0))
        if "N" in object_inventory:
            window.blit(NEEDLE,(70, 0))
        if "T" in object_inventory:
            window.blit(PIPE,(105, 0))
    
        #pygame.display.flip()          

class Player:
    def __init__(self):
    #self.structure_maze = structure_maze           
        self.position_x = 0
        self.position_y = 0
        self.x = 0
        self.y = 0
        
    def position(self, direction):
        if direction == "q":
            if self.position_x > 0:
                if self.structure_maze[self.position_y][self.position_x-1] != "#":
                    self.position_x -= 1
                    self.x = self.position_x.letter_size
        elif direction == "d":
            if self.position_x < (len(structure_maze) - 1):
                if self.structure_maze[self.position_y][self.position_x+1] != "#":
                    self.position_x += 1 
                    self.x = self.position_x.letter_size 
        elif direction == "z":
            if self.position_y > 0:
                if self.structure_maze[self.position_y-1][self.position_x] != "#":
                    self.position_y -= 1
                    self.y = self.position_y.letter_size
        elif direction == "s":
            if self.position_y < (len(structure_maze) - 1):
                if self.structure_maze[self.position_y+1][self.position_x] != "#":
                    self.position_y += 1 
                    self.y = self.position_y.letter_size
        return (self.position_x, self.position_y)           

  
class Items:
    
    def __init(self, pos_x, pos_y, image, structure_maze):
        self.structure_maze = structure_maze
        self.pos_x = 0
        self.pos_y = 0 
        self.x = 0
        self.y = 0
        self.object_x = object_x
        self.object_y = object_y 
        self.image = image
        ether = pygame.image.load("ethertest.png").convert_alpha()
        needle = pygame.image.load("needletest.png").convert_alpha()
        pipe = pygame.image.load("pipetest.png").convert_alpha()
    
    def random_position(self, structure_maze):
        while True:
            self.pos_y = randint(0, 14)
            self.pos_x = randint(0, 14)
            if self.structure_maze[self.pos_y][self.pos_x] == " ":
                self.x = self.pos_x * letter_size
                self.y = self.pos_y * letter_size
                return (self.y, self.x)
         
    def position_object(self, maze):
        for object in ["E", "N", "T"]:
            self.object_y, self.object_x = random_position(maze)
            self.maze[self.object_y][self.object_x] = object
    
        
                    
