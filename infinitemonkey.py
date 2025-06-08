import time
from english_dictionary.scripts.read_pickle import get_dict
import random
import sys
dictionary = get_dict()
abc = list("abcdefghijklmnopqrstuvwxyz")

def monkey():
  attempts = 0
  words_count = 0
  word = input("Please enter the word to search for (under or equal to 10 letters): ")
  if len(word) > 10:
    print("Your word is above the length limit.")
    sys.exit()
  filequestion = input("Do you want to save the found words to a .txt file? (yes/no): ").strip().lower()
  if filequestion == "yes":
    filelocation = input("Please enter the path to the .txt file: ")
  elif filequestion == "no":
    filequestion = False
  start = time.time()
  while(True):
    word_length = random.randint(1, 10)
    random_word = ''.join(random.choices(abc, k=word_length))
    print(random_word)
    attempts += 1
    if random_word in dictionary:
      words_count +=1
      if filequestion:
        wordtext = random_word + "\n"
        with open(filelocation, "a") as fileopen:
          fileopen.write(wordtext)
    if random_word == word:
      end = time.time()
      elapsed_time = end - start
      print(f"Word found after {attempts} attempts!")
      print(f"The generator also found {words_count} words!")
      print(f"Elapsed time: {elapsed_time} seconds")
      if filequestion:
        with open(filelocation, "a") as final:
            final.write(f"{words_count} words found after {attempts} attempts with an elapsed time of {elapsed_time} seconds.")
      break
  
monkey()
