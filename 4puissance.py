from sense_hat import SenseHat
from time import sleep
from A4i import A4i
from random import randint

sense = SenseHat()
sense.clear()
sense.low_light = True

ai = A4i(True, False)

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [127, 127, 0]
cyan = [0, 127, 127]
magenta = [127, 0, 127]

white = [255, 255, 255]
low_white = [160, 140, 180]
off = [0, 0, 0]

global player
player = 0
global player_color
player_color = [red, green]

x = randint(0,3)
if x == 2:
    player_color = [yellow, cyan]
elif x == 1:
    player_color = [magenta, blue]
elif x == 0:
    player_color = [red, green]


global selected
selected = 0
preview = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

global taille
taille = [0, 0, 0, 0, 0, 0, 0, 0]
grid = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
global p_grid
p_grid = [[-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1]]

global running
running = True


def reset():
    global p_grid
    global taille
    global player
    global player_color

    sense.clear()

    x = randint(0, 4)
    if x == 2:
        player_color = [yellow, cyan]
    elif x == 1:
        player_color = [magenta, blue]
    elif x == 0:
        player_color = [red, green]

    player = 0
    taille = [0, 0, 0, 0, 0, 0, 0, 0]
    p_grid = [[-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1]]


def check_grid():
    for i in range(7):
        for ii in range(5):
            if p_grid[i][ii] == p_grid[i][ii + 1] == p_grid[i][ii + 2] == p_grid[i][ii + 3] != -1:
                return player
    for i in range(4):
        for ii in range(8):
            if p_grid[i][ii] == p_grid[i + 1][ii] == p_grid[i + 2][ii] == p_grid[i + 3][ii] != -1:
                return player
    for i in range(4):
        for ii in range(5):
            if p_grid[i + 3][ii] == p_grid[i + 2][ii + 1] == p_grid[i + 1][ii + 2] == p_grid[i][ii + 3] != -1:
                return player
    for i in range(4):
        for ii in range(5):
            if p_grid[i][ii] == p_grid[i + 1][ii + 1] == p_grid[i + 2][ii + 2] == p_grid[i + 3][ii + 3] != -1:
                return player
    return -1


def grid_to_matrix():
    for i in range(7):
        for ii in range(8):
            if p_grid[i][ii] == 0:
                grid[i][ii] = player_color[0]
            elif p_grid[i][ii] == 1:
                grid[i][ii] = player_color[1]
            else:
                grid[i][ii] = [0, 0, 0]
    matrix = [preview[0], preview[1], preview[2], preview[3], preview[4], preview[5], preview[6], preview[7],
              grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], grid[0][5], grid[0][6], grid[0][7],
              grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], grid[1][5], grid[1][6], grid[1][7],
              grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], grid[2][5], grid[2][6], grid[2][7],
              grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], grid[3][5], grid[3][6], grid[3][7],
              grid[4][0], grid[4][1], grid[4][2], grid[4][3], grid[4][4], grid[4][5], grid[4][6], grid[4][7],
              grid[5][0], grid[5][1], grid[5][2], grid[5][3], grid[5][4], grid[5][5], grid[5][6], grid[5][7],
              grid[6][0], grid[6][1], grid[6][2], grid[6][3], grid[6][4], grid[6][5], grid[6][6], grid[6][7]]
    sense.set_pixels(matrix)


def preview_selection(left):
    global selected
    if left: selected = (selected - 1) % 8
    else: selected = (selected + 1) % 8
    for i in range(8):
        if i == selected:
            preview[i] = player_color[player]
        else:
            preview[i] = off
    grid_to_matrix()


def left():
    preview_selection(True)


def right():
    preview_selection(False)


def ok():
    global player
    global running
    global taille
    if taille[selected] < 7:
        hauteur = (6 - taille[selected])
        p_grid[hauteur][selected] = player
        taille[selected] += 1
        grid_to_matrix()

        if check_grid() != -1:
            phrase = "Player " + str(player) + " won !"
            sense.show_message(phrase, 0.08, player_color[player], [30, 30, 30])
            sense.clear(player_color[player])
            running = False
        else:
            player = (player + 1) % 2
            if ai.activated and player == 1:
                x_ai = ai.play(p_grid, taille)
                hauteur = (6 - taille[x_ai])
                p_grid[hauteur][x_ai] = player
                taille[x_ai] += 1
                if check_grid() != -1:
                    grid_to_matrix()
                    sleep(1.1)
                    sense.show_message("You lost !", 0.06, player_color[0], [30, 0, 0])
                    running = False
                else:
                    player = (player + 1) % 2
                    grid_to_matrix()
            else:
                preview[selected] = player_color[player]
                grid_to_matrix()


def main():
    preview_selection(False)
    while running:

        for event in sense.stick.get_events():
            # print("joystick was {} {}".format(event.action, event.direction))
            if event.direction == 'up' and event.action == 'pressed':
                ok()
            elif event.direction == 'down' and event.action == 'pressed':
                ok()
            elif event.direction == 'left' and event.action == 'pressed':
                left()
            elif event.direction == 'right' and event.action == 'pressed':
                right()


while True:
    running = True
    sense.show_message("puissance4", 0.05, [127, 0, 127], [0, 0, 0])
    main()
    sleep(0.2)
    reset()
