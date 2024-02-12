import fileIO
import random

def test_words(known_file_path: str, wrong_file_path: str, vocab_to_test: map, section_testing: str):
  """
    Tests the user on a set of vocabulary words.

    Parameters:
    known_file_path (str): The file path to the known words list.
    wrong_file_path (str): The file path to the wrong words list.
    vocab_to_test (dict): A dictionary containing vocabulary words to be tested, where keys are Korean words and values are English words.
    section_testing (str): The section or category of the vocabulary being tested.

    Returns:
    None
  """
  print(section_testing)
  for korean, english in vocab_to_test.items():
      print(f'Word to translate: {english}')
      user_input = input("Enter the Korean translation: ")

      if user_input == korean:
        print(f"Correct! {english} = {korean}")
        add_to_known_words_check(known_file_path, english, korean)
      else:
        print(f"Nice try but: {english} = {korean}")
        fileIO.write_word_to_file(wrong_file_path, english, korean)
      print("\n\n")


def add_to_known_words_check(file_path: str, english: str, korean: str):
  """
    Prompts the user to add a word to the known words list.

    Parameters:
    file_path (str): The file path to the known words list.
    english (str): The English translation of the word.
    korean (str): The Korean word.

    Returns:
    None
  """
  check = ""
  while check != "yes" and check != "no" and check != "네" and check != "아니":
    check = input("Would you like to add thsi word to the known words list? yes, no, 네, 아니\n")
  
  if check == "yes" or check == "네":
    fileIO.write_word_to_file(file_path, english, korean)


def review_check(known_words_path: str, wrong_word_path: str, vocab_to_test: map, section_testing: str):
  """
    Initiates a review session for testing vocabulary words.

    Parameters:
    known_words_path (str): The file path to the known words list.
    wrong_word_path (str): The file path to the wrong words list.
    vocab_to_test (dict): A dictionary containing vocabulary words to be tested, where keys are Korean words and values are English words.
    section_testing (str): The section or category of the vocabulary being tested.

    Returns:
    None
  """
  check = ""
  while check != "yes" and check != "no" and check != "네" and check != "아니":
    check = input("Would you like to add thsi word to the known words list? yes, no, 네, 아니\n")
  
  if check == "yes" or check == "네":
    test_words(known_words_path, wrong_word_path, vocab_to_test, section_testing)


def shuffle_dict(vocab_map: map):
    """
    Shuffles the key-value pairs in a dictionary.

    Parameters:
    vocab_map (dict): The dictionary to be shuffled.

    Returns:
    dict: The shuffled dictionary.
    """
    items = list(vocab_map.items())
    random.shuffle(items)
    shuffled_dict = dict(items)
    return shuffled_dict