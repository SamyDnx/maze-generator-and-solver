import sys
sys.setrecursionlimit(5000)

import pygame
import random
from collections import deque

pygame.init()

# 101 7
ROWS, COLLS = 101, 101    # Needs to be odd
CELL_SIZE = 7
HEIGHT, WIDTH = COLLS * CELL_SIZE, ROWS * CELL_SIZE
CHANCE = 0.05
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Maze Solver")

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # U, R, L, D

def init_grid(height, width):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    return maze

def generate_maze(x=0, y=0):
    maze[x][y] = 0

    random.shuffle(directions)
    for dir_x, dir_y in directions:
        nei_x, nei_y = x + dir_x * 2, y + dir_y * 2
        if 0 <= nei_x < ROWS and 0 <= nei_y < COLLS and maze[nei_x][nei_y] == 1:
            maze[x + dir_x][y + dir_y] = 0
            generate_maze(nei_x, nei_y)

### This func was made by chatgpt because its late ###
# Function to randomly remove some walls to introduce loops in the maze
def create_loops(maze, chance=CHANCE):
    for x in range(1, ROWS - 1):
        for y in range(1, COLLS - 1):
            # Only consider walls between two open cells
            if maze[x][y] == 1:
                neighbors = 0
                for dir_x, dir_y in directions:
                    nei_x, nei_y = x + dir_x, y + dir_y
                    if 0 <= nei_x < ROWS and 0 <= nei_y < COLLS and maze[nei_x][nei_y] == 0:
                        neighbors += 1
                # If there are two or more open neighbors, remove the wall with a small chance
                if neighbors >= 2 and random.random() < chance:
                    maze[x][y] = 0

def bfs_solve(maze, start, goal):
    frontier = deque([start])
    visited = set([start])
    parent = {}

    while frontier:
        curr = frontier.popleft()

        if curr == goal:
            break

        for dir_x, dir_y in directions:
            nei = (curr[0] + dir_x, curr[1] + dir_y)

            if 0 <= nei[0] < ROWS and 0 <= nei[1] < COLLS and nei not in visited and maze[nei[0]][nei[1]] == 0:
                frontier.append(nei)
                visited.add(nei)
                parent[nei] = curr
    
    # Backtrack to breakdown the path found
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()

    return (path, visited)

# TODO : Implement dfs
def dfs_solve(maze, start, goal):
    ...

def draw_maze(maze):
    window.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLLS):
            rect = pygame.Rect((j)*CELL_SIZE, (i)*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            match maze[i][j]:
                case 0:
                    color = WHITE
                case 1:
                    color = BLACK
                case 2:
                    color = BLUE
                case -2:
                    color = RED
            pygame.draw.rect(window, color, rect)
            pygame.display.flip()

def draw_path(path, color):
    for coor in path:
        rect = pygame.Rect(coor[1]*CELL_SIZE, coor[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(window, color, rect)
        pygame.display.flip()

def draw_visited(visited, color):
    for coor in visited:
        rect = pygame.Rect(coor[1]*CELL_SIZE, coor[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(window, color, rect)
        pygame.display.flip()


maze = init_grid(ROWS, COLLS)
generate_maze()
create_loops(maze, CHANCE)  # Add loops to the maze by removing walls
draw_maze(maze)

show_solution = False
show_visited = False

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        # TODO : addapt the input handler for different solving algorithms
        elif event.type == pygame.KEYDOWN:
            bfs = bfs_solve(maze, (0,0), (ROWS-1, COLLS-1))
            if event.key == pygame.K_SPACE:
                if show_solution: draw_path(bfs[0], WHITE)
                else: draw_path(bfs[0], GREEN)
                show_solution = not show_solution
                show_visited = False
            elif event.key == pygame.K_e:
                if show_visited: draw_visited(bfs[1], WHITE)
                else: draw_visited(bfs[1], RED)
                show_visited = not show_visited
                show_solution = False
            elif event.key == pygame.K_BACKSPACE:
                draw_path(bfs[0], WHITE)
                draw_visited(bfs[1], WHITE)
                show_solution = False
                show_visited = False
            elif event.key == pygame.K_r:
                maze = init_grid(ROWS, COLLS)
                generate_maze()
                create_loops(maze)
                draw_maze(maze)
                show_solution = False
                show_visited = False
