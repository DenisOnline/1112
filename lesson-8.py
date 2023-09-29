# import tkinter as tk
#
# root = tk.Tk()
# root.title("First Window")
# root.geometry('600x400')
# root.iconbitmap('icon.ico')
# # root.resizable(False, False)
# root.minsize(400, 300)
# root.maxsize(800, 600)
#
# label_1 = tk.Label(master=root,
#                    text="Hello",
#                    font=("Vollkorn", 20, "bold"),
#                    bg="red",
#                    fg="yellow",
#                    width=10,
#                    height=3,
#                    # padx=65,
#                    # pady=30,
#                    anchor="e",
#                    relief=tk.RAISED,
#                    bd=10,
#                    justify=tk.LEFT)
# label_1.pack()
#
# root.mainloop()


import tkinter as tk

bomb = 100
score = 0
press_return = True

root = tk.Tk()
root.title("Game")
root.geometry("600x600")
root.iconbitmap("bomb.ico")

label = tk.Label(root,
                 text='Press [enter] to start the game',
                 font=('Comic Sans MS', 12))
fuse_label = tk.Label(root,
                      text=f'Fuse: {str(bomb)}',
                      font=('Comic Sans MS', 14))
score_label = tk.Label(root,
                       text=f'Score: {str(score)}',
                       font=('Comic Sans MS', 14))
label.pack()
fuse_label.pack()
score_label.pack()

img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()


def update_display():
    pass


def is_alive():
    pass


def update_bomb():
    pass


def update_score():
    pass


def start(event):
    pass


def click():
    pass


click_button = tk.Button(root,
                         text='Click me',
                         bg='black',
                         fg='white',
                         width=15,
                         font=('Comic Sans MS', 14),
                         command=click)
click_button.pack()
root.bind('<Return>', start)

root.mainloop()
