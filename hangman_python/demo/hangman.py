import random
import functions as f
from messages import m


# how many incorrect guesses has the player made?
guesses = 0


# randomly select one of five words to play hangman
word = random.choice(["secret", "cucumber", "potpourri", "jumpoff", "queazy"])


# proxy is the placeholder text that hides the letters from the player
# if they haven't yet guessed a letter then proxy shows an underscore instead
proxy = ["_"] * len(word)


# clear the console
f.clear()


# play the intro text
f.intro()


# prompt the player to start the game
raw_input("\n\nPress ENTER when you are ready!")


# clear the console
f.clear()


# first drawing of the gallows!!
f.draw(guesses)


#print a playful message to the player
f.message(guesses, random.choice(m[guesses]))


# print out the hidden word proxy
# the proxy starts out as a string of underscores
# which are replaced with letters when the player
# guesses correctly
f.printProxy(proxy)


# START THE GAME LOOP
# The game loop continues to run until the
# player has won or until our friend is hanged
while True:
    # deconstructing the tuple into
    # three disict variables
    # 'didfind' is a boolean that tells us whether the
    #          player guesses a correct character or not
    # 'char' is the character guessed
    # 'matches' is a list of indicies for character matches
    didfind, char, matches = f.guess(word)


    # clear the terminal screen
    # it just looks better and feels more like a game
    f.clear()


    # if didfind is true then create a successMessage and
    # update the word proxy string
    if didfind:

        # if we're still going, then redraw the output screen
        f.draw(guesses)
        f.successMessage(matches)
        f.updateProxy(proxy, matches, char)
        f.printProxy(proxy)

    # else they didn't find a letter
    else:

        # increment the number of incorrect guesses
        guesses += 1
        f.draw(guesses)
        

        print "Nope. That letter isn't in the word."


        f.message(guesses, random.choice(m[guesses]))
        f.printProxy(proxy)


    # if the player has lost or won, break out of the while loop
    # hasWon returns True or False
    if guesses > 6:
        f.clear()
        #draw the gallows one last time
        f.draw(guesses)
        f.failureOutro()
        break


    if f.hasWon(proxy):

        #draw the gallows one last time
        f.clear()
        f.draw(guesses)
        f.successOutro()
        break

