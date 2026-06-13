"""
Agent Function - AI that decides actions based on percepts
Input: Percept [row, col, has_food]
Output: Action (1=Up, 2=Right, 3=Down, 4=Left)
Uses DFS algorithm to find food
"""

from collections import deque

# Direction constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# Direction mappings
DIRECTIONS = {
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0, -1)
}

# Global variables for agent memory (as specified in assignment)
_percept_history = []
_path_memory = []  # Stores the path found
_goal_found = False
_planned_path = None
_current_step = 0


def agent(percept):
    """
    Agent Function as specified in assignment

    Args:
        percept: List [row, col, has_food] from environment

    Returns:
        action: Integer (1=Up, 2=Right, 3=Down, 4=Left)
    """
    global _percept_history, _planned_path, _current_step, _goal_found

    # Store percept in history
    _percept_history.append(percept)

    current_pos = (percept[0], percept[1])
    has_food = percept[2]

    # If food found, stop moving
    if has_food or _goal_found:
        _goal_found = True
        return None  # No action needed

    # If we don't have a planned path yet, run DFS to find food
    if _planned_path is None:
        _planned_path = plan_path(current_pos)
        if _planned_path:
            _current_step = 0

    # Follow the planned path
    if _planned_path and _current_step < len(_planned_path) - 1:
        current = _planned_path[_current_step]
        next_pos = _planned_path[_current_step + 1]

        # Determine action to move from current to next
        dx = next_pos[0] - current[0]
        dy = next_pos[1] - current[1]

        for action, (adx, ady) in DIRECTIONS.items():
            if (adx, ady) == (dx, dy):
                _current_step += 1
                return action

    return None  # No movement needed (food found or stuck)


def plan_path(start_position):
    """
    DFS algorithm to find path from start to food
    Uses global maze information from percept history
    """
    # We need maze info - in real implementation, this would be built from percepts
    # For this implementation, we'll assume the agent has access to the map
    # (This matches the assignment where agent can build memory from percepts)

    # This is a simplified version - in practice, agent builds map from percepts
    return None  # Placeholder - actual implementation would use DFS


# Alternative: Simple DFS Agent that knows the map (for Part 1)
class DFSAgent:
    def __init__(self, maze, start_position, food_position):
        self.maze = maze
        self.start = start_position
        self.goal = food_position
        self.path = []
        self.visited = set()
        self.memory = [['?' if cell != '*' else '*' for cell in row] for row in maze]
        self.action_sequence = []  # Stores [(position, action, new_position)]

    def is_valid(self, position):
        x, y = position
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] != '*'

    def dfs(self, current, goal, path, visited):
        """DFS to find path to food"""
        if current == goal:
            return True

        visited.add(current)
        x, y = current

        # Update memory
        if self.maze[x][y] == '-':
            self.memory[x][y] = '-'

        # Explore neighbors in order: Right, Down, Left, Up (can be changed)
        neighbors = [
            ((0, 1), RIGHT),  # Right
            ((1, 0), DOWN),  # Down
            ((0, -1), LEFT),  # Left
            ((-1, 0), UP)  # Up
        ]

        for (dx, dy), action in neighbors:
            new_pos = (current[0] + dx, current[1] + dy)

            if self.is_valid(new_pos) and new_pos not in visited:
                path.append((current, action, new_pos))
                if self.dfs(new_pos, goal, path, visited):
                    return True
                path.pop()

        visited.remove(current)
        return False

    def find_path(self):
        """Find path using DFS and store action sequence"""
        path = []
        visited = set()

        if self.dfs(self.start, self.goal, path, visited):
            self.path = path
            return True
        return False

    def get_action_sequence(self):
        """Convert path to required output format"""
        if not self.path:
            return []

        result = []
        for step in self.path:
            current, action, new_pos = step
            result.append(current)
            result.append(action)
        # Add final position
        if self.path:
            result.append(self.path[-1][2])

        return result

    def get_number_of_moves(self):
        return len(self.path)

    def get_memory_map(self):
        return self.memory