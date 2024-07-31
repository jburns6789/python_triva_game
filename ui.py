from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain # <----- quiz brain object

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("425x600")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.score_label.grid(row=0, column=1, pady=20, sticky=E)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="quiz_brain.next_question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")) #<---- have to give a center postion of the canvas location, half of canvas width and height.
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.t_button = Button(self.window, image=true_img, command=self.true_click, highlightthickness=0)
        self.t_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.f_button = Button(image=false_img, command=self.false_click, highlightthickness=0)
        self.f_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_click(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




