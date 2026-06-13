"""
Pac-Man AI - DFS Pathfinding
Artificial Intelligence Course Project

Finds food in a maze using Depth-First Search algorithm.
Outputs: Start position, Food position, Number of moves, Movement sequence
"""

# Define direction constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def is_valid_position(maze, position):
    """Check if a position is valid (within bounds and not a wall)"""
    x, y = position
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '*'


def read_map_from_file(file_name):
    """Read the maze, agent start position, and food position from the file"""
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Remove empty lines and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]

    # Parse dimensions
    dimensions = lines[0].strip()
    rows, cols = map(int, dimensions.split(','))

    # Parse agent's start position
    start_line = lines[1].strip()
    start_x, start_y = map(int, start_line.split(','))
    start_position = (start_x, start_y)

    # Parse maze layout (remaining lines)
    maze = []
    for line in lines[2:]:
        if line.strip():
            maze.append(list(line.strip()))

    # Ensure maze has correct dimensions
    if len(maze) != rows:
        print(f"Warning: Expected {rows} rows, got {len(maze)}")

    # Find food position
    food_position = None
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'f':
                food_position = (x, y)
                break
        if food_position:
            break

    return maze, start_position, food_position


def dfs(maze, current_position, goal_position, path, visited, memory):
    """DFS function for finding the path to food"""
    if current_position == goal_position:
        # Mark food in memory
        memory[current_position[0]][current_position[1]] = 'f'
        return True

    visited.add(current_position)
    x, y = current_position

    # Update memory map based on the cell type
    if maze[x][y] == '-' or maze[x][y] == 'a':
        memory[x][y] = '-'
    elif maze[x][y] == '*':
        memory[x][y] = '*'

    # Define possible movements with directions
    # Order matters for DFS - can be changed to explore different paths
    directions = [
        ((0, 1), RIGHT),  # Right
        ((1, 0), DOWN),  # Down
        ((0, -1), LEFT),  # Left
        ((-1, 0), UP)  # Up
    ]

    for (dx, dy), action in directions:
        new_x, new_y = current_position[0] + dx, current_position[1] + dy
        new_position = (new_x, new_y)

        if is_valid_position(maze, new_position) and new_position not in visited:
            path.append((current_position, action, new_position))
            if dfs(maze, new_position, goal_position, path, visited, memory):
                return True  # Food found
            path.pop()  # Backtrack if this path doesn't lead to food

    visited.remove(current_position)
    return False


def format_output(start_position, food_position, path):
    """Format output exactly as required by the assignment"""
    # Build the movement sequence list
    movement_sequence = []

    for step in path:
        current_pos, action, new_pos = step
        if not movement_sequence:  # First step
            movement_sequence.append(current_pos)
        movement_sequence.append(action)
        movement_sequence.append(new_pos)

    return movement_sequence


def print_output(start_position, food_position, path, memory):
    """Print output in the exact format specified"""
    print(start_position)
    print(food_position)
    print(len(path))

    # Print movement sequence
    movement_seq = format_output(start_position, food_position, path)
    print(movement_seq)

    # Print memory map (bonus - optional)
    print("\nMemory Map After Exploration:")
    for row in memory:
        print(''.join(row))


def main():
    # Read input file
    input_file = 'maps.txt'  # Change this to your file path

    try:
        maze, start_position, food_position = read_map_from_file(input_file)
    except FileNotFoundError:
        print(f"Error: Could not find {input_file}")
        print("Creating a sample map...")

        # Create a simple sample map for demonstration
        maze = [
            ['*', '*', '*', '*', '*'],
            ['*', 'a', '-', '-', '*'],
            ['*', '*', '*', '-', '*'],
            ['*', '-', '-', 'f', '*'],
            ['*', '*', '*', '*', '*']
        ]
        start_position = (1, 1)
        food_position = (3, 3)

    # Prepare DFS search
    path = []
    visited = set()

    # Initialize memory map
    memory = [['?' if cell == '-' or cell == 'a' else '*' if cell == '*' else '?' for cell in row] for row in maze]

    # Run DFS to find path
    found = dfs(maze, start_position, food_position, path, visited, memory)

    if found:
        print_output(start_position, food_position, path, memory)
    else:
        print("No path found to food!")


if __name__ == "__main__":
    main()