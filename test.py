import tkinter as tk

# Function to move the circle
def move_circle():
    global x, y, x_speed
    
    # Clear the canvas
    canvas.delete("all")
    
    # Draw the circle in a new position
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="blue", outline="black", tags="circle")
    
    # Update the x-coordinate
    x += x_speed
    
    # Repeat the function after a delay
    canvas.after(10, move_circle)

# Create the main window
root = tk.Tk()
root.geometry("600x400")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Set initial values
x = 50  # x-coordinate of the circle's center
y = 200  # y-coordinate of the circle's center
radius = 20  # radius of the circle
x_speed = 1  # pixels per frame

# Start the animation
move_circle()

# Start the main loop
root.mainloop()
