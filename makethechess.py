# Create an 8x8 chessboard as a list of lists
chessboard = [['' for _ in range(8)] for _ in range(8)]

# Fill the chessboard with alternating colors (e.g., 'W' for white, 'B' for black)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chessboard[i][j] = '■'
        else:
            chessboard[i][j] = '□'

# Add numbers and letters to the sides
for i in range(8):
    chessboard[i].insert(0, str(8 - i))  # Add numbers on the left side

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chessboard.append([''] + letters)  # Add letters on the bottom

# Print the chessboard
for row in chessboard:
    print(' '.join(row))


class Piece:
    def __init__(self, name, location, icon):
        self.name = name
        self.icon = icon
        self.location = location

    def draw_yourself(self, file, rank):
        for b in chessboard:
            if b == rank:
                for c in range(len(b)):
                    if c == file:
                        chessboard[chessboard.index(b)][c] = self.icon

    def check_legal_move(self):
        pass
