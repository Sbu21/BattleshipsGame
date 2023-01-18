class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]

    def play(self, move, board):
        x = int(move[1]) - 1
        y = ord(move[0]) - ord('A')
        win = False
        if board[x][y] == 'S':
            board[x][y] = 'H'
            win = self._check_win(board)
            return "hit", x, y, win
        else:
            board[x][y] = 'M'
            return "miss", x, y, win

    def _parse_move(self, move):
        x = int(move[1]) - 1
        y = ord(move[0]) - ord('A')
        return x, y

    def _check_win(self, board):
        for row in board:
            if "S" in row:
                return False
        return True
