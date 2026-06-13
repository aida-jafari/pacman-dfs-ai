"""
Environment Function - Simulates the Pac-Man game world
Input: Action (1=Up, 2=Right, 3=Down, 4=Left)
Output: Percept [row, col, has_food]
"""

# Global variables to maintain world state (as specified in assignment)
_maze = None
_agent_position = None
_food_position = None
_rows = None
_cols = None

# Direction mappings
DIRECTIONS = {
    UP: (-1, 0),  # 1 = Up
    RIGHT: (0, 1),  # 2 = Right
    DOWN: (1, 0),  # 3 = Down
    LEFT: (0, -1)  # 4 = Left
}


def initialize_environment(maze, start_position, food_position):
    """Initialize the environment with maze data (called once at start)"""
    global _maze, _agent_position, _food_position, _rows, _cols
    _maze = [row[:] for row in maze]  # Deep copy
    _agent_position = start_position
    _food_position = food_position
    _rows = len(maze)
    _cols = len(maze[0])


def is_valid_position(position):
    """Check if position is within bounds and not a wall"""
    x, y = position
    return 0 <= x < _rows and 0 <= y < _cols and _maze[x][y] != '*'


def environment(action):
    """
    Environment Function as specified in assignment

    Args:
        action: Integer (1=Up, 2=Right, 3=Down, 4=Left)

    Returns:
        percept: List [row, col, has_food] where has_food is True/False
    """
    global _agent_position

    # Calculate new position based on action
    dx, dy = DIRECTIONS.get(action, (0, 0))
    new_x = _agent_position[0] + dx
    new_y = _agent_position[1] + dy
    new_position = (new_x, new_y)

    # Check if movement is valid
    if is_valid_position(new_position):
        _agent_position = new_position

    # Check if current position has food
    has_food = (_agent_position == _food_position)

    # Return percept
    return [_agent_position[0], _agent_position[1], has_food]


def get_current_position():
    """Helper to get current agent position"""
    return _agent_position


def get_food_position():
    """Helper to get food position"""
    return _food_position


def get_maze():
    """Helper to get maze"""
    return _maze