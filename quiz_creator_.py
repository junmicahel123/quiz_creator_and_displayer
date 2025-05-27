# pseudocode
# use def for questionare
    # use while loop for first loop
        # ask for user input
        # ask for question
        # ask for choices
        # ask for the correct answer
# use def to save the data into file
    # use with openn
    #

import tkinter as tk
from tkinter import messagebox


class QuizCreatorWindow:
    def __init__(self):
        self.questions = []

        self.root = tk.Tk()
        self.root.title("Quiz Question Creator")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f4f7")

        header = tk.Label(self.root, text="QUIZ QUESTION CREATOR", font=("Arial", 16, "bold"),
                          bg="#2c3e50", fg="white", pady=10)
        header.pack(fill="x")

        main_frame = tk.Frame(self.root, bg="#f0f4f7", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        tk.Label(main_frame, text="Enter your question:", font=("Arial", 11), bg="#f0f4f7").pack(anchor="w")
        self.question_entry = tk.Entry(main_frame, width=50, font=("Arial", 10))
        self.question_entry.pack(pady=5)

        self.choice_entries = []
        for i in range(4):
            tk.Label(main_frame, text=f"Choice {chr(97 + i)}:", font=("Arial", 11), bg="#f0f4f7").pack(anchor="w")
            entry = tk.Entry(main_frame, width=50, font=("Arial", 10))
            entry.pack(pady=2)
            self.choice_entries.append(entry)

        tk.Label(main_frame, text="Correct answer (a, b, c, d):", font=("Arial", 11),
                 bg="#f0f4f7").pack(anchor="w", pady=(10, 0))
        self.correct_answer = tk.Entry(main_frame, width=5, font=("Arial", 10))
        self.correct_answer.pack(pady=5)

        button_style = {"font": ("Arial", 11), "width": 20, "bd": 0,
                        "relief": "ridge", "cursor": "hand2", "padx": 5, "pady": 5}

        add_btn = tk.Button(main_frame, text="➕ Add Question", command=self.add_question,
                            bg="#27ae60", fg="white", **button_style)
        add_btn.pack(pady=10)

        finish_btn = tk.Button(main_frame, text="💾 Finish & Save", command=self.finish,
                               bg="#2980b9", fg="white", **button_style)
        finish_btn.pack()

        back_btn = tk.Button(main_frame, text="↩️ Back to Main Menu", command=self.back_to_main_menu,
                             bg="#e67e22", fg="white", **button_style)
        back_btn.pack(pady=10)

    def run(self):
        self.root.mainloop()

    def add_question(self):
        question = self.question_entry.get()
        choices = [entry.get() for entry in self.choice_entries]
        correct = self.correct_answer.get().strip().lower()

        if not question or any(not c for c in choices) or correct not in ['a', 'b', 'c', 'd']:
            messagebox.showwarning("Input Error", "Please complete all fields and choose a valid correct answer (a-d).")
            return

        self.questions.append({
            'Question': question,
            'Choices': choices,
            'Correct Answer': correct
        })

        self.question_entry.delete(0, tk.END)
        for entry in self.choice_entries:
            entry.delete(0, tk.END)
        self.correct_answer.delete(0, tk.END)

        messagebox.showinfo("Saved", "Question added!")

    def finish(self):
        if not self.questions:
            messagebox.showwarning("No Questions", "You haven't added any questions yet.")
            return

        with open('quiz_creator_datas.txt', 'w') as file:
            for i, q in enumerate(self.questions, 1):
                file.write(f"Question {i}: {q['Question']}\n")
                file.write(f"   a) {q['Choices'][0]}\n")
                file.write(f"   b) {q['Choices'][1]}\n")
                file.write(f"   c) {q['Choices'][2]}\n")
                file.write(f"   d) {q['Choices'][3]}\n")
                file.write(f"Correct Answer: {q['Correct Answer']}\n\n")

        messagebox.showinfo("Saved", "All questions saved to quiz_creator_datas.txt")
        self.root.destroy()

    def back_to_main_menu(self):
        self.root.destroy()
       
       
