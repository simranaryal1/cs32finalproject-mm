# mastermind_2p_server.py

from socket32 import create_new_socket

HOST = '127.0.0.1'
PORT = 65432

def compare_guess(secret, guess):
    full = 0
    partial = 0

    secret_unused = []
    guess_unused = []

    for i in range(len(secret)):
        if guess[i] == secret[i]:
            full += 1
        else:
            secret_unused.append(secret[i])
            guess_unused.append(guess[i])

    for ch in guess_unused:
        if ch in secret_unused:
            partial += 1
            secret_unused.remove(ch)

    return full, partial

def get_secret_code(code_length):
    while True:
        secret = input(f"Player 1, enter a {code_length}-number secret code: ")

        if len(secret) == code_length and secret.isdigit():
            return secret
        else:
            print(f"Secret code must be exactly {code_length} numbers. Try again.")

def main():
    print("WELCOME TO TWO-PLAYER MASTERMIND!")

    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print("Mastermind server started. Listening on", (HOST, PORT))

        conn2client, addr = s.accept()
        print("Connected by", addr)

        conn2client, addr = s.accept()
        print("Connected by", addr)

        with conn2client:
            mode = conn2client.recv()

            # 👇 ADD THIS PART HERE
            difficulty = input("Player 1, choose difficulty (regular/hard): ").lower()

            if difficulty == "hard":
                code_length = 6
                max_guesses = 15
            else:
                code_length = 4
                max_guesses = 10

            # send code length to client
            conn2client.sendall(str(code_length))

            # now get secret code
            secret = get_secret_code(code_length)

            guess_count = 0

            while True:
                guess = conn2client.recv()

                    while True:
                        guess = conn2client.recv()

                        if guess == '':
                            break

                full, partial = compare_guess(secret, guess)

                if mode == "easy":
                    hint = ""

                    for i in range(len(secret)):
                        if guess[i] == secret[i]:
                            hint += secret[i]
                        else:
                            hint += "_"

                    message = f"Full: {full}, Partial: {partial}\nHint: {hint}"
                else:
                    message = f"Full: {full}, Partial: {partial}"

                if full == 4:
                    message += "\nYou guessed the code!"
                    conn2client.sendall(message)
                    break
                else:
                    conn2client.sendall(message)

if __name__ == "__main__":
    main()
