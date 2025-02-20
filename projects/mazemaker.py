# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

import random
from colorama import init, Fore

# colorama needs to be initialized in order to be used
init()

UNVISITED = "."
WALL = "█"
CELL = " "

# UNVISITED = "u"
# WALL = "w"
# CELL = "c"


def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(UNVISITED)
        maze.append(line)
    return maze


def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == UNVISITED:
                print(Fore.WHITE, f"{UNVISITED}", end="")
            elif maze[i][j] == CELL:
                print(Fore.GREEN, f"{CELL}", end="")
            else:
                print(Fore.RED, f"{WALL}", end="")
        print("\n")


def surroundingCells(rand_wall):
    s_cells = 0
    if maze[rand_wall[0] - 1][rand_wall[1]] == CELL:
        s_cells += 1
    if maze[rand_wall[0] + 1][rand_wall[1]] == CELL:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] - 1] == CELL:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] + 1] == CELL:
        s_cells += 1
    return s_cells


def delete_wall(rand_wall):
    for wall in walls:
        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
            walls.remove(wall)


def create_maze():
    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Get the current x and y coordinates for ease of code reading
        x = rand_wall[1]
        y = rand_wall[0]

        # Check if it is a left wall
        if x != 0:
            if maze[y][x - 1] == UNVISITED and maze[y][x + 1] == CELL:
                # Find the number of surrounding cells
                # s_cells = surroundingCells(rand_wall)

                if surroundingCells(rand_wall) < 2:
                    # Denote the new path
                    maze[y][x] = CELL

                    # Mark the new walls
                    # Upper cell
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])

                    # Bottom cell
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])

                    # Leftmost cell
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])

                # Delete wall
                # for wall in walls:
                #     if wall[0] == y and wall[1] == x:
                #         walls.remove(wall)
                delete_wall(rand_wall)
                continue

        # Check if it is an upper wall
        if y != 0:
            if maze[y - 1][x] == UNVISITED and maze[y + 1][x] == CELL:

                # s_cells = surroundingCells(rand_wall)
                if surroundingCells(rand_wall) < 2:
                    # Denote the new path
                    maze[y][x] = CELL

                    # Mark the new walls
                    # Upper cell
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])

                    # Leftmost cell
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])

                    # Rightmost cell
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])

                # Delete wall
                # for wall in walls:
                #     if wall[0] == y and wall[1] == x:
                #         walls.remove(wall)
                delete_wall(rand_wall)
                continue

        # Check the bottom wall
        if y != height - 1:
            if maze[y + 1][x] == UNVISITED and maze[y - 1][x] == CELL:

                # s_cells = surroundingCells(rand_wall)
                if surroundingCells(rand_wall) < 2:
                    # Denote the new path
                    maze[y][x] = CELL

                    # Mark the new walls
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])

                # Delete wall
                # for wall in walls:
                #     if wall[0] == y and wall[1] == x:
                #         walls.remove(wall)
                delete_wall(rand_wall)
                continue

        # Check the right wall
        if x != width - 1:
            if maze[y][x + 1] == UNVISITED and maze[y][x - 1] == CELL:

                # s_cells = surroundingCells(rand_wall)
                if surroundingCells(rand_wall) < 2:
                    # Denote the new path
                    maze[y][x] = CELL

                    # Mark the new walls
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])

                # Delete wall
                # for wall in walls:
                #     if wall[0] == y and wall[1] == x:
                #         walls.remove(wall)
                delete_wall(rand_wall)
                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if wall[0] == y and wall[1] == x:
                walls.remove(wall)


def create_maze_old():
    # I hate the use of the global here
    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Get the current x and y coordinates for ease of code reading
        x = rand_wall[1]
        y = rand_wall[0]

        # If only one of the cells that the wall divides is visited
        # This means whe check left and right, as well as up and down

        # Make sure we're not on one of the edges
        # If it's not at the left or right edge
        if x != 0:
            # Check if it separates two open cells left and right
            if maze[y][x - 1] == UNVISITED and maze[y][x + 1] == CELL:
                # As long as there aren't any other open cells around us
                if surroundingCells(rand_wall) < 2:
                    # Turn this into an open cell
                    maze[y][x] = CELL

                    # Add the walls around us to the walls list
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])

                # delete_wall(rand_wall)
                # continue

        if x != width - 1:
            # Check if it separates two open cells left and right
            if maze[y][x + 1] == UNVISITED and maze[y][x - 1] == CELL:
                # As long as there aren't any other open cells around us
                if surroundingCells(rand_wall) < 2:
                    # Turn this into an open cell
                    maze[y][x] = CELL

                    # Add the walls around us to the walls list
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])

                # delete_wall(rand_wall)
                # continue

        # If it's not at the top or bottom edge
        if y != 0:
            # Check if it separates two open cells left and right
            if maze[y - 1][x] == UNVISITED and maze[y + 1][x] == CELL:
                # As long as there aren't any other open cells around us
                if surroundingCells(rand_wall) < 2:
                    # Turn this into an open cell
                    maze[y][x] = CELL

                    # Add the walls around us to the walls list
                    if y != 0:
                        if maze[y - 1][x] != CELL:
                            maze[y - 1][x] = WALL
                        if [y - 1, x] not in walls:
                            walls.append([y - 1, x])
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])
                # delete_wall(rand_wall)
                # continue

        if y != height - 1:
            # Check if it separates two open cells left and right
            if maze[y + 1][x] == UNVISITED and maze[y - 1][x] == CELL:
                # As long as there aren't any other open cells around us
                if surroundingCells(rand_wall) < 2:
                    # Turn this into an open cell
                    maze[y][x] = CELL

                    # Add the walls around us to the walls list
                    if y != height - 1:
                        if maze[y + 1][x] != CELL:
                            maze[y + 1][x] = WALL
                        if [y + 1, x] not in walls:
                            walls.append([y + 1, x])
                    if x != 0:
                        if maze[y][x - 1] != CELL:
                            maze[y][x - 1] = WALL
                        if [y, x - 1] not in walls:
                            walls.append([y, x - 1])
                    if x != width - 1:
                        if maze[y][x + 1] != CELL:
                            maze[y][x + 1] = WALL
                        if [y, x + 1] not in walls:
                            walls.append([y, x + 1])

                # delete_wall(rand_wall)
                # continue

        # THIS IS WHAT WAS MISSING!
        # You need to remove the wall no matter what -- I wonder even if you
        # need to remove it in each loop
        # ANSWER: You do -- the continue statements will skip it if you don't.
        # Maybe if you let it fall through?
        # ANSWER: Yes, you can let it fall through to here.
        delete_wall(rand_wall)


def make_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == UNVISITED:
                maze[i][j] = WALL


def create_entrance_exit(width, height):
    for i in range(0, width):
        if maze[1][i] == CELL:
            maze[0][i] = CELL
            break
    for i in range(width - 1, 0, -1):
        if maze[height - 2][i] == CELL:
            maze[height - 1][i] = CELL
            break


height = 11
width = 27
maze = init_maze(width, height)

# Changed this so we guarantee a number between 1 and height-1
starting_height = int(random.random() * (height - 2)) + 1
starting_width = int(random.random() * (width - 2)) + 1
maze[starting_height][starting_width] = CELL

walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])
maze[starting_height - 1][starting_width] = WALL
maze[starting_height][starting_width - 1] = WALL
maze[starting_height][starting_width + 1] = WALL
maze[starting_height + 1][starting_width] = WALL

print_maze(maze)

create_maze_old()
make_walls(width, height)
create_entrance_exit(width, height)
print_maze(maze)
