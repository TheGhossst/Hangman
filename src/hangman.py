#https://github.com/TheGhossst
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
        
        self.submit_button = tk.Button(root, text="Submit Guess",command=self.check_guess, font=("Arial", 18))
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
        
        self.reveal_free_character() 
    
    #Reveal a character    
    def reveal_free_character(self):
        hidden_indices = []
        for i, char in enumerate(self.display_word):      
            if char == "_":
                hidden_indices.append(i)
                
        if hidden_indices:
            index_to_reveal = hidden_indices[0]
            self.display_word[index_to_reveal] = self.word[index_to_reveal]
            self.word_label.config(text=" ".join(self.display_word))
            self.previous_guesses.append(self.word[index_to_reveal])
            self.guesses_text.insert(tk.END, self.word[index_to_reveal] + "\n")
    #Check user guess       
    def check_guess(self):    
        guess = self.input_entry.get().strip().upper()
        if len(guess) != 1:
            messagebox.showinfo("Hangman", "Invalid choice! Please enter a valid letter.")
            self.input_entry.delete(0, tk.END)
            return
        self.input_entry.delete(0, tk.END)
        
        if not guess or guess.isspace() or guess.isdigit():
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
        
        if "_" not in self.display_word:
            self.word_label.config(text="You win! The word was " + self.word)
            self.input_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
        elif self.guesses_left == 0:
            self.word_label.config(text="Game over! The word was " + self.word)
            self.input_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
        else:
            self.guess_label.config(text="Guesses left: " + str(self.guesses_left))
    
    def draw_hangman(self):
        if self.guesses_left == 5:  self.canvas.create_oval(140, 60, 160, 80, width=2)  # Head
        elif self.guesses_left == 4:  self.canvas.create_line(150, 80, 150, 130, width=2)  # Body
        elif self.guesses_left == 3:  self.canvas.create_line(150, 90, 130, 110, width=2)  # Larm
        elif self.guesses_left == 2:  self.canvas.create_line(150, 90, 170, 110, width=2)  # Rarm
        elif self.guesses_left == 1:  self.canvas.create_line(150, 130, 130, 150, width=2)  # Lleg
        elif self.guesses_left == 0:
            self.canvas.create_line(150, 130, 170, 150, width=2)  # Rleg
            self.word_label.config(text="Game over! The word was " + self.word)
            self.input_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
        
def main():
    root = tk.Tk()
    root.title("Hangman Game")
    HangmanGame(root)
    root.mainloop()
    
#call main()
if __name__ == "__main__":
    main()
