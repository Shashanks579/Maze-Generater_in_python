import random

class Maze:
    """
    A class to generate and display a perfect maze using DepthFirst Search (DFS) with an iterative stack.
    """
    def _init_(self, width, height):
        self.width = width
        self.height = height
        # Create a grid of cells
        # Each cell is a dict with 'visited' status and 'walls'
        self.grid = [[
            {
                "visited": False,
                "walls": {"N": True, "S": True, "E": True, "W": True},
            }
            for _ in range(width)]
            for _ in range(height)]
        self.stack = []

    def find_neighbors(self, x, y):
        """Find all valid, unvisited neighbors of a cell (x, y)."""
        neighbors = []
        # (dx, dy, my_wall, neighbor_wall)
        directions = [
            (0, -1, "N", "S"),  # North
            (0, 1, "S", "N"),  # South
            (1, 0, "E", "W"),  # East
            (-1, 0, "W", "E"), # West
        ]
        for dx, dy, my_wall, neighbor_wall in directions:
            nx, ny = x + dx, y + dy
            # Check if neighbor is within bounds
            if 0 <= nx < self.width and 0 <= ny < self.height:
                # Check if neighbor is not visited
                if not self.grid[ny][nx]["visited"]:
                    neighbors.append((nx, ny, my_wall, neighbor_wall))
        return neighbors

    def remove_wall(self, x1, y1, x2, y2, my_wall, neighbor_wall):
        """Remove the wall between two adjacent cells."""
        self.grid[y1][x1]["walls"][my_wall] = False
        self.grid[y2][x2]["walls"][neighbor_wall] = False

    def generate(self):
        """Generate the maze using iterative DFS."""
        # 1. Start at a random cell
        start_x, start_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        
        # 2. Mark as visited and push to stack
        self.grid[start_y][start_x]["visited"] = True
        self.stack.append((start_x, start_y))

        # 3. Traversal Loop
        while self.stack:
            # Get current cell (top of stack)
            cx, cy = self.stack[-1]
            # Find unvisited neighbors
            neighbors = self.find_neighbors(cx, cy)

            if neighbors:
                # 4. Advance
                # Randomly choose a neighbor
                nx, ny, my_wall, neighbor_wall = random.choice(neighbors)
                # Remove wall
                self.remove_wall(cx, cy, nx, ny, my_wall, neighbor_wall)
                # Mark neighbor as visited and push to stack
                self.grid[ny][nx]["visited"] = True
                self.stack.append((nx, ny))
            else:
                # 5. Backtrack
                # No unvisited neighbors, pop from stack
                self.stack.pop()

    def display(self):
        """Display the maze as ASCII art."""
        # Print top border
        print(" " + "_" * (self.width * 2 - 1))
        for y in range(self.height):
            row_str = "|"
            for x in range(self.width):
                cell = self.grid[y][x]
                # South wall
                if cell["walls"]["S"]:
                    row_str += "_"
                else:
                    row_str += " "
                # East wall
                if cell["walls"]["E"]:
                    row_str += "|"
                else:
                    row_str += " "
            print(row_str)

# Main execution block
if _name_ == "_main_":
    print("--- Maze Generator using DFS ---")
    try:
        w = int(input("Enter maze width: "))
        h = int(input("Enter maze height: "))
        if w <= 0 or h <= 0:
            print("Dimensions must be positive integers.")
        else:
            maze = Maze(w, h)
            maze.generate()
            print("\nGenerated Maze:")
            maze.display()
    except ValueError:
        print("Invalid input. Please enter integers.")