
from random import choice
from Forca.palavras import STATUS, WORDS 


def get_secret_word(words: list) -> str: 
    return choice(words).upper()

def print_game_board(
    secret_word: str,
    correct_letters: list[str],
    missed_letters: list[str],
    error: int,
    attempts: int,
    status: list[str],
) -> None:

    enconced_word = ""
    for letter in secret_word:
        if letter not in correct_letters:
            enconced_word += "_"
        else:
            enconced_word += letter

    if  error <= attempts:
        print(status[error])
        print(enconced_word)

    print(f"\nLetras corretas: {' '.join(correct_letters)}")

    print(f"\nLetras erradas: {' '.join(missed_letters)}")

    return None

def read_input_player() -> str:  
    input_char = input("\nDigite uma letra: ").upper() 
    while len(input_char) != 1:
        print("Entre com apenas um caracter!")
        input_char = input("\nDigite uma letra com um único caracter: ").upper()
    return input_char
    
def guess_letter(input_char: str, secret_word: str, correct_letters: list, wrong_letters: list) -> bool:
    if input_char in secret_word and input_char not in correct_letters:
        correct_letters.append(input_char)
        return True

    elif input_char not in secret_word and input_char not in wrong_letters:
        wrong_letters.append(input_char)
        return False

    else: 
        print("\nEsta letra já foi jogada, por favor escolha outra!")
        return False

def game_continue(correct_letters: list, secret_word: str, error: int, attempts: int, status: list) -> bool:
    if set(correct_letters) == set(secret_word):
        print("\nVocê venceu!")
        return False
    elif error >= attempts:
        print(status[error])
        print(f"A palavra secreta é {secret_word}.")
        return False 
    return True

secret_word = get_secret_word(WORDS) 

correct_letters = []

missed_letters = []

error = 0

attempts = 6

while game_continue(correct_letters, secret_word, error, attempts, STATUS):
    print_game_board(secret_word, correct_letters, missed_letters, error, attempts, STATUS)
    input_char = read_input_player()
    if not guess_letter(input_char, secret_word, correct_letters, missed_letters):
        error += 1












