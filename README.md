# Maze Solver

This project generates a random maze using recursive backtracking and introduces loops to create multiple possible paths. It includes implementations of two algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to solve the maze. The solution paths and visited cells can be visualized in real-time using Pygame.

## Features

- Random maze generation using recursive backtracking.
- Optional loop creation to introduce multiple paths in the maze.
- Maze-solving using BFS and DFS.
- Visualization of both solution paths and visited cells for each algorithm.
- User controls to interact with and reset the maze.

## Installation

To run the program, you need to have Python installed along with the `pygame` library. You can install `pygame` via `pip`:

```bash
pip install pygame
```

## How to Run

After installing the dependencies, you can run the script by executing:

```bash
python maze_solver.py
```

A window will appear displaying a randomly generated maze. You can use the keyboard controls to solve the maze using either BFS or DFS.

## Controls

- **Spacebar**: Show/hide the solution path.
- **E**: Show/hide the visited cells.
- **B**: Solve the maze using BFS.
- **D**: Solve the maze using DFS.
- **R**: Regenerate the maze.
- **Backspace**: Clear all paths and visited cells.

## Code Overview

### Maze Generation

The maze is generated using the `generate_maze` function, which employs recursive backtracking to create a perfect maze (one path between any two points). The `create_loops` function introduces loops by randomly removing walls with a certain chance.

```python
def generate_maze(x=0, y=0):
    # Recursive backtracking to generate the maze
    ...

def create_loops(maze, chance=0.05):
    # Randomly removes walls to introduce loops
    ...
```

### BFS and DFS Solvers

The BFS and DFS algorithms are implemented to solve the maze. Each algorithm returns the solution path and the set of visited cells.

```python
def bfs_solve(maze, start, goal):
    # Breadth-First Search to solve the maze
    ...

def dfs_solve(maze, start, goal):
    # Depth-First Search to solve the maze
    ...
```

### Drawing Functions

The drawing functions are responsible for visualizing the maze, solution paths, and visited cells in the Pygame window.

```python
def draw_maze(maze):
    # Draws the maze grid
    ...

def draw_path(path, color):
    # Draws the solution path
    ...

def draw_visited(visited, color):
    # Draws the visited cells
    ...
```

## Customization

- **Maze Size**: The maze size can be adjusted by changing the `ROWS` and `COLLS` constants.
- **Cell Size**: You can modify the `CELL_SIZE` to scale the maze cells.
- **Loop Chance**: Adjust the `CHANCE` constant to control how often loops are introduced in the maze.

## Example

Here is an example of a randomly generated maze and its solution using DFS (blue) and BFS (green).

![Maze Solver Example](./example_maze.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Notes:
- Replace `./images/example_maze.png` with the actual path to a sample screenshot of your project, if available.
- You can also add more details or sections as necessary, such as known issues or future improvements.
