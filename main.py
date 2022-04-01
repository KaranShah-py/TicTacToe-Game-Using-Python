from tkinter import *
from tkinter.font import *
from random import *

# Basic window and other stuff
root = Tk()
root.geometry('1400x1000')
root.title('Tic Tac Toe')
root.config(bg='#00004d')
root.minsize(width=1400, height=1000)
root.maxsize(width=1400, height=1000)

box_number_selected = StringVar()
global box_numbers
box_numbers = ['1','2','3','4','5','6','7','8','9']
box_number_selected.set(box_numbers[0])

player_1_moves = []
player_2_moves = []

global checkifx
checkifx = 0

global checkify
checkify = 0 

global last_number
last_number = 0

global count
count = 0

# funtions
# This function will check if the player which is using x is winning or not
def check_if_x_is_the_winner():
    global player_1_moves
    solutions = ['123', '456', '789', '147', '258', '369', '159', '357']
    player_1_moves.sort()

    if len(player_1_moves) == 3:
        temp_str = player_1_moves[0] + player_1_moves[1] + player_1_moves[2]
        if temp_str in solutions:
            result_label.config(text='PLAYER 1 IS THE \n WINNER')
            x_button.config(state=DISABLED)
            y_button.config(state=DISABLED)
        else:
            pass
    if len(player_1_moves) == 4:
        temp_str1 = player_1_moves[0] + player_1_moves[1] + player_1_moves[2]
        temp_str2 = player_1_moves[0] + player_1_moves[2] + player_1_moves[3]
        temp_str3 = player_1_moves[0] + player_1_moves[1] + player_1_moves[3]
        temp_str4 = player_1_moves[1] + player_1_moves[2] + player_1_moves[3]
        
        compare_x_moves = list()
        compare_x_moves.append(temp_str1)
        compare_x_moves.append(temp_str2)
        compare_x_moves.append(temp_str3)
        compare_x_moves.append(temp_str4)

        if (compare_x_moves[0] in solutions) or (compare_x_moves[1] in solutions) or (compare_x_moves[2] in solutions) or (compare_x_moves[3] in solutions):
            result_label.config(text='PLAYER 1 IS THE \n WINNER')
            x_button.config(state=DISABLED)
            y_button.config(state=DISABLED)

        elif (compare_x_moves[0] not in solutions) and (compare_x_moves[1] not in solutions) and (compare_x_moves[2] not in solutions) and (compare_x_moves[3] not in solutions):
           global checkifx
           checkifx = 1

# This function will check if the player which uses 0 is the winning or not.
def check_if_0_is_the_winner():
    global player_2_moves
    solutions = ['123', '456', '789', '147', '258', '369', '159', '357']
    player_2_moves.sort()
    if len(player_2_moves) == 3:
        temp_str = player_2_moves[0] + player_2_moves[1] + player_2_moves[2]
        if temp_str in solutions:
            result_label.config(text='PLAYER 2 IS THE \n WINNER')
            x_button.config(state=DISABLED)
            y_button.config(state=DISABLED)
        else:
            pass

    if len(player_2_moves) == 4:
        temp_str1 = player_2_moves[0] + player_2_moves[1] + player_2_moves[2]
        temp_str2 = player_2_moves[0] + player_2_moves[2] + player_2_moves[3]
        temp_str3 = player_2_moves[0] + player_2_moves[1] + player_2_moves[3]
        temp_str4 = player_2_moves[1] + player_2_moves[2] + player_2_moves[3]

        compare_y_moves = list()
        compare_y_moves.append(temp_str1)
        compare_y_moves.append(temp_str2)
        compare_y_moves.append(temp_str3)
        compare_y_moves.append(temp_str4)

        if (compare_y_moves[0] in solutions) or (compare_y_moves[1] in solutions) or (compare_y_moves[2] in solutions) or (compare_y_moves[3] in solutions):
            result_label.config(text='PLAYER 2 IS THE \n WINNER')
            x_button.config(state=DISABLED)
            y_button.config(state=DISABLED)
        elif (compare_y_moves[0] not in solutions) and (compare_y_moves[1] not in solutions) and (compare_y_moves[2] not in solutions) and (compare_y_moves[3] not in solutions):
            global checkify
            checkify = 1

def final_round_checking():
    if last_number == '1':
        text_box1.config(text='X', fg='#f535aa')
    elif last_number == '2': 
        text_box2.config(text='X', fg='#f535aa')
    elif last_number == '3':
        text_box3.config(text='X', fg='#f535aa')
    elif last_number == '4':
        text_box4.config(text='X', fg='#f535aa')
    elif last_number == '5':
        text_box5.config(text='X', fg='#f535aa')
    elif last_number == '6':
        text_box6.config(text='X', fg='#f535aa')
    elif last_number == '7':
        text_box7.config(text='X', fg='#f535aa')
    elif last_number == '8':
        text_box8.config(text='X', fg='#f535aa')
    else:
        text_box9.config(text='X', fg='#f535aa')

    solutions = ['123', '456', '789', '147', '258', '369', '159', '357']
    flag = 0   # for comaparison
    player_1_moves.sort()
    if len(player_1_moves) == 5:
        for i in range(0,3):
            if flag == 1:
                break
            for j in range(i+1,4):
                if flag == 1:
                    break
                for k in range(j+1,5):
                    temp_str = player_1_moves[i] + player_1_moves[j] + player_1_moves[k]
                    
                    if temp_str in solutions:
                        flag = 1
                        break
                    else:
                        flag = 0
                temp_str = ''
        if flag == 1:
            result_label.config(text='PLAYER 1 IS THE WINNER')
        else:
            result_label.config(text='IT\'S A TIE')

    

