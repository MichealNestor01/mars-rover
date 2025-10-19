import numpy as np

DEFAULT_GRID_WIDTH = 10
DEFAULT_GRID_HEIGHT = 10
DEFAULT_MOVEMENT_MAP = {
    "M": 1, # by default M command means go in current direction 1 unit
}
DEFAULT_ROTATION_MAP = {
    "L": -np.pi/2,
    "R": np.pi/2,
}
DEFAULT_TOLERANCE = 5
DEFAULT_ORIENTATION_MAP = { # angle from the y-axis in radians
    0:  "N",
    np.round(np.pi/2, DEFAULT_TOLERANCE):  "E",
    np.round(np.pi, DEFAULT_TOLERANCE): "S",
    np.round(-np.pi, DEFAULT_TOLERANCE): "S", # accept +-pi to mean south :)
    np.round(-np.pi/2, DEFAULT_TOLERANCE): "W",
}

def execute(
        command: str,
        grid_width: int = DEFAULT_GRID_WIDTH,
        grid_height: int = DEFAULT_GRID_HEIGHT,
        movement_map: dict[str, float] = DEFAULT_MOVEMENT_MAP,
        rotation_map: dict[str, float] = DEFAULT_ROTATION_MAP,
        orientation_map: dict[float, str] = DEFAULT_ORIENTATION_MAP,
        tolerance: int = 5,
    ) -> str:
    '''mars rover kata solution'''
    loc = np.array((0, 0)) # location vector, (x, y)
    rot = np.array((0, 1)) # direction vector, starting looking north to (0, 1)
    for char in command:
        if char in movement_map:
            loc += movement_map.get(char) * rot
        elif char in rotation_map:
            theta = rotation_map.get(char)
            sin_theta = np.sin(theta)
            cos_theta = np.cos(theta)
            rotation_matrix = np.array((
                (cos_theta, sin_theta),
                (-sin_theta, cos_theta)
            ))
            rot = rotation_matrix @ rot
        # check we haven't exceeded the grid
        if loc[1] >= grid_height:
            loc[1] %= grid_height
    # to convert the rotation vector into an angle from the y axis
    rot_angle = np.round(np.arctan2(*rot), tolerance)
    return f"0:{np.round(loc[1])}:{orientation_map.get(rot_angle, "N")}"