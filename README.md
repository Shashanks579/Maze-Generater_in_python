Python Maze Generator (Iterative DFS)
This is a Python script that generates a "perfect" maze—a maze with no loops and exactly one path between any two cells. It uses an iterative Depth-First Search (DFS) algorithm and renders the output as ASCII art in the console.
How It Works
The project is built around a single Maze class that encapsulates the grid state and all necessary logic.
 * Initialization: A grid is created as a 2D list. Each cell is a dictionary storing its visited status and the state of its four walls (North, South, East, West).
 * Generation Algorithm (Iterative DFS):
   * A random cell is chosen, marked as visited, and pushed onto an explicit stack.
   * The algorithm loops as long as the stack is not empty.
   * It looks at the cell on top of the stack (without popping it) and finds all of its unvisited neighbors.
   * If unvisited neighbors are found:
     * One neighbor is chosen at random.
     * The wall between the current cell and the chosen neighbor is "removed" (both booleans in their respective walls dicts are set to False).
     * The chosen neighbor is marked as visited and pushed onto the stack.
   * If no unvisited neighbors are found:
     * The current cell is a "dead end."
     * It is pop()-ed from the stack, and the algorithm backtracks to the previous cell.
 * Display: The display method iterates through the grid and builds each row of text. It efficiently renders the entire maze by only checking the South and East walls for each cell.
