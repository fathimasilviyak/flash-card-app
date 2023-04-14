import random
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card['French'])


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
right_button_img = PhotoImage(file="images/right.png")
left_button_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)
left_button = Button(image=left_button_img, highlightthickness=0, command=next_card)
left_button.grid(row=1, column=1)

next_card()

window.mainloop()
