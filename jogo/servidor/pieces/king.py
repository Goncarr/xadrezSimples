from servidor.pieces.piece import Piece
import servidor

class King(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)

    def check_available_moves(self, board: list[list]):
        self.available_moves = []
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = 8 - int(self.current_pos[1])

        for target_y in range(current_y - 1, current_y + 2):
            for target_x in range(current_x - 1, current_x + 2):

                if 0 <= target_x < 8 and 0 <= target_y < 8:
                    if target_x == current_x and target_y == current_y:
                        continue
                    target_square = board[target_y][target_x]
                    if target_square == "  ":
                        self.available_moves.append([servidor.letter[target_x], 8 - target_y])
                    else:
                        if self.piece[0] != target_square.piece[0]:
                            self.available_moves.append([servidor.letter[target_x], 8 - target_y])

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
