# mastermind_2p_client.py

from socket32 import create_new_socket

HOST = '127.0.0.1'
PORT = 65432

def player_guess(code_length):
    while True:
        guess = input(f"Player 2, enter your {code_length}-character guess (numbers or letters): ")
        if len(guess) != code_length:
            print(f"Guess must be exactly {code_length} characters.")
        elif not guess.isalnum():   # able to input letters or numbers
            print("Use only letters or numbers.")
        else:
            return guess

def main():
    print("WELCOME TO TWO-PLAYER MASTERMIND!")

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        mode = input("Choose mode (easy/normal): ").lower()
        s.sendall(mode)

        code_length = int(s.recv())

        while True:
            guess = player_guess(code_length)

            s.sendall(guess)

            response = s.recv()
            print(response)

            if "You guessed the code!" in response or "Out of guesses!" in response:
                break

if __name__ == "__main__":
    main()
