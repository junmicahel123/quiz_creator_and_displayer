# 
# import tkinter
    # import quiz creator
    # import quiz displayer
#initialize Class 
    # def initialization of roots for gui
    # def for quiz creator
    # def for quiz displayer

import tkinter as tk
from quiz_creator_ import QuizCreatorWindow
from quiz_displayer_ import QuizDisplayerWindow

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.geometry("300x200")
        
        tk.Label(self.root, text="Choose an option:", font=("Arial", 14)).pack(pady=20)
        
        tk.Button(self.root, text="Quiz Creator", command=self.open_quiz_creator, width=20).pack(pady=5)
        tk.Button(self.root, text="Quiz Displayer", command=self.open_quiz_displayer, width=20).pack(pady=5)
        
        self.root.mainloop()

    def open_quiz_creator(self):
        self.root.destroy()
        QuizCreatorWindow().run()


    def open_quiz_displayer(self):
        self.root.destroy()
        QuizDisplayerWindow().run()

if __name__ == "__main__":
    MainMenu()