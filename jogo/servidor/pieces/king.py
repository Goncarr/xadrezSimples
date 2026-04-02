from servidor.pieces.piece import Piece
import servidor

class King(Piece):
    def __init__(self, piece: str, current_pos):
        super().__init__(piece, current_pos)

    def check_available_moves(self, board):
        self.available_moves = []
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = 8 - int(self.current_pos[1])

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                tx, ty = current_x + dx, current_y + dy
                if 0 <= tx < 8 and 0 <= ty < 8:
                    target = board[ty][tx]
                    if target == "  " or target.piece[0] != self.piece[0]:
                        if self.is_move_legal(self, [servidor.letter[tx], 8 - ty], board):
                            self.available_moves.append([servidor.letter[tx], 8 - ty])

    def _raw_king_squares(self, king_piece):
        """Returns the 8 squares a king geometrically covers, with no legality check."""
        squares = []
        kx = servidor.letter.index(king_piece.current_pos[0])
        ky = 8 - int(king_piece.current_pos[1])
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                tx, ty = kx + dx, ky + dy
                if 0 <= tx < 8 and 0 <= ty < 8:
                    squares.append([servidor.letter[tx], 8 - ty])
        return squares

    def _get_attacked_squares(self, board):
        """
        Returns all squares attacked by enemy pieces without triggering recursion.
        Enemy kings are handled with raw geometry only — no is_move_legal call.
        """
        attacked = []
        for line in board:
            for piece in line:
                if piece == "  " or piece.piece[0] == self.piece[0]:
                    continue
                if isinstance(piece, King):
                    # Raw geometry only — calling check_available_moves here
                    # would recurse infinitely via is_move_legal -> is_in_check
                    attacked.extend(self._raw_king_squares(piece))
                else:
                    piece.check_available_moves(board)
                    attacked.extend(piece.available_moves)
        return attacked

    def is_in_check(self, board):
        attacked_squares = self._get_attacked_squares(board)
        # current_pos is a string like "e1", attacked_squares contains lists like ['e', 1]
        king_pos = [self.current_pos[0], int(self.current_pos[1])]
        return king_pos in attacked_squares

    def is_move_legal(self, piece, target_pos, board):
        original_pos = piece.current_pos
        target_x = servidor.letter.index(target_pos[0])
        target_y = 8 - int(target_pos[1])
        original_target_sq = board[target_y][target_x]

        old_x, old_y = servidor.letter.index(original_pos[0]), 8 - int(original_pos[1])
        board[old_y][old_x] = "  "
        board[target_y][target_x] = piece
        # Store as string to stay consistent with how current_pos is normally stored
        piece.current_pos = target_pos[0] + str(target_pos[1])

        in_check = self.is_in_check(board)

        board[old_y][old_x] = piece
        board[target_y][target_x] = original_target_sq
        piece.current_pos = original_pos

        return not in_check

    def is_checkmate(self, board):
        stalemate = True
        for row in board:
            for piece in row:
                if piece != "  " and piece.piece[0] == self.piece[0]:
                    piece.check_available_moves(board)
                    if piece.available_moves:
                        stalemate = False

        if not self.is_in_check(board) and stalemate:
            return 2

        elif not self.is_in_check(board) and not stalemate:
            return False

        stalemate = True
        for row in board:
            for piece in row:
                if piece != "  " and piece.piece[0] == self.piece[0]:
                    piece.check_available_moves(board)
                    if piece.available_moves:
                        stalemate = False
                    if stalemate:
                        return 2
                    for move in piece.available_moves:
                        if self.is_move_legal(piece, move, board):
                            return False

        return 1

    def move(self, piece: Piece, move_requested: str, board: list):
        current_x, current_y = servidor.letter.index(self.current_pos[0]), 8 - int(self.current_pos[1])
        move_x, move_y = move_requested[0], int(move_requested[1])
        move = [move_x, move_y]
        if move in self.available_moves:
            move[0] = servidor.letter.index(move[0])
            board[current_y][current_x] = "  "
            board[8 - move[1]][move[0]] = piece
            self.current_pos = move_requested