from servidor.pieces.piece import Piece
import servidor

class Rook(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)

    def check_available_moves(self, board: list[list]):
        self.available_moves = []

        # 1. Map 'e2' to x=4, y=6
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = 8 - int(self.current_pos[1])

        # 4 Cardinal directions: (delta_y, delta_x)
        directions = [
            (-1, 0),  # Up (towards rank 8 / index 0)
            (1, 0),  # Down (towards rank 1 / index 7)
            (0, -1),  # Left
            (0, 1)  # Right
        ]

        for dy, dx in directions:
            for i in range(1, 8):
                new_y = current_y + (dy * i)
                new_x = current_x + (dx * i)

                if 0 <= new_y < 8 and 0 <= new_x < 8:
                    target = board[new_y][new_x]

                    if target == "  ":
                        self.available_moves.append([servidor.letter[new_x], 8 - new_y])
                    else:
                        if self.piece[0] != target.piece[0]:
                            self.available_moves.append([servidor.letter[new_x], 8 - new_y])

                        break
                else:
                    break


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