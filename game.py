board = [0] * 8

for collumn in range(len(board)):
    board[collumn] = ["__"] * 8

current_point = [6,6]
available_moves = []
current_x = 6 - int(round(6/1.5,0))
print(current_x)

for row in range(6):
    if board[current_x][current_x] == "__":
        board[current_x][current_x] = "mango"
        available_moves.append((current_x, current_x))
        current_x+=1

print(available_moves)

for row in board:
    print(row)
    print("\n")