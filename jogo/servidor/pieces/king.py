from servidor.pieces.piece import Piece
import servidor

class King(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)


    def check_available_moves(self,board:list[list]):
        self.available_moves = []
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = int(self.current_pos[1])


        for row in range(current_x, current_x + 3):
            for column in range(current_y, current_y + 3):
                if (board[column - 1][row - 1] == "  " and "w" not in board[column - 1][row - 1])  and (row - 1 >= 0 and column - 1 >= 0):
                    self.available_moves.append([servidor.letter[row - 1], column - 1])


    def move(self, piece: Piece, move_requested:str, board:list):
        current_x, current_y = servidor.letter.index(self.current_pos[0]), 8 - int(self.current_pos[1])
        move_x, move_y = move_requested[0], int(move_requested[1])
        print(self.available_moves)
        move = [move_x, move_y]
        print(move)
        if move in self.available_moves:
            print("Move in dict")
            move[0] = servidor.letter.index(move[0])
            print(move)
            board[current_y][current_x] = "  "
            board[8 - move[1]][move[0]] = piece
            self.current_pos = move_requested
