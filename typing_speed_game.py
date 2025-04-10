import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

win=tk.Tk()
win.geometry('800x600+400+100')
win.configure(bg='powder blue')
win.title('Typing Speed Increaser Game')
win .iconbitmap('Typing Speed.ico')


words=['Mango','Apple','Jocker','Mobile','Laptop','Door','Bell','Acting','Cauliflower','Sad','Good','Bad','Orange','Lemon','Spanich','Potato','Tomato']

def time():
    global time_left,score,miss,a
    if time_left>=11:
        pass
    else:
        time_label_count.configure(fg='red')
    if time_left>0:
        time_left-=1
        time_label_count.configure(text=time_left)
        time_label_count.after(1000,time)
    else:
        game_play_detail_label.configure(text=f'Hit = {score} | Miss {miss} | Total Score = {score-miss}')
        rr=messagebox.askretrycancel('Notification','For Play Again, Hit Retry Button.')
        if rr:
            score=0
            time_left=60
            miss=0
            time_label_count.configure(fg='blue')
            a=True
            time_label_count.configure(text=time_left)
            word_lable.configure(text=words[0])
            score_lable_count.configure(text=score)

def label_slider():
    global count,slider_words
    text='Welcome To Typing Speed Increaser Game'
    if count>=len(text):
        count=0
        slider_words=''
    slider_words+=text[count]
    count+=1
    font_lable.configure(text=slider_words)
    font_lable.after(150,label_slider)
a=True
def start_game(event=None):
    global score,miss,time_left,a
    
    if time_left!=0:
        if a:
            time()
        a=False
        game_play_detail_label.configure(text='')
        if(word_entry.get()==word_lable['text']):
            score+=1
            score_lable_count.configure(text=score)
        else:
            miss+=1

        # print(word_entry.get())
        random.shuffle(words)
        word_lable.configure(text=words[0])
        word_entry.delete(0,END)







score=0
time_left=60
count=0
slider_words=''
miss=0


font_lable=Label(win,font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
font_lable.place(x=10,y=10)
label_slider()

random.shuffle(words)

word_lable=Label(win,text=words[0],font=('airal',25,'italic bold'),bg='powder blue',fg='black')
word_lable.place(x=390,y=200)

score_lable=Label(win,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue')
score_lable.place(x=10,y=100)

score_lable_count=Label(win,text=score ,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
score_lable_count.place(x=80,y=180)

timer_label=Label(win,text='Time Left' ,font=('airal',25,'italic bold'),bg='powder blue')
timer_label.place(x=600,y=100)

time_label_count=Label(win,text=time_left ,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
time_label_count.place(x=680,y=180)

game_play_detail_label=Label(win,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),bg='powder blue',fg='dark grey')
game_play_detail_label.place(x=120,y=450)




word_entry=Entry(win,font=('airal',25,'italic bold'),bd=10,justify=CENTER)
word_entry.place(x=250,y=300)
word_entry.focus_set()






win.bind('<Return>',start_game)

win.mainloop()