def delete_from_options():
    box_numbers.remove(box_number_selected.get())
    select_box = OptionMenu(root,box_number_selected, *box_numbers)
    select_box.place(x=200, y=200)
    box_number_selected.set(choice(box_numbers))

def put_x(): 
    if box_number_selected.get() == '1':
        text_box1.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '2':
        text_box2.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '3':
        text_box3.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '4':
        text_box4.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '5':
        text_box5.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '6':
        text_box6.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '7':
        text_box7.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '8':
        text_box8.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()

    else:
        text_box9.config(text='X', fg='#f535aa')
        player_1_moves.append(box_number_selected.get())
        delete_from_options()
    x_button.config(state=DISABLED)
    y_button.config(state=NORMAL)
    
    if len(player_1_moves) > 2:
        check_if_x_is_the_winner()


def put_y():
    global count 
    count = count + 1
    global last_number
    if box_number_selected.get() == '1':
        text_box1.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '2':
        text_box2.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '3':
        text_box3.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '4':
        text_box4.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '5':
        text_box5.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '6':
        text_box6.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '7':
        text_box7.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    elif box_number_selected.get() == '8':
        text_box8.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()

    else:
        text_box9.config(text='0', fg='#39ff14')
        player_2_moves.append(box_number_selected.get())
        delete_from_options()
    x_button.config(state=NORMAL)
    y_button.config(state=DISABLED)

    if len(player_2_moves) > 2:
        check_if_0_is_the_winner()

    if count == 4:
        player_1_moves.append(box_numbers[0])
        last_number = player_1_moves[4]
        final_round_checking()
        x_button.config(state=DISABLED)
        y_button.config(state=DISABLED)
    
# Defining of the widgets 
my_canva = Canvas(root, width=600, height=600, bg='#00004d', borderwidth=0, relief=GROOVE)
my_canva.create_line(200, 10, 200, 590, fill='White', smooth=1, width=10)
my_canva.create_line(400, 10, 400, 590, fill='White', smooth=1, width=10)
my_canva.create_line(10, 200, 590, 200, fill='White', smooth=1, width=10)
my_canva.create_line(10, 400, 590, 400, fill='White', smooth=1, width=10)

x_button = Button(root, text='X', bg='#00004d', fg='White', font=('Helvetica', 20, BOLD), borderwidth=0, relief=GROOVE, padx=20, pady=20, command=put_x)
y_button = Button(root, text='0', bg='#00004d', fg='White', font=('Helvetica', 20, BOLD), borderwidth=0, relief=GROOVE, pady=20, padx=20, command=put_y, state=DISABLED)

text_box1 = Label(my_canva,text='1', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box2 = Label(my_canva,text='2', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box3 = Label(my_canva,text='3', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box4 = Label(my_canva,text='4', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box5 = Label(my_canva,text='5', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box6 = Label(my_canva,text='6', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box7 = Label(my_canva,text='7', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box8 = Label(my_canva,text='8', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))
text_box9 = Label(my_canva,text='9', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))

select_box_l = Label(root,text='Select Box \n Number', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 12, BOLD))
select_box = OptionMenu(root,box_number_selected, *box_numbers)
player_1 = Label(root,text='Player 1 : X', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 15, BOLD))
player_2 = Label(root,text='Player 2 : 0', bg='#00004d', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 15, BOLD))

x_and_0 = Label(root,text='TIC  TAC  TOE', bg='#000033', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 30, BOLD))

global result_label
result_label = Label(root,text='', bg='#000033', fg='White', borderwidth=0, relief=GROOVE, font=('Helvetica', 15, BOLD))

# Putting them on the screen
my_canva.pack(pady=100)

select_box_l.place(x=100, y=200)
select_box.place(x=200, y=200)
result_label.place(x=100, y=400)

x_and_0.place(x=560, y=20)
player_1.place(x=100, y=20)
player_2.place(x=100, y=60)

x_button.place(x=1100, y=200)
y_button.place(x=1100, y=400)

text_box1.place(x=85, y=85)
text_box2.place(x=285, y=85)
text_box3.place(x=485, y=85)
text_box4.place(x=85, y=285)
text_box5.place(x=285, y=285)
text_box6.place(x=485, y=285)
text_box7.place(x=85, y=485)
text_box8.place(x=285, y=485)
text_box9.place(x=485, y=485)

# Mainloop
root.mainloop()