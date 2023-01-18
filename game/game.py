import random

from src.board.texttable_board import TextTable_board
from src.player.player import Player
from src.board.board import Board
from src.player.computer import Computer



class BattleshipGame:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()
        self.board = Board()
        self.table = TextTable_board()

    def play(self):
        self.player.place_ships()
        self.computer.place_ships()

        self.table.display_board(self.player.board)
        self.table.display_board(self.computer.hidden_board())

        while True:

            move = input("Enter your move (e.g. A5): ")
            if not self._validate_move(move):
                print("Invalid move, please enter a move in the format A5")
                continue

            result, x, y, win = self.board.play(move, self.computer.board)

            if result == "hit":
                print("Hit!")
                self.computer.board[x][y] = 'H'
                self.computer.hidden_board()[x][y] = 'H'
                if win:
                    print("You win!")
                    break
            elif result == "miss":
                print("Miss!")
                self.computer.board[x][y] = 'M'
                self.computer.hidden_board()[x][y] = 'M'

            self.table.display_board(self.computer.hidden_board())

            move = self.computer.get_move()
            print()

            result, x, y, win = self.board.play(move, self.player.board)
            if result == "hit":
                print("Computer Hit your ship!")
                self.player.board[x][y] = 'H'

                if win:
                    print("Computer wins!")
                    break

            elif result == "miss":
                print("Computer Missed!")
                self.player.board[x][y] = 'M'

            self.table.display_board(self.player.board)


    def _validate_move(self, move):
        if len(move) != 2:
            return False
        if move[0] not in "ABCDEFGHIJ":
            return False
        if not move[1].isnumeric() or int(move[1]) < 1 or int(move[1]) > 10:
            return False
        return True


if __name__ == "__main__":
    game = BattleshipGame()
    game.play()