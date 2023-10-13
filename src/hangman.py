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
        
        self.previous_guesses_label = tk.Label(root, text="Previous Guesses:", font=("Arial", 18))
        self.previous_guesses_label.pack()
        
        self.guesses_text = tk.Text(root, height=10, width=15, font=("Arial", 18))
        self.guesses_text.pack()
        
        self.draw_hangman()
        
    def draw_hangman(self):
        self.canvas.create_line(20, 220, 180, 220, width=2) #Floor
        self.canvas.create_line(90, 220, 90, 30, width=2)   #Pole
        self.canvas.create_line(90, 30, 150, 30, width=2)   #Ceiling
        self.canvas.create_line(150, 30, 150, 60, width=2)  #Rope
        self.canvas.create_oval(140, 60, 160, 80, width=2)  #Head
        self.canvas.create_line(150, 80, 150, 130, width=2) #body
        
def main():
    root = tk.Tk()
    root.title("Hangman Game")
    HangmanGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()
