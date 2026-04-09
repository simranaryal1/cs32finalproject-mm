#mastermind.py

import random
def compare_guess(secret, guess):
    full = 0
    partial = 0

    secret_unused = []
    guess_unused = []

    for i in range (len(secret)):
        if guess [i] == secret[i]:
            full +=1

    for ch in guess_unused:
        if ch in secret_unused:
            partial +=1
            secret.unused.remove(ch)

        partial -= full

        return full, partial

def main():
    print("WELCOME TO MASTERMIND!")

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    secret = "".join (random.choice(numbers) for _ in range (4))

    while True:
        guess = input ("Enter your 4-number guess: ")

        if len(guess) !=4 or not guess.isdigit():
            print ("Invalid guess, try again")
            continue

        full, partial = compare_guess (secret, guess)

        print (f"Full: {full}, Partial: {partial}")

        if full ==4:
            print("You win!")
            break

if __name__ == "__main__":
    main()
