import tkinter as tk

# Canvas size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40  # Each cell's size
ERASER_SIZE = 20  # Eraser size

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Tool in Tkinter")

        # Canvas setup
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Grid of blue cells
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="white")
                self.cells.append(cell)

        # Create Eraser (invisible, just used for tracking)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="black", width=1)

        # Bind mouse drag event to erasing function
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        """Function to erase cells when the eraser moves over them."""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

        # Check which cells overlap with eraser and change their color to white
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping:
            if item in self.cells:  # Only erase grid cells, not the eraser
                self.canvas.itemconfig(item, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
