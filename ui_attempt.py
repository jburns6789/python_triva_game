from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("800x600")
        self.window.configure(bg=THEME_COLOR)

        self.score = 0
        self.score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.score.grid(row=0, column=1, pady=20, sticky=E)

        self.text_box = Text(height=25, width=75, padx=20)
        self.text_box.grid(row=1, column=1, rowspan=2, pady=20)

        self.text_label = Label(text="Question", bg=THEME_COLOR, fg="white", font=("Arial", 20, "italic"))
        self.text_label.grid(row=1, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.t_button = Button(self.window, image=self.true_img, command=self.true_click, highlightthickness=0)
        self.t_button.grid(row=3, column=0, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.f_button = Button(image=self.false_img, command=self.false_click, highlightthickness=0)
        self.f_button.grid(row=3, column=2, pady=20)

        self.window.mainloop()

    def true_click(self):
        self.window.text_label.config(text="clicked")

    def false_click(self):
        pass




