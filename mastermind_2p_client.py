# mastermind_2p_client.py

from socket32 import create_new_socket

HOST = '127.0.0.1'
PORT = 65432

def player_guess():
    while True:
        guess = input("Player 2, enter your 4-number guess: ")

        if len(guess) == 4 and guess.isdigit():
            return guess
        else:
            print("Guess must be exactly 4 numbers. Try again.")

def main():
    print("WELCOME TO TWO-PLAYER MASTERMIND!")

    with create_new_socket() as s:
        s.connect((HOST, PORT))

        while True:
            guess = player_guess()

            s.sendall(guess)

            response = s.recv()
            print(response)

            if "You guessed the code!" in response:
                break

if __name__ == "__main__":
    main()
