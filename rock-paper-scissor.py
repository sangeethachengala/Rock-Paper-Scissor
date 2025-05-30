import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result.set("It's a Draw!")
        result_label.config(fg="blue")
    elif (choice == "Rock" and computer_choice == "Scissor") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissor" and computer_choice == "Paper"):
        result.set("You Win!")
        result_label.config(fg="green")
    else:
        result.set("You Lose!")
        result_label.config(fg="red")

    computer_label.config(text=f"Computer: {computer_choice}",fg="purple")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("600x300")
root.configure(bg="pink")  

result = tk.StringVar()
result.set("Choose Rock, Paper or Scissor")

# Computer choice 
computer_label = tk.Label(
    root, text="Computer: ?", font=("Arial", 20, "bold"), bg="pink", fg="brown"
)
computer_label.pack(pady=30)

# Result label
result_label = tk.Label(
    root, textvariable=result, font=("Arial", 24, "bold"), bg="pink"
)
result_label.pack(pady=20)

# Buttons
buttons_frame = tk.Frame(root, bg="pink")
buttons_frame.pack()

colors = {"Rock": "#ff9999", "Paper": "#99ccff", "Scissor": "#b3ffb3"}

for choice in ["Rock", "Paper", "Scissor"]:
    tk.Button(
        buttons_frame,
        text=choice,
        command=lambda c=choice: play(c),
        width=10,
        height=2,
        bg=colors[choice],
        fg="black",
        activebackground="#cccccc",
        font=("Arial", 14, "bold")
    ).pack(side=tk.LEFT, padx=10, pady=20)

root.mainloop()

