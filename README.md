\# Pac-Man AI - DFS Pathfinding



\## Artificial Intelligence Course Project



An intelligent Pac-Man agent that finds food in a maze using \*\*Depth-First Search (DFS)\*\* algorithm. The agent perceives its environment through sensors and makes decisions based solely on percepts, following the classic AI agent architecture.



\---



\## Project Overview



This project implements a goal-based agent for the Pac-Man game with the following features:



\- \*\*DFS Algorithm\*\* with two goal-testing strategies (at node expansion time)

\- \*\*Environment Function\*\* – Simulates the game world, processes actions, returns percepts

\- \*\*Agent Function\*\* – Maintains internal state, chooses actions based on percept history

\- \*\*Random Map Generation\*\* – Bonus feature for dynamic maze creation

\- \*\*Graphical Visualization\*\* – Bonus feature to visualize the path



\### Course Details

\- \*\*Course:\*\* Artificial Intelligence \& Expert Systems

\- \*\*Assignment:\*\* Project 1 - Pac-Man AI

\- \*\*Date:\*\* \[Your semester/year]



\---



\## How It Works



\### Architecture



┌─────────────┐ Action ┌─────────────┐

│ Agent │ ────────► │ Environment │

│ (AI Brain) │ │ (World) │

│ │ ◄──────── │ │

└─────────────┘ Percept └─────────────┘





\### Agent Function

\- Input: Percept (current position + cell type)

\- Output: Action (Up=1, Right=2, Down=3, Left=4)

\- Internal memory: Stores percept history



\### Environment Function

\- Input: Action

\- Output: Percept (new position, cell contains food? yes/no)

\- Maintains: Grid state, wall positions, agent location, food location



\### DFS Implementation

\- Two goal-testing approaches:

&#x20; 1. Test when expanding node

&#x20; 2. Test when generating node

\- Returns: Path from start to food as sequence of actions



\---



\## Input Format (TXT File)

rows columns

start\_row start\_col

(empty line)

map\_grid...





\*\*Legend:\*\*

\- `\*` = Wall

\- `a` = Agent (Pac-Man) starting position

\- `f` = Food (goal)

\- `.` = Empty space



\---



\## Output Format



The program outputs exactly:



1\. \*\*Start position\*\* – Tuple `(row, col)`

2\. \*\*Food position\*\* – Tuple `(row, col)`

3\. \*\*Number of moves\*\* – Integer

4\. \*\*Movement sequence\*\* – List of alternating positions and actions

5\. \*\*Memory trace\*\* – Bonus feature (visited nodes history)



\### Example Output:

(2, 4)

(3, 6)

3

\[(2, 4), 2, (2, 5), 2, (2, 6), 3, (3, 6)]





\### Direction Mapping:

| Action | Direction |

|--------|-----------|

| 1 | Up |

| 2 | Right |

| 3 | Down |

| 4 | Left |



\---



\## 🚀 How to Run



\### Prerequisites

\- Python 3.8+



\### Run the program:

```bash

\# Navigate to project folder

cd pacman-dfs-ai



\# Run with default map

python src/main.py maps/map1.txt



\# Run with random map (bonus)

python src/main.py --random 10 10

