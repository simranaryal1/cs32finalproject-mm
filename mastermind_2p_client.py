# mastermind_2p_client.py

from socket32 import create_new_socket

HOST = '127.0.0.1'
PORT = 65432

def player_guess(code_length):
    while True:
        guess = input(f"Player 2, enter your {code_length}-number guess: ")

        if len(guess) == code_length and guess.isdigit():
            return guess
        else:
            print(f"Guess must be exactly {code_length} numbers. Try again.")

def main():
    print("WELCOME TO TWO-PLAYER MASTERMIND!")

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        mode = input("Choose mode (easy/normal): ").lower()
        difficulty = input("Choose difficulty (regular/hard): ").lower()

        settings = mode + "," + difficulty
        s.sendall(settings)
        difficulty = input("Choose difficulty (regular/hard): ").lower()

        while True:
            guess = player_guess(code_length)

            s.sendall(guess)

            response = s.recv()
            print(response)

            if "You guessed the code!" in response:
                break

if __name__ == "__main__":
    main()
