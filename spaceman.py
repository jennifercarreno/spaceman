import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    user_guess = ''

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
           user_guess += secret_word[i]

    if secret_word == user_guess:
        return True
    else:
        return False
         

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    blanks = '_' * len(secret_word)
    

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
 
    


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    print(secret_word)

    #TODO: show the player information about the game according to the project spec
    print(f'The secret_word contans: {len(secret_word)} letters')
    print('You have 7 incorrect guesses, please enter one letter per round')

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    print('___________________________________________________________________')
    letters_guessed = []

    guesses = 0
    is_game_over = False

    while not is_game_over:
        guesses += 1
        user_guess = input('Enter a letter: ')
        letters_guessed.append(user_guess)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        is_guess_in_word(user_guess, secret_word)

        #TODO: show the guessed word so far
        get_guessed_word(secret_word, letters_guessed)

        #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed) or guesses >= 7:
            is_game_over = True

#These function calls that will start the game
print('Welcome to Spaceman!')


secret_word = load_word()
spaceman(secret_word)
