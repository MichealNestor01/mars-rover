import numpy as np

DEFAULT_GRID_WIDTH = 10
DEFAULT_GRID_HEIGHT = 10

def execute(
        command: str,
        grid_width: int = DEFAULT_GRID_WIDTH,
        grid_height: int = DEFAULT_GRID_HEIGHT,
    ) -> str:
    '''mars rover kata solution'''
    loc = np.array((0, 0)) # location coordinate, (x, y)
    for char in command:
        if char == "M":
            loc += np.array((0, 1))
        # check we haven't exceeded the grid
        if loc[1] >= grid_height:
            loc[1] %= grid_height
    return f"0:{np.round(loc[1])}:N"