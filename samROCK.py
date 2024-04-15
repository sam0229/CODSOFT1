import tkinter as tk
import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create buttons for user's choice
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI
root.mainloop()
