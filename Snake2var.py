from tkinter import *

game_width = 500
game_height = 500
snake_item = 10
snake_color1 = "red"
snake_color2 = "yellow"
snake_x = 24
snake_y = 24
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 5

tk = Tk()
tk.title("Snake")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item, fill=snake_color1)
    id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item + snake_item - 2, fill=snake_color1)
    snake_list.append([x, y, id1, id2])
    #print(snake_list)


snake_paint_item(canvas, snake_x, snake_y)


def coolling_with_a_wall(snake_x, snake_y, game_width, game_height):

    if snake_x < 0 or snake_y < 0:
        tk.destroy()
    elif snake_x  > 49 or snake_y > 49:
        tk.destroy()


def check_can_we_delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def snake_move(event):
    global snake_x
    global snake_y
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    coolling_with_a_wall(snake_x, snake_y, game_width, game_height)
    snake_paint_item(canvas, snake_x, snake_y)




canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

tk.mainloop()
