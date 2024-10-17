# Maze Generator and Solver

This project is a Python-based maze generator and solver using the `pygame` library. The maze is generated using recursive backtracking, and the solver uses breadth-first search (BFS). The generated maze can optionally contain loops to create more complex and challenging mazes. The program features a visual interface to generate, solve, and display the maze and the solution paths.

## Features

- **Maze Generation**: Generates a random maze using recursive backtracking.
- **Maze with Loops**: Adds loops to the maze by randomly removing walls to create multiple paths.
- **Maze Solving**:
  - **Breadth-First Search (BFS)**: Solves the maze and displays the solution path.
  - **Depth-First Search (DFS)**: Planned feature (to be implemented).
- **Visualization**: Visualizes both the maze generation and the solving process.
- **Interactivity**: 
  - Press `SPACE` to toggle showing/hiding the BFS solution path.
  - Press `E` to toggle showing/hiding the visited nodes during BFS.
  - Press `BACKSPACE` to clear the solution and visited paths.
  - Press `R` to regenerate the maze.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SamyDnx/maze-generator-solver.git
   cd maze-generator-solver
