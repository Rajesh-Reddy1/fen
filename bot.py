fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R'

# class Game:
#     def __init__(self, fen):
#         self.board = fen_to_board(fen)
#     def replace_lowercase(self):
#         for row in self.board:
#             for i, char in enumerate(row):
#                 if char.islower():
#                     row[i] = 'B'
class Game:
    def __init__(self, fen):
        self.board = fen_to_board(fen)

    def insert_before_p(self):
        for row in self.board:
            i = 0
            while i < len(row):
                if row[i] == 'p':
                    row.insert(i, 'b')
                    i += 1
                i += 1

def fen_to_board(fen):
    board = []
    for row in fen.split('/'):
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(['-'] * int(char))
            else:
                board_row.append(char)
        board.append(board_row)
    return board


game = Game(fen)

# print(game.board)

game = Game(fen)
# print(game.board)
game.insert_before_p()
print(game.board)