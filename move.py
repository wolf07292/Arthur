import tkinter
import random
from tkinter import PhotoImage


def prepare_and_start():
    global player
    
    canvas.delete("all")
    player_pos = (random.randint(1, N_Y - 1) * step,random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    label.config(text="Найди выход")
    master.bind("<KeyPress>", key_pressed)

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <=0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >= HEIGHT:
        canvas.move(obj, 0, -HEIGHT)


def key_pressed(event):
    if event.keysym =='Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'Down':
        move_wrap(player, 0 , step)
    elif event.keysym == 'Right':
        move_wrap(player, step, 0)
    elif event.keysym == 'left':
        move_wrap(player, -step, 0)
