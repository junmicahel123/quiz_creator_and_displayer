###
#START

#LOAD questions from 'quiz_creator_data_.txt'
#PARSE each block into:
#    - question text
 #   - 4 choices
  #  - correct answer (a–d)

#WHILE questions remain:
 #   SELECT a random question
  #  REMOVE it from the pool
   ##WAIT for user's answer

   # IF answer is correct:
    #    SHOW "Correct!"
 #   ELSE:
#        SHOW "Incorrect!" and the correct answer

#HOW "All questions answered" when done



##########
import tkinter as tk
from tkinter import messagebox
import random

def load_questions():
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
        messagebox.showerror("Error", "quiz_creator_data_.txt not found.")
        return []

def ask_question():
    global current_question
    if not question_pool:
        messagebox.showinfo("Done", "You've answered all questions!")
        root.destroy()
        return

    current_question = question_pool.pop(0) 

    question_label.config(text=current_question["Question"])
    for i, btn in enumerate(choice_buttons):
        btn.config(text=f"{chr(97+i)}) {current_question['Choices'][i]}", state="normal")


def check_answer(choice_index):
    answer_letter = chr(97 + choice_index)
    if answer_letter == current_question["Correct Answer"]:
        messagebox.showinfo("Result", "✅ Correct!")
    else:
        messagebox.showinfo("Result", f"❌ Incorrect!\nCorrect answer: {current_question['Correct Answer']}) {current_question['Choices'][ord(current_question['Correct Answer']) - 97]}")
    ask_question()

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")
root.configure(bg="#ecf0f1")

question_pool = load_questions()
current_question = {}

question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14, "bold"), bg="#34495e", fg="white", pady=10)
question_label.pack(fill="x", padx=10, pady=20)

choice_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=40, command=lambda idx=i: check_answer(idx), bg="#3498db", fg="white", cursor="hand2")
    btn.pack(pady=5)
    choice_buttons.append(btn)


if question_pool:
     ask_question()
else:
    messagebox.showwarning("Empty", "No questions available in the file.")
    root.destroy()

root.mainloop()