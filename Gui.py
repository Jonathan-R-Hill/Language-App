import tkinter as tk
import sys
import fileIO
import random

vocab_file_path = "zvocab.txt"
wrong_file_path = "zwrong.txt"
known_vocab_path = "zknown.txt"
sys.stdout.reconfigure(encoding='utf-8')
# Remove duplicate entries in all files
fileIO.remove_duplicate_entries(wrong_file_path)
fileIO.remove_duplicate_entries(known_vocab_path)
fileIO.remove_duplicate_entries(vocab_file_path)
# Update files removing known words from the vocab list
fileIO.update_vocab_file(vocab_file_path, known_vocab_path)
# Generate maps
vocab_map = fileIO.read_data_file(vocab_file_path)
# ---------- Global Variables ---------- #
current_word_index = 0
korean_word = list(vocab_map.keys())[current_word_index]
english_word = vocab_map[korean_word]
FONT = ('Batang Regular', 16)
def main():
    # ---------- Functions ---------- #
    def update_english_label(english_word):
        english_word_label.config(text=english_word, font= FONT)

    def clear_entry_box():
        text_entry.delete(0, tk.END)
        
    def get_user_input():
        global current_word_index
        global korean_word
        global english_word
        
        user_input = text_entry.get()
        clear_entry_box()
        
        if user_input == korean_word:
            last_word_label.config(text=f"You were correct!\n{korean_word} = {english_word}", font=FONT)
        else:
            last_word_label.config(text=f"That was incorrect\n{korean_word} = {english_word}", font=FONT)
            fileIO.write_word_to_file(wrong_file_path, english_word, korean_word)

        # Update to the next word
        current_word_index = random.randint(0, len(vocab_map))

        korean_word = list(vocab_map.keys())[current_word_index]
        english_word = vocab_map[korean_word]
        update_english_label(english_word)


    # ---------- GUI Build ---------- #
    BG_COL = "#B1DDC6"

    window = tk.Tk()
    window.title("Language App")
    window.config(padx=40, pady=40, bg=BG_COL)

    check_button = tk.Button(window, text="Check Answer", command=get_user_input, padx=10, pady=10, font=FONT)
    check_button.grid(column=2, row=2)

    english_word_label = tk.Label(window, text=english_word, font=FONT)
    english_word_label.grid(column=1, row=0)

    text_entry = tk.Entry(window, font=FONT)
    text_entry.grid(column=2, row=1, padx=10, pady=10)

    last_word_label = tk.Label(window, text="")
    last_word_label.grid(column=3, row=0)

    window.mainloop()
