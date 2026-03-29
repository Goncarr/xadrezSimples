# dicionário com as coordenadas das peças brancas
from servidor.pieces.pawn import Pawn

wpawn = Pawn("wP", "a1")
wpawn2 = Pawn("wP", "b1")
wpawn3 = Pawn("wP", "c1")
wpawn4 = Pawn("wP", "d1")
wpawn5 = Pawn("wP", "e1")
wpawn6 = Pawn("wP", "f1")
wpawn7 = Pawn("wP", "g1")
wpawn8 = Pawn("wP", "h1")

DEFAULT_WHITE_BOARD_MAP = {
    "wP": [wpawn, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8]
}


"""
DEFAULT_WHITE_BOARD_MAP = {
    "wP": ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
    "wN": ["b0", "g0"],
    "wB": ["c0", "f0"],
    "wR": ["a0", "h0"],
    "wQ": ["d0"],
    "wK": ["e0"],
}
"""
bpawn = Pawn("bP", "a6")
bpawn2 = Pawn("bP", "b6")
bpawn3 = Pawn("bP", "c6")
bpawn4 = Pawn("bP", "d6")
bpawn5 = Pawn("bP", "e6")
bpawn6 = Pawn("bP", "f6")
bpawn7 = Pawn("bP", "g6")
bpawn8 = Pawn("bP", "h6")

DEFAULT_BLACK_BOARD_MAP = {
    "bP": [bpawn, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8],
}

"""
# dicionário com as coordenadas das peças pretas
DEFAULT_BLACK_BOARD_MAP = {
    "bP": ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    "bN": ["b7", "f7"],
    "bB": ["c7", "g7"],
    "bR": ["a7", "h7"],
    "bQ": ["d7"],
    "bK": ["e7"],
}
"""

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