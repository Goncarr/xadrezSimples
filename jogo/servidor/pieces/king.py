from servidor.pieces.piece import Piece

class King(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)


    def move(self,board:list[list]):
        self.available_moves = []

        current_x, current_y = int(self.current_pos[0]), int(self.current_pos[1])

        for row in range(current_x, current_x + 3):
            for column in range(current_y, current_y + 3):
                if board[row - 1][column - 1] == "__" and (row - 1 >= 0 and column - 1 >= 0):
                    self.available_moves.append((row - 1, column - 1))

