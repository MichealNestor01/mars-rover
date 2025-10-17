import numpy as np

def execute(command: str) -> str:
    loc = np.array((0, 0)) # location coordinate, (x, y)
    for char in command:
        if char == "M":
            loc += np.array((0, 1))
    return f"0:{np.round(loc[1])}:N"