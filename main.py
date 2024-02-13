import sys

# My files
import fileIO
import functions

vocab_file_path = "zvocab.txt"
wrong_file_path = "zwrong.txt"
known_vocab_path = "zknown.txt"

all_words_map = fileIO.read_data_file(vocab_file_path)
known_words_map = fileIO.read_data_file(known_vocab_path)
wrong_words_map = fileIO.read_data_file(wrong_file_path)

# Remove known words from other maps
for word in known_words_map:
    if word in all_words_map:
      del all_words_map[word]
  
# Shuffle the maps
all_words_map = functions.shuffle_dict(all_words_map)
known_words_map = functions.shuffle_dict(known_words_map)
wrong_words_map = functions.shuffle_dict(wrong_words_map)

sys.stdout.reconfigure(encoding='utf-8')

# -------------------- Run -------------------- #
# Update files removing known words from the vocab list
fileIO.update_vocab_file(vocab_word_path=vocab_file_path, known_words_path=known_vocab_path)

# Review known words
if len(known_words_map) != 0:
  functions.review_check(wrong_file_path, known_words_map, "Review")

# Past wrong words
if len(wrong_words_map) != 0:
  functions.test_words(known_vocab_path, wrong_file_path, wrong_words_map, "Past Incorrect Words")

# All Words that are not known
functions.test_words(known_vocab_path, wrong_file_path, all_words_map, "All Words")

