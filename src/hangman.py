import tkinter as tk
from random_word import RandomWords

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.r = RandomWords()
        self.word = self.r.get_random_word().upper()
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
        
def main():
    root = tk.Tk()
    root.title("Hangman Game")
    HangmanGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()
