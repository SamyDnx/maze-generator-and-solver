# Maze Generator and Solver

This project is a Python-based maze generator and solver using the `pygame` library. It visualizes both the creation of mazes and the process of solving them with the BFS (Breadth-First Search) algorithm. The project also allows the user to introduce loops into the maze, making it more complex and interesting.

## Features

- **Maze Generation**:
  - Uses a randomized version of Prim's algorithm to create a perfect maze (a maze with no loops).
  - Option to introduce loops to create a non-perfect maze, adding complexity.
- **Maze Solving**:
  - Visualizes the pathfinding process using Breadth-First Search (BFS).
  - Shows the cells visited by the algorithm.
- **Interactivity**:
  - Generate new mazes on demand.
  - Solve the maze and visualize the path and visited cells.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SamyDnx/maze-generator-solver.git
   cd maze-generator-solver
   ```

2. **Install Dependencies**:
   This project requires Python 3.x and the `pygame` library.
   You can install `pygame` using pip:
   ```bash
   pip install pygame
   ```

## How to Run

1. After installing the dependencies, run the `main.py` file:
   ```bash
   python main.py
   ```

2. Use the controls below to interact with the maze generation and solving process.

## Controls

- **`SPACE`**: Solve the maze and display the solution path.
- **`E`**: Show the visited cells during the search process.
- **`R`**: Generate a new random maze.
- **`BACKSPACE`**: Clear the solution path and visited cells.

## Maze Generation

The maze is generated using a recursive backtracking algorithm, starting from the top-left corner. The maze grid consists of walls (`1`) and open paths (`0`). The algorithm digs through walls to create paths and recursively explores the grid.

- **Recursive Maze Generation**: 
  ```python
  def generate_maze(x=0, y=0):
      ...
  ```

- **Adding Loops to the Maze**:
  Loops are introduced to make the maze more complex. A small chance (configurable) allows certain walls to be removed to create multiple possible solutions.
  ```python
  def create_loops(maze, chance=0.05):
      ...
  ```

## Maze Solving

The maze is solved using the Breadth-First Search (BFS) algorithm. BFS guarantees finding the shortest path from the start point to the goal point in the maze.

- **BFS Pathfinding**: 
  ```python
  def bfs_solve(maze, start, goal):
      ...
  ```

## Visualization

- **Maze**: The maze grid is visualized with white cells for paths and black cells for walls. As the solver works, the solution path is drawn in **green**, and the visited cells are drawn in **red**.
  ```python
  def draw_maze(maze):
      ...
  ```

- **Solution Path**: The solution path is highlighted in green once the maze is solved.
  ```python
  def draw_path(path, color):
      ...
  ```

- **Visited Cells**: Cells visited by the BFS algorithm are shown in red, allowing you to observe how the algorithm explores the maze.
  ```python
  def draw_visited(visited, color):
      ...
  ```

## Code Overview

- **Maze Generation**: 
  The maze generation algorithm carves paths by recursively visiting neighbors and removing walls. It uses the grid layout where odd-numbered rows and columns are walls, and even-numbered rows and columns are paths.

  ```python
  def generate_maze():
      ...
  ```

- **Pathfinding**: 
  The BFS algorithm is used to find the shortest path from the start to the goal. The algorithm explores the maze level by level, ensuring that the shortest path is found.

  ```python
  def bfs_solve():
      ...
  ```

- **Interactive Drawing**: 
  The maze and the algorithm's progress are drawn in real-time using `pygame`’s rendering capabilities. The `draw_path` and `draw_visited` functions update the display as the algorithm runs.

  ```python
  def draw_maze():
      ...
  def draw_path():
      ...
  def draw_visited():
      ...
  ```

## Future Improvements

- **DFS Solver**: Add support for solving the maze using Depth-First Search (DFS).
- **A* Algorithm**: Implement the A* search algorithm for a more efficient pathfinding solution.
- **Custom Maze Sizes**: Allow users to configure the maze dimensions and complexity.
- **Maze Editing**: Provide a feature to manually edit the maze before solving.

## Acknowledgements

This project was built using the `pygame` library and inspired by classic maze generation and solving algorithms.

---

Feel free to contribute by adding new features, optimizing the algorithms, or improving the visualizations!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
