from tkinter import *
import  random
def  next_turn(row,column):
    global  player
    if button[row][column]['text']=='' and winning_game() is False:
        if player ==players[0]:
            button[row][column]['text']=player
            if  winning_game() is False:
                player=players[1]
                label.config(text=(players[1]+" turn"))
            elif winning_game() is True:
                label.config(text=(players[0]+" won"))
            elif winning_game() == "tie":
                label.config(text="tie")
        else:
            button[row][column]['text'] = player
            if winning_game() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif winning_game() is True:
                label.config(text=(players[1] + " won"))
            elif winning_game() == "tie":
                label.config(text="tie")
def  winning_game():
    for row in range(3):
        if button[row][0]['text']==button[row][1]['text']==button[row][2]['text']!='':
            button[row][0].config(bg='green')
            button[row][1].config(bg='green')
            button[row][2].config(bg='green')
            return True
    for coloum in range(3):
        if button[0][coloum]['text']==button[1][coloum]['text']==button[2][coloum]['text']!='':
            button[0][coloum].config(bg='green')
            button[1][coloum].config(bg='green')
            button[2][coloum].config(bg='green')
            return True
    if button[0][0]['text']==button[1][1]['text']==button[2][2]['text']!='':
        button[0][0].config(bg='green')
        button[1][1].config(bg='green')
        button[2][2].config(bg='green')
        return True
    elif button[0][2]['text']==button[1][1]['text']==button[2][0]['text']!='':
        button[0][2].config(bg='green')
        button[1][1].config(bg='green')
        button[2][0].config(bg='green')
        return True
    elif emtpy() is False:
        for row in range(3):
            for coloum in range(3):
                button[row][coloum].config(bg='yellow')
        return 'tie'
    else:
        return False
def emtpy():
    spaces=9
    for row in range(3):
        for coloum in range(3):
            if button[row][coloum]['text']!="":
                spaces-=1
    if spaces ==0:
        return False
    else:
        return True
def new_game():
    global player
    player=random.choice(players)
    label.config(text=player+" turn")
    for row in  range(3):
        for coloum in range(3):
            button[row][coloum].config(text='',bg='#F0F0F0')

window=Tk()
window.title("tik-tak-tok")
players=['X','O']
player=random.choice(players)
button=[[0,0,0],
        [0,0,0],
        [0,0,0]]
label=Label(window,text=player+" turn",font=('consolas',40))
label.pack(side='top')

rest_button=Button(text='reset',font=('consolas',24),command=new_game)
rest_button.pack(side='top')

frame=Frame(window)
frame.pack()

for row in range(3):
    for coloum in range(3):
        button[row][coloum]=Button(frame,text='',font=('consolas',24),width=6,height=2
                                   ,command=lambda row=row,coloum=coloum:next_turn(row,coloum))
        button[row][coloum].grid(row=row,column=coloum)

window.mainloop()