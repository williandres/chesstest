import chess
from os import system
board = chess.Board()

while True:
    print(board)
    board.push_san(input("Movimiento: "))
    system("clear")