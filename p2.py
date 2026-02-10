import random

# ----- Word list (small on purpose) -----
WORDS = [
    "crane", "trace", "slate", "flame", "blame",
    "grape", "plane", "brick", "pride", "shine",
    "stone", "money", "cigar", "reign", "sweet",
    "sound", "round", "heart", "earth", "water"
]


# ----- Core scoring logic -----
def score_guess(guess, secret):
    result = []
    for i in range(5):
        if guess[i] == secret[i]:
            result.append("Y")
        elif guess[i] in secret[i+1:]:
            result.append("O")
        else: 
            result.append("X")
    return "".join(result)


# ----- Check guess formatting -----
def is_valid_guess(guess):
    if len(guess) != 5:
        return False
    if not guess.isalpha() or not guess.islower():
        return False
    return True

# ----- Choose secret word -----
def choose_secret(words):
   return words[0]





# ----- One turn of the game -----
def play_turn(secret, guess):
    if not is_valid_guess(guess):
        return "Invalid guess"
    return score_guess(guess, secret)


# ----- Full Wordle game -----
def play_game(words):
    secret = choose_secret(words)
    max_guesses = 6
    for turn in range(max_guesses):
        guess = input("Enter a 5 letter guess: ")
        feedback = play_turn(secret, guess)
        print(feedback)
        if feedback == "YYYYY":
            print("You win!")
            return
    print("You Lose. The secret word was", secret)