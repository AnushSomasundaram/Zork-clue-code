from tkinter import *
from PIL import ImageTk, Image
from board import *
#from main_game import *
from player import *
root = Tk()

#Title Definition and Title logo 
root.title('Zork-Clue')
moveto = ' '
new_board = Board()
user_name=(" ")
new_board = Board()


'''
#Map Image
map_path = r"map.jpg"
global map_image
map_image = ImageTk.PhotoImage(Image.open(map_path))
map_label = Label(root, image=map_image)


#Intro Image

intro_path = r"mansion.jpg"
global intro_image
intro_image = ImageTk.PhotoImage(Image.open(intro_path))
my_label = Label(root, image=intro_image)
'''


def movement(player):

    #moveto = (input("Which way do you want to move:- "))
    moveto_gui_label = Label(root, text = "Which way do you want to move:- ")
    moveto_gui_input = Entry(root, borderwidth=8)
    moveto_gui_label.pack()
    moveto_gui_input.pack()
    
    if moveto == "mr":
        new_board.moveright(player)
        new_board.current_room(player)        
        
    elif moveto == "ml" :
        new_board.moveleft(player)
        new_board.current_room(player) 
        
    elif moveto == "mu" :
        new_board.moveup(player)     
        new_board.current_room(player)    

    elif moveto == "md" :
        new_board.movedown(player)  
        new_board.current_room(player)    
    else:
        moveto_invalid_label = Label(root, text = "invalid move")
        moveto_invalid_label.pack()
        new_board.current_room(player)

def objective_loop(player):
    print(weapon_position)
    found=0
    while found==0:
        
        if str(Board.board[player.x][player.y]) != str(weapon_position):
            movement(p1)
            found=0
        else:
            found=1

    game_found_label = Label(root, text = "You have found the weapon. Now the lunatic can be convicted.")
    game_found_label.pack()

intro_gui_label = Label(root, text = """Welcome to Manor Mansions, the heart of this town. It's the residence of the mayor of this town. \n
Unfortunately the towns mental asylum had a security breach, one of the lunatics got out and killed the mayor's dog with a candle stick.\n
The killer has been caught but cannot be convicted until the murder weapon is found, according to interpol it's still in one of the rooms inside the mansion.\n
Help the mayor's dog get his justice by helping them find the weapon.""")

intro2_gui_label = Label(root, text = "\nYou have Entered the Mansion\n")

intro3_gui_label = Label(root, text = """\nThis is the The map of the Mansion.\n
You have Entered through the Foyer and are currently standing on the J3 tile""")

intro4_gui_label = Label(root, text = """To move up type in 'mu'\n
To move down type in 'md'\n
To move left type in 'ml'\n
To move right type in 'mr'\n""")



def intro1():
    #my_label.pack()
    intro_gui_label.pack()
    user_name_label.pack()
    user_name_input.pack()
    username_confirm.pack()
    username_confirm.pack()
    intro1_next_button.pack()

def intro2():
    intro1_delete()
    intro2_gui_label.pack()
    #map_label.pack()
    intro3_gui_label.pack()
    intro2_next_button.pack()

def intro_movement():
    intro2_delete()
    moveto_gui_label.pack()
    intro4_gui_label.pack()
    moveto_gui_input.pack()
    intro4_next_button.pack()
    objective_loop(p1)
    #intro_movement_text.pack()

def intro1_delete():
    #my_label.pack_forget()
    intro_gui_label.pack_forget()
    intro1_next_button.pack_forget()
    user_name_label.pack_forget()
    user_name_input.pack_forget()
    

def intro2_delete():
    intro2_gui_label.pack_forget()
    #map_label.pack_forget()
    intro3_gui_label.pack_forget()
    intro2_next_button.pack_forget()

def get_username():
    user_name = user_name_input.get()
    username_confirm.pack_forget()
    #just code for seeing if name is collected
    #user_name_display = Label(root, text = user_name)
    #user_name_display.pack()

def get_direction():
    moveto = moveto_gui_input.get()
    # = Label(root, text = moveto)
    #moto_check_label.pack()
    #intro4_gui_label.pack_forget()  


'''
def main_game_intro_gui():
    user_name_label.pack()
    user_name_input.pack()
    #user_name_button.pack()

def username_gui_del():
    user_name_label.pack_forget()
    user_name_input.pack_forget()
    #user_name_button.pack_forget()
'''
#run this command first in gui and clear the screen
user_name_label = Label(root,text = "To play, please enter your name :- ")
user_name_input = Entry(root, borderwidth = 8)
user_name=user_name_input.get()
p1=Player(user_name)
new_board.addPlayer(p1)
trial = Label(root, text = user_name)
#user_name_input.bind("<Return>")
#user_name_button = Button(root, text="Next ->",padx=45, pady=20, command = username_gui_del)
moveto_gui_label = Label(root, text = "Which way do you want to move:- ")
moveto_gui_input = Entry(root, borderwidth=8)


intro1_next_button = Button(root, text="Next ->",padx=45, pady=20, command = intro2)
intro2_next_button = Button(root, text="Next ->",padx=45, pady=20, command = intro_movement)
intro4_next_button = Button(root, text="Next ->",padx=45, pady=20, command = get_direction) 
username_confirm = Button(root, text = "Confirm  Username ", command = get_username)

#intro_movement_text = Entry(root, borderwidth=8)



intro1()
#movement(p1)

root.mainloop()