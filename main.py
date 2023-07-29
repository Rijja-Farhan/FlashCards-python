#----imports
from tkinter import *
import pandas
import random
import csv
BACKGROUND_COLOR = "#B1DDC6"
new_word ={}
try:
    data = pandas.read_csv("./data/learn_this.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    word_data = data.to_dict(orient="records")

#-----generating random word
def random_words():
    global new_word,flip
    window.after_cancel(flip)
    new_word = random.choice(word_data)
    canvas.itemconfig(image,image=front_image)
    canvas.itemconfig(title,text ="French",fill="black")
    canvas.itemconfig(word,text =new_word["French"],fill="black")
    flip= window.after(3000, flip_card)



#----flipping the cards

def flip_card():
    global new_word
    canvas.itemconfig(image,image=back_image)
    canvas.grid(column=0,row=0,columnspan=2)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=new_word["English"],fill="white")


def word_leared():
    word_data.remove(new_word)
    new_data= pandas.DataFrame(word_data)
    new_data.to_csv("./data/learn_this.csv")
    random_words()








#----setting up the UI
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg =BACKGROUND_COLOR)

canvas =Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)


front_image = PhotoImage(file="./images/card_front.png")
image=canvas.create_image(400, 263, image=front_image)
back_image = PhotoImage(file="./images/card_back.png")
canvas.grid(column=0,row=0,columnspan=2)

title = canvas.create_text(400, 150, text="Title", font=("Arial", 14, "italic"))
word= canvas.create_text(400, 200, text="Word", font=("Arial", 14, "bold"))



wrong_image=PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command= random_words)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command= word_leared)
right_button.grid(column=1,row=1)
flip = window.after(3000, flip_card)
random_words()

window.mainloop()
