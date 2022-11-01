from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value to
        x (int): _description_
        y (int): _description_
    Returns:
        List[str]: Modified board
    """

    # Step 1: Ensure the x and y are going to be within bounds.
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board):return

    # Step 2: We want to check whether the current position will equal the old value.
    if input_board[y][x] != old:
        return

    # Step 3: Set current position to the new value.
    input_board[y][x] = new

    # Step 4: Try to fill the neighboring positions.
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

    # raise NotImplementedError


ans = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in ans:
    print(a)