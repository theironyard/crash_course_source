import re
import time
import os


# clears the output window
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


# update the proxyword variable so that each index in the updates
# list is changed to char
def updateProxy(proxy, updates, char):
    for i in updates:
        proxy[i] = char

    return proxy


# print the proxy array and some messaging around it
def printProxy(proxy):
    px = ""
    correct = 0

    for letter in proxy:
        px += letter + " "
        if letter != "_":
            correct += 1

    print "The word: " + px + "\n\n"


# nicely intro the main rules of the game
def intro():
    print "____    ____ "
    print "`MM'    `MM' "
    print " MM      MM  "
    print " MM      MM    ___    ___  __     __     ___  __    __      ___    ___  __  "
    print " MM      MM  6MMMMb   `MM 6MMb   6MMbMMM `MM 6MMb  6MMb   6MMMMb   `MM 6MMb  "
    print " MMMMMMMMMM 8M'  `Mb   MMM9 `Mb 6M'`Mb    MM69 `MM69 `Mb 8M'  `Mb   MMM9 `Mb "
    print " MM      MM     ,oMM   MM'   MM MM  MM    MM'   MM'   MM     ,oMM   MM'   MM "
    print " MM      MM ,6MM9'MM   MM    MM YM.,M9    MM    MM    MM ,6MM9'MM   MM    MM "
    print " MM      MM MM'   MM   MM    MM  YMM9     MM    MM    MM MM'   MM   MM    MM "
    print " MM      MM MM.  ,MM   MM    MM (M        MM    MM    MM MM.  ,MM   MM    MM "
    print "_MM_    _MM_`YMMM9'Yb._MM_  _MM_ YMMMMb. _MM_  _MM_  _MM_`YMMM9'Yb._MM_  _MM_ "
    print "                                6M    Yb "
    print "                                YM.   d9 "
    print "                                 YMMMM9 "

    print "Howdy!. Time to play hangman!"
    print "Don't worry, its safe as can be"
    time.sleep(1)
    print "The rules are simple:"
    print "Keep guessing letters until"
    print "you've completed the hidden word..."
    print "...or until you've hanged the man. :P\n"
    time.sleep(1)
    print "Here's a hint: All of the letters are lowercase!\n\n"
    time.sleep(1)


# End of game message if the player fails seven guesses
def failureOutro():
    print "HANGED!"
    print "Well, thats the end of our friend."
    print "You'll get 'em next time, tiger..."
    print "...Too bad our friend won't be around to see it."


# End of game message if the succeeds by completing the hidden word
def successOutro():
    print "Hey, you did it! You saved our friend from a terrible fate."
    time.sleep(1)
    print """Sort of, anyway. I mean the second you close this console window, our friend will
cease to exist."""
    print "No matter, you won! Hiyo! Awesomesauce!!\n\n"


# In game message if the player guesses a wrong letter
def message(num, message):
    print message
    print "You have " + str(7 - num) + " guesses left\n\n"


# In game message if the player guesses a correct letter
def successMessage(list):
    print "Excellent guess. You found " + str(len(list)) + " character matches."
    print "Looks like our friend might just survive.\n\n"


# prompt the player for a character guess and return a
# tuple describing the result
def guess(word):
    char = ""

    while char == "":
        char = raw_input("Guess a letter: ")

    found = letterIn(word, char)
    return (len(found) > 0, char, found)


# test if the word has been completed
def hasWon(word):
    return "_" not in word


# finds all character matches in a word and
# returns a list of word indicies for the letter
def letterIn(word, character):
    return [match.start() for match in re.finditer(character, word)]


# logic for drawing the hangman image
def draw(guesses):
    a = " "
    b = " "
    c = "   "
    d = "       "
    e = "     "
    f = "     "

    if guesses > 0:
        a = "|"

    if guesses > 1:
        b = "0"

    if guesses > 2:
        c = " A "
        d = "   V   "

    if guesses > 3:
        c = "/A "
        d = "/  V   "

    if guesses > 4:
        c = "/A\\"
        d = "/  V  \\"

    if guesses > 5:
        e = "/    "
        f = "|    "

    if guesses > 6:
        e = "/ \\  "
        f = "|   |"

    print "    H A N G M A N"
    print "    ============="
    print "      " + a + "        ##"  # a
    print "      " + b + "        ##"  # b
    print "     " + c + "       ##"  # c
    print "   " + d + "     ##"  # d
    print "     " + e + "     ##"  # e
    print "    " + f + "      ##"  # f
    print "    " + f + "      ##"
    print "               ##"
    print " ###################"
    print " ###################\n\n"
