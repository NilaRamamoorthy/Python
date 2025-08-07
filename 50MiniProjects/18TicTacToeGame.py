import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Human starts
        self.winner = None

    def display_board(self):
        print("\nBoard:")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.check_winner(row, col)
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def check_winner(self, row, col):
        # Check row, column, and diagonals
        if all(self.board[row][i] == self.current_player for i in range(3)) or \
           all(self.board[i][col] == self.current_player for i in range(3)) or \
           (row == col and all(self.board[i][i] == self.current_player for i in range(3))) or \
           (row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3))):
            self.winner = self.current_player

    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def get_empty_cells(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def ai_move(self):
        empty_cells = self.get_empty_cells()
        return random.choice(empty_cells) if empty_cells else None

    def play(self):
        while not self.winner and not self.is_draw():
            self.display_board()
            if self.current_player == 'X':
                row, col = map(int, input("Enter row and column (0-2) for your move: ").split())
                self.make_move(row, col)
            else:
                print("Computer's turn:")
                row, col = self.ai_move()
                print(f"Computer chose: {row} {col}")
                self.make_move(row, col)

        self.display_board()
        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
