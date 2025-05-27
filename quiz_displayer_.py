import tkinter as tk
from tkinter import messagebox
import random


class QuizDisplayerWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.root.configure(bg="#ecf0f1")

        self.question_pool = self.load_questions()
        self.current_question = {}

        self.question_label = tk.Label(self.root, text="", wraplength=450, font=("Arial", 14, "bold"),
                                       bg="#34495e", fg="white", pady=10)
        self.question_label.pack(fill="x", padx=10, pady=20)

        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 12), width=40,
                            command=lambda idx=i: self.check_answer(idx),
                            bg="#3498db", fg="white", cursor="hand2")
            btn.pack(pady=5)
            self.choice_buttons.append(btn)

        back_btn = tk.Button(self.root, text="↩️ Back to Main Menu", command=self.back_to_main_menu,
                             bg="#e67e22", fg="white", font=("Arial", 11), width=20)
        back_btn.pack(pady=20)

        if self.question_pool:
            self.ask_question()
        else:
            messagebox.showwarning("Empty", "No questions available in the file.")
            self.root.destroy()

    def run(self):
        self.root.mainloop()

    def load_questions(self):
        try:
            with open("quiz_creator_datas.txt", "r") as file:
                content = file.read().strip().split("\n\n")
                questions = []
                for block in content:
                    lines = block.strip().split("\n")
                    question = lines[0].split(":", 1)[1].strip()
                    choices = [line.split(")", 1)[1].strip() for line in lines[1:5]]
                    correct = lines[5].split(":")[1].strip().lower()
                    questions.append({
                        "Question": question,
                        "Choices": choices,
                        "Correct Answer": correct
                    })
                random.shuffle(questions)
                return questions
        except FileNotFoundError:
            messagebox.showerror("Error", "quiz_creator_datas.txt not found.")
            return []

    def ask_question(self):
        if not self.question_pool:
            messagebox.showinfo("Done", "You've answered all questions!")
            self.root.destroy()
            return

        self.current_question = self.question_pool.pop(0)

        self.question_label.config(text=self.current_question["Question"])
        for i, btn in enumerate(self.choice_buttons):
            btn.config(
                text=f"{chr(97+i)}) {self.current_question['Choices'][i]}",
                state="normal"
            )

    def check_answer(self, choice_index):
        answer_letter = chr(97 + choice_index)
        if answer_letter == self.current_question["Correct Answer"]:
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            correct_letter = self.current_question["Correct Answer"]
            correct_text = self.current_question["Choices"][ord(correct_letter) - 97]
            messagebox.showinfo("Result", f"❌ Incorrect!\nCorrect answer: {correct_letter}) {correct_text}")
        self.ask_question()

    def back_to_main_menu(self):
        self.root.destroy()
        