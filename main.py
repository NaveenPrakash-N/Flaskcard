from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# read csv
try:
    data=pandas.read_csv('data/words_to_learn.csv')
except:
    data= pandas.read_csv('data/french_words.csv')
csv_dict=data.to_dict(orient='records')
current_card={}

# functions
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(csv_dict)
    canvas.itemconfig(word, text='French',fill='black')
    canvas.itemconfig(f_word,text=current_card['French'],fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(word,text='English',fill = 'white')
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(f_word, text=current_card['English'],fill = 'white')

def is_known():
    csv_dict.remove(current_card)
    new_dict = pandas.DataFrame.from_dict(csv_dict)
    new_dict.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer = window.after(3000, flip_card)
# images
wrong_mark = PhotoImage(file='images/wrong.png')
right_mark = PhotoImage(file='images/right.png')
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

# UI
canvas = Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image=canvas.create_image(400,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
word = canvas.create_text(400,150,text='',font=("Ariel",40,'italic'))
f_word = canvas.create_text(400,263,text='',font=("Ariel",60,'bold'))

wrong_mark_button = Button(image=wrong_mark, highlightthickness=0, command=next_card)
wrong_mark_button.grid(row=1,column=0)

right_mark_button = Button(image=right_mark, highlightthickness=0, command=is_known)
right_mark_button.grid(row=1,column=1)

next_card()

window.mainloop()