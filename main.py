import sys

# My files
import FileIO
import Func

vocab_file_path = "zvocab.txt"
wrong_file_path = "zwrong.txt"
known_vocab_path = "zknown.txt"

all_words_map = FileIO.read_data_file(vocab_file_path)
known_words_map = FileIO.read_data_file(known_vocab_path)
wrong_words_map = FileIO.read_data_file(wrong_file_path)

# Remove known words from other maps
for word in known_words_map:
    if word in all_words_map:
      del all_words_map[word]
    if word in wrong_words_map:
      del known_words_map[word]

sys.stdout.reconfigure(encoding='utf-8')


# -------------------- Run -------------------- #

# Review known words
if len(known_words_map) != 0:
  Func.review_check(known_vocab_path, wrong_file_path, known_vocab_path, "Review")

# Past wrong words
if len(wrong_words_map) != 0:
  Func.test_words(known_vocab_path, wrong_file_path, wrong_words_map, "Past Incorrect Words")

# All Words that are not known
Func.test_words(known_vocab_path, wrong_file_path, all_words_map, "All Words")

