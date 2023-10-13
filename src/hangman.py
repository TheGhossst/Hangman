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
    def draw_hangman(self):
def main():
    root = tk.Tk()
    root.title("Hangman Game")
    HangmanGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()
