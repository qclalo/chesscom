import tkinter as tk

def draw_arrow(canvas):
    canvas.create_line(50, 50, 150, 50, arrow=tk.LAST)  # Horizontal line
    canvas.create_line(100, 50, 100, 150, arrow=tk.LAST)  # Vertical line

# Create the main application window
root = tk.Tk()
root.title("Arrow Drawing")

# Create a canvas widget for drawing
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create a button to draw the arrow
draw_button = tk.Button(root, text="Draw Arrow", command=lambda: draw_arrow(canvas))
draw_button.pack()

# Run the Tkinter main loop
root.mainloop()
