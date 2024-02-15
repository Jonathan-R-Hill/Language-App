# My files
import Gui
import Console

def program_choice():
  programChoice = ""
  while programChoice != 'gui' and programChoice != 'console':
    programChoice = input("Chose between: console and gui\n")
  
  if programChoice == 'gui':
    Gui.main()
  elif programChoice == 'console':
    Console.main()


if __name__ == "__main__":
  program_choice()