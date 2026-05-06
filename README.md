# cs32finalproject-mm
# Mastermind Game

This project is a Mastermind-style guessing game. The current version includes a two-player client-server mode. Player 1 enters a secret 4-digit code or 6-digit on the server side, and Player 2 guesses the code from the client side. After each guess, the server sends back feedback showing how many digits are fully correct and how many are partially correct.

## How to Run

Open two terminals. In the first terminal, run: python3 mastermind_2p_server.py
Enter a 4-digit secret code.

In the second terminal, run: python3 mastermind_2p_client.py
Enter 4-digit or 6-digit guesses until the code is guessed correctly or until the total number of guesses is used.

## Files

- mastermind.py: original single-player prototype
- mastermind_2p_server.py: server side for two-player version
- mastermind_2p_client.py: client side for two-player version
- socket32.py: CS32 socket helper library used for networking

## External Contributors

I used ChatGPT to help debug errors, understand socket issues, and write parts of the two-player client/server structure. The networking structure was based on the CS32 roshambo assignment and the course-provided socket32.py file.
