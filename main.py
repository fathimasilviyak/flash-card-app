from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="langage",  font=("arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
right_button_img = PhotoImage(file="images/right.png")
left_button_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(row=1, column=0)
left_button = Button(image=left_button_img, highlightthickness=0)
left_button.grid(row=1, column=1)
window.mainloop()