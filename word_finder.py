from funcs import *

def main():
   
   puzzle = get_puzzle()
   words = get_words()
   
   print("Puzzle:\n")
   for line in puzzle:
      print(line)

   print("")

   for word in words:
      answer = check_word(word,puzzle)
      if answer != "None":
         print(word+": ("+answer[2]+") row:", answer[0],"column:", answer[1])
      else:
         print(word+": word not found")


if __name__ == '__main__':
   main()
