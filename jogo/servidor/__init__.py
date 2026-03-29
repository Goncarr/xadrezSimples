# dicionário com as coordenadas das peças brancas
from servidor.pieces.pawn import Pawn
pawn = Pawn("wP", )

DEFAULT_WHITE_BOARD_MAP = {
    "wP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "wN": [(7, 1), (7, 6)],
    "wB": [(7, 2), (7, 5)],
    "wR": [(7, 0), (7, 7)],
    "wQ": [(7, 3)],
    "wK": [(7, 4)],
}

# dicionário com as coordenadas das peças pretas
DEFAULT_BLACK_BOARD_MAP = {
    "bP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "bN": [(0, 1), (0, 6)],
    "bB": [(0, 2), (0, 5)],
    "bR": [(0, 0), (0, 7)],
    "bQ": [(0, 3)],
    "bK": [(0, 4)],
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

COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "obj_obj  "
SYM_OP = "sym      "
SUB_OP = "sub      "
BYE_OP = "bye      "
END_OP = "stop     "
PORT = 35000
SERVER_ADDRESS = "localhost"