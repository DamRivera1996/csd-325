"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # <-- NEW: water/lake character

# Settings:
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    addLake(forest)  # <-- NEW: add the lake
    bext.clear()

    while True:
        displayForest(forest)
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                # Skip the lake so it’s never modified
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            # Fire does NOT spread across water
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def addLake(forest):
    """Add a fixed lake roughly in the center of the display."""
    lake_width = 15
    lake_height = 6
    start_x = (WIDTH // 2) - (lake_width // 2)
    start_y = (HEIGHT // 2) - (lake_height // 2)

    for x in range(start_x, start_x + lake_width):
        for y in range(start_y, start_y + lake_height):
            forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            tile = forest[(x, y)]
            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif tile == WATER:
                bext.fg('blue')  # <-- Blue lake display
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print(f"Grow chance: {GROW_CHANCE * 100:.1f}%  ", end='')
    print(f"Lightning chance: {FIRE_CHANCE * 100:.1f}%  ", end='')
    print("Press Ctrl-C to quit.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
