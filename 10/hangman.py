from string import ascii_lowercase
import sys

sys.path.append('.')

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'

def update_word():
    global word_state
    x = ('_' if char not in solved_letters else char for char in
         ascii_lowercase)
    x = ''.join(x)
    word_state = word.translate(str.maketrans(ascii_lowercase, x))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)
    word = word.lower()
    print(word)

    # init / call program
    # Setup
    print('Welcome to Hangman!')
    letters = len(word)
    solved_letters = ''
    mistakes = 0
    update_word()

    # Main game loop
    while True:
        print(f'Current guessed word: {word_state}')

        # Guess loop
        guess = input('Guess a letter! : ')
        if guess in solved_letters:
            print('Good, but guessed before! Try again.')
            continue
        elif guess in word:
            print('good guess!')
            solved_letters = ''.join((guess, solved_letters))

        else:
            print('Not quite!')
            mistakes += 1

        update_word()

        # have I won?
        if '_' not in word_state:
            print("Congratulations! You've won!")
            break
        elif mistakes >= ALLOWED_GUESSES:
            print("You lost!")
            break
        else:
            print(f'Your solved letters are: {solved_letters}')
            print(HANG_GRAPHICS[mistakes])
