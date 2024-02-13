import sys

# My files
import fileIO
import functions

vocab_file_path = "zvocab.txt"
wrong_file_path = "zwrong.txt"
known_vocab_path = "zknown.txt"

sys.stdout.reconfigure(encoding='utf-8')

# -------------------- Run -------------------- #
# Remove duplicate entries in all files
fileIO.remove_duplicate_entries(wrong_file_path)
fileIO.remove_duplicate_entries(known_vocab_path)
fileIO.remove_duplicate_entries(vocab_file_path)

# Update files removing known words from the vocab list
fileIO.update_vocab_file(vocab_file_path, known_vocab_path)

# Generate maps
vocab_map = fileIO.read_data_file(vocab_file_path)
known_words_map = fileIO.read_data_file(known_vocab_path)
wrong_words_map = fileIO.read_data_file(wrong_file_path)

# Shuffle the maps
vocab_map = functions.shuffle_dict(vocab_map)
known_words_map = functions.shuffle_dict(known_words_map)
wrong_words_map = functions.shuffle_dict(wrong_words_map)

# Review known words
if len(known_words_map) != 0:
  functions.review_check(wrong_file_path, known_words_map, "Review")

# Past wrong words
if len(wrong_words_map) != 0:
  functions.test_words(known_vocab_path, wrong_file_path, wrong_words_map, "Past Incorrect Words")

# All Words that are not known
functions.test_words(known_vocab_path, wrong_file_path, vocab_map, "All Words")

