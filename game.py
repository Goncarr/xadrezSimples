#step1) Board
#step2) Pieces
#step3) Turns
#step4) Move pieces on each turn

#create 8x8 matrix

board = [0] * 8

for collumn in range(len(board)):
    board[collumn] = ["  "] * 8

#dicionário com as coordenadas das peças brancas
white_pieces_map = {
    "wP": [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)],
    "wN": [(7,1),(7,6)],
    "wB": [(7,2),(7,5)],
    "wR": [(7,0),(7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)],
}

#dicionário com as coordenadas das peças pretas
black_pieces_map = {
    "bP": [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
    "bN": [(0,1),(0,6)],
    "bB": [(0,2),(0,5)],
    "bR": [(0,0),(0,7)],
    "bQ": [(0,3)],
    "bK": [(0,4)],
}

col_map = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
}

"""_summary_
    Esta função criar o tabuleiro de xadrez sem as peças

    @parametros
    board:list - matriz 8x8 representado o tabuleiro
"""
def print_board(board:list):
    for i, row in enumerate(board):
        print(8-i, end= ": ")
        for j, col in enumerate(row):
            print(col, end= " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

"""_summary_
    Esta função insere as peças pretas e brancas no tabulerios

    @parametros
    board:list - matriz 8x8 representado o tabuleiro
    white_pieces:dict - dicionário com as pecas brancas
    black_pieces:dict - dicionário com as pecas pretas
"""
def put_pieces(board:list,white_pieces:dict, black_pieces:dict):
    for piece, squares in white_pieces.items():
        for square in squares:
            x,y = square[0], square[1]
            board[x][y] = piece
    for piece, squares in black_pieces.items():
        for square in squares:
            x,y = square[0], square[1]
            board[x][y] = piece


put_pieces(board,white_pieces_map,black_pieces_map)
print_board(board)

curr_turn = 1
game_over = False

while not game_over:
    print_board(board)
    print("")
    curr_player = ""

    if curr_turn % 2 == 1:
        curr_player = "white"
    else:
        curr_player = "black"

    curr_turn += 1 

    print(f"{curr_player}'s turn!")
    print("")
    
    starting_square = input("Enter the square whose piece you'd like to play (EX: e1): ")
    start_x, start_y = starting_square[0], starting_square[1]
    start_x = col_map[start_x]
    start_y = 8 - int(start_y)
    start_x, start_y = start_y, start_x

    ending_square = input("Enter the square you'd like to move (EX: a4): ")
    end_x, end_y = ending_square[0], ending_square[1]
    end_x = col_map[end_x]
    end_y = 8 - int(end_y)
    end_x, end_y = end_y, end_x

    temp = board[start_x][start_y]
    board[start_x][start_y] = "  "
    board[end_x][end_y] = temp