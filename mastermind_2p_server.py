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

def get_secret_code():
    while True:
        secret = input("Player 1, enter a 4-number secret code: ")

        if len(secret) == 4 and secret.isdigit():
            return secret
        else:
            print("Secret code must be exactly 4 numbers. Try again.")

def main():
    print("WELCOME TO TWO-PLAYER MASTERMIND!")
    secret = get_secret_code()

    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print("Mastermind server started. Listening on", (HOST, PORT))

        conn2client, addr = s.accept()
        print("Connected by", addr)

        with conn2client:
            while True:
                guess = conn2client.recv()

                if guess == '':
                    break

                full, partial = compare_guess(secret, guess)

                if full == 4:
                    message = f"Full: {full}, Partial: {partial}\nYou guessed the code!"
                    conn2client.sendall(message)
                    break
                else:
                    message = f"Full: {full}, Partial: {partial}"
                    conn2client.sendall(message)

if __name__ == "__main__":
    main()
