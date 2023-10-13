import tkinter as tk
from random_word import RandomWords
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.r = RandomWords()
        self.word = self.r.get_random_word().upper()
        print(self.word)
        self.guesses_left = 6
        self.display_word = ["_"] * len(self.word)
        self.previous_guesses = []
        
        self.canvas = tk.Canvas(root, width=200, height=250)
        self.canvas.pack()
        
        self.word_label = tk.Label(root, text=" ".join(self.display_word), font=("Arial", 24))
        self.word_label.pack()
        
        self.guess_label = tk.Label(root, text="Guesses left: " + str(self.guesses_left), font=("Arial", 18))
        self.guess_label.pack()
        
        self.input_entry = tk.Entry(root, font=("Arial", 18))
        self.input_entry.pack()
        
        self.submit_button = tk.Button(root, text="Submit Guess",command=" ", font=("Arial", 18))
        self.submit_button.pack()
        
        self.previous_guesses_label = tk.Label(root, text="Previous Guesses:", font=("Arial", 18))
        self.previous_guesses_label.pack()
        
        self.guesses_text = tk.Text(root, height=10, width=15, font=("Arial", 18))
        self.guesses_text.pack()
        
        #Initial Hangman Setting
        self.canvas.create_line(20, 220, 180, 220, width=2) #Floor
        self.canvas.create_line(90, 220, 90, 30, width=2)   #Pole
        self.canvas.create_line(90, 30, 150, 30, width=2)   #Ceiling
        self.canvas.create_line(150, 30, 150, 60, width=2)  #Rope
        
    def check_guess(self):    
        guess = self.input_entry.get().strip().upper()
        self.input_entry.delete(0, tk.END)
        if not guess or guess.isspace():
            messagebox.showinfo("Hangman", "Invalid choice! Please enter a valid letter.")
            return
        elif guess in self.previous_guesses:
            messagebox.showinfo("Hangman", "You already guessed that letter!")
            return
        
        self.previous_guesses.append(guess)
        self.guesses_text.insert(tk.END, guess + "\n")
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.display_word[i] = guess
            self.word_label.config(text=" ".join(self.display_word))
        else:
            self.guesses_left -= 1
            self.draw_hangman()
    def draw_hangman(self):
        self.canvas.create_oval(140, 60, 160, 80, width=2)  #Head
        self.canvas.create_line(150, 80, 150, 130, width=2) #body
        self.canvas.create_line(150, 90, 130, 110, width=2) #Larm
        self.canvas.create_line(150, 90, 170, 110, width=2) #Rarm
        self.canvas.create_line(150, 130, 130, 150, width=2) #Lleg
        self.canvas.create_line(150, 130, 170, 150, width=2) #Rleg
        
def main():
    root = tk.Tk()
    root.title("Hangman Game")
    HangmanGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()
