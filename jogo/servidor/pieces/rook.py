from servidor.pieces.piece import Piece
import servidor

class Knight(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)


    def move_rook(self,move:str, board:list):
        current_x, current_y = servidor.col_map(self.current_pos[0]), int(self.current_pos[1])
        move_x, move_y = servidor.col_map(move[0]), int(move[1])
        if move in self.available_moves:
            board[current_x][current_y] = "  "
            board[move_x][move_y] = self.piece
            self.current_pos = move



    def check_available_moves(self, board: list[list]):
        self.available_moves = []
        # Assuming current_pos is stored as (row, col) integers
        current_x, current_y = self.current_pos

        # Directions: (delta_row, delta_col)
        directions = [
            (-1, 0), # Up
            (1, 0),  # Down
            (0, -1), # Left
            (0, 1)   # Right
        ]

        for dx, dy in directions:
            for i in range(1, 8):  # Check up to 7 squares away
                new_x = current_x + dx * i
                new_y = current_y + dy * i

                # Stay within the board boundaries
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target = board[new_x][new_y]

                    if target == "  ":
                        # Empty square - keep going
                        self.available_moves.append((new_x, new_y))
                    else:
                        # Logic for hitting a piece
                        # If target color != self.color: self.available_moves.append((new_x, new_y))
                        # For now, we stop at any piece to prevent jumping:
                        break
                else:
                    # Out of bounds
                    break