from sys import argv
script, textfile = argv

textdata = open(textfile)
name = textdata.read()

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

def initiate(name):
    guess = []
    for i in range(0,len(name)):
        guess.append("_")
    return guess

def guessed_wrong(a):
    return 


def checkguess(name, guess, guessed_char, avlbl):
    if guessed_char in name:
        for i in range(0,len(name)):
            if name[i] == guessed_char:
                guess[i] = guessed_char
        return guess, avlbl
    else:
        print("not found")
        avlbl -= 1
        print(f"{avlbl} guesses remaining")
        return guess, avlbl


def show(guess):
    for i in range(0,len(guess)):
        print (guess[i], end = "")

name_list = convert(name)
available = 10
guessed_so_far = (initiate(name))
print("Let's start!\nGuess a letter.\n")
print(guessed_so_far)

while guessed_so_far != name_list and available > 0:
    guessed_letter = input("Your guess? ")
    guessed_so_far, available = checkguess(name_list, guessed_so_far, guessed_letter, available)
    print (guessed_so_far)

if available == 0:
    print("hacked!")

if guessed_so_far == name_list:
    print("hung.")
