# Put your functions in here.
# Feel free to run your design past me before beginning to implement your solution.
        
def get_puzzle():

	string = input("")
	puzzle = []
	
	puzzle.append(string[0:10])
	puzzle.append(string[10:20])
	puzzle.append(string[20:30])
	puzzle.append(string[30:40])
	puzzle.append(string[40:50])
	puzzle.append(string[50:60])
	puzzle.append(string[60:70])
	puzzle.append(string[70:80])
	puzzle.append(string[80:90])
	puzzle.append(string[90:100])

	return puzzle

def get_words():

	string = input("")
	words = string.split()

	return words

def check_word(word, puzzle):
	if check_right(word,puzzle) != -1:
		return check_right(word,puzzle)
	
	elif check_left(word,puzzle) != -1:
		return check_left(word,puzzle)
	
	elif check_up(word,puzzle) != -1:
		return check_up(word,puzzle)
	
	elif check_down(word,puzzle) != -1:
		return check_down(word,puzzle)

	elif check_diagonal(word, puzzle) != -1:
		return check_diagonal(word,puzzle)
	
	else:
		return "None"


def check_right(word, puzzles):
	for row in range(len(puzzles)):
		num = puzzles[row].find(word)
		if num != -1:
			return (row,num, "FORWARD")
	return -1

def check_left(word, puzzle):
	new_word = []
	for i in range(len(word)-1 , -1, -1):
		new_word.append(word[i])
	backwards = "".join(new_word)

	for row in range(len(puzzle)):
		num = puzzle[row].find(backwards)
		if num != -1:
			return (row, num + len(word) - 1, "BACKWARD")
	return -1

def check_down(word, puzzle):
	reverse = reverse_puzzle(puzzle)
	wrong = check_right(word, reverse)
	if wrong != -1:
		return(wrong[1], wrong[0], "DOWN")
	else:
		return wrong

def check_up(word, puzzle):
	reverse = reverse_puzzle(puzzle)
	wrong = check_left(word, reverse)
	if wrong != -1:
		return(wrong[1], wrong[0], "UP")
	else:
		return wrong

def reverse_puzzle(puzzle):
	reverse = []
	for letter in range(10):
		letters = []
		for row in range(10):
			letters.append(puzzle[row][letter])
		new_string = ''.join(letters)
		reverse.append(new_string)
	return reverse

def check_diagonal(word, puzzles):

	for row in range(len(puzzles)):
		for letter in range(10):
			if word[0] == puzzles[row][letter]:
				i = 0
				test_word = []
				while i < len(word):
					if row + i < 10 and letter + i < 10:
						test_word.append(puzzles[row+i][letter+i])
					i+= 1
				if ''.join(test_word) == word:
					return (row, letter, "DIAGONAL")
	return -1


