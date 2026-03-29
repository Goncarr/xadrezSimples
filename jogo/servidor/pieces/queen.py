from servidor.pieces.piece import Piece

class Queen(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)


    def check_available_moves(self,board:list[list]):
        self.available_moves = []

        current_x, current_y = int(self.current_pos[0]), int(self.current_pos[1])

        for row in range(len(board)):
            if board[row][current_y] == "  ":
                self.available_moves.append((current_x, row))

        for column in range(len(board)):
            if board[current_x][column] == "  ":
                self.available_moves.append((column, current_y))