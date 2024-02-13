def read_data_file(file_path: str):
  """
    Reads data from a file and returns it as a dictionary.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    dict: A dictionary containing the data read from the file.
  """
  vocab_map = {}
  
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      for line in file:
        parts = line.strip().split(',')
        
        if len(parts) == 2:
            korean, english = parts
            vocab_map[korean.strip()] = english.strip()
  except FileNotFoundError:
      print("File not found.")
  except Exception as e:
      print("An error occurred:", e)
  return vocab_map


def write_word_to_file(file_path: str, english: str, korean: str):
  """
    Writes a word pair to a file.

    Parameters:
    file_path (str): The path to the file to write to.
    english (str): The English word.
    korean (str): The Korean word.

    Returns:
    None
  """
  try:
    with open(file_path, 'a', encoding='utf-8') as file:
      file.write(f"{korean},{english}\n")  
  except FileNotFoundError:
    print("File not found.")
  except Exception as e:
    print("An error occurred:", e)

def update_vocab_file(vocab_word_path: str, known_words_path: str):
    """
    Updates the vocabulary file by removing words that are present in the known words file.

    Parameters:
    vocab_word_path (str): The file path to the vocabulary file to be updated.
    known_words_path (str): The file path to the known words file.

    Returns:
    None
    """
    # Read known words and store them in a set
    known_words_set = set()
    with open(known_words_path, 'r', encoding='utf-8') as file:
      for line in file:
          parts = line.strip().split(',')
          if len(parts) == 2:
              korean, english = parts
              known_words_set.add(korean.strip())

    # Read vocabulary file and filter out known words
    temp_list = []
    with open(vocab_word_path, 'r', encoding='utf-8') as file:
      for line in file:
          parts = line.strip().split(',')
          if len(parts) == 2:
              korean, english = parts
              if korean.strip() not in known_words_set:
                  temp_list.append(line.strip())

    #  Write  content back to vocabulary file
    with open(vocab_word_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(temp_list))

