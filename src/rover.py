import numpy as np

DEFAULT_GRID_WIDTH = 10
DEFAULT_GRID_HEIGHT = 10
DEFAULT_MOVEMENT_MAP = {
    "M": 1.0, # by default M command means go in current direction 1 unit
}
DEFAULT_ROTATION_MAP = {
    "L": -np.pi/2,
    "R": np.pi/2,
}
DEFAULT_ROUND_TO = 5
DEFAULT_ORIENTATION_MAP = { # angle from the y-axis in radians
    0:  "N",
    np.round(np.pi/2, DEFAULT_ROUND_TO):  "E",
    np.round(np.pi, DEFAULT_ROUND_TO): "S",
    np.round(-np.pi, DEFAULT_ROUND_TO): "S", # accept +-pi to mean south 
    np.round(-np.pi/2, DEFAULT_ROUND_TO): "W",
}

def _rotate_clockwise(vector: np.ndarray[float], theta: float) -> np.ndarray[float]:
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    rotation_matrix = np.array((
        (cos_theta, sin_theta),
        (-sin_theta, cos_theta)
    ))
    return rotation_matrix @ vector

def _update_location(
        loc: np.ndarray[float], 
        rot: np.ndarray[float],
        obstacles: list[np.ndarray[float]],
        movement_scalar: float
    ) -> list[np.ndarray, bool]: # new_loc, hit_obstacle 
    if len(obstacles):
        new_loc = loc + (movement_scalar * rot)
        for o in obstacles: 
            if np.allclose(o, new_loc):
                return loc, True
        return new_loc, False
    return loc + (movement_scalar * rot), False

def execute(
        command: str,
        grid_width: int = DEFAULT_GRID_WIDTH,
        grid_height: int = DEFAULT_GRID_HEIGHT,
        movement_map: dict[str, float] = DEFAULT_MOVEMENT_MAP,
        rotation_map: dict[str, float] = DEFAULT_ROTATION_MAP,
        orientation_map: dict[float, str] = DEFAULT_ORIENTATION_MAP,
        obstacles: list[np.ndarray[float]] = [],
        round_to: int = DEFAULT_ROUND_TO,
    ) -> str:
    '''mars rover kata solution'''

    loc, rot = np.array((0.0, 0.0)), np.array((0.0, 1.0)) # start (0,0) looking north
    hit_obstacle = False

    # move the robot
    for char in command:
        if char in movement_map:
            loc, hit_obstacle = _update_location(loc, rot, obstacles, movement_map.get(char))
            if hit_obstacle:
                break
        elif char in rotation_map:
            rot = _rotate_clockwise(rot, rotation_map.get(char))
        #  ensure grid isn't exceeded
        loc[0] %= grid_width
        loc[1] %= grid_height
    
    # convert the rotation matrix to angle from (0, 1) and format the output string
    rot_angle = np.round(np.arctan2(*rot), round_to)
    orientation = orientation_map.get(rot_angle, "N")
    x_val, y_val = np.round(loc).astype(int)
    return_string = f"{x_val}:{y_val}:{orientation}"
    if hit_obstacle:
        return f"O:{return_string}"
    return return_string