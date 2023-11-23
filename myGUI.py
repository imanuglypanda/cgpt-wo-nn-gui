import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph_Learner import doc_graph

# Sample data for graph
mynums = [x for x in range(50)]

# Initialize Graph Learner
g = doc_graph(5)
g.add_doc(mynums)

# Function to get numbers from entry and display result
def get_numbers():
    # Get the input values from the entry widget
    input_values = entry.get()

    # Convert the input string to a list of numbers
    numbers = [int(num) for num in input_values.split()]
    
    # Generate result using Graph Learner
    output = g.gen_next(numbers, 5)
    
    # Display the result
    result_label.config(text=f"Result: {output}")
    
    # Create and display the line graph
    create_line_graph(numbers)

# Function to upload a file and populate the entry widget
def upload_file():
    # Open a file dialog to allow the user to select a file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    # Check if a file was selected
    if file_path:
        # Open the selected file for reading
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Clear the current content of the entry widget
            entry.delete(0, tk.END)
            
            # Insert the content of the file into the entry widget
            entry.insert(0, content)

# Function to create and display a line graph
def create_line_graph(numbers):
    # Clear the previous graph (if any)
    if hasattr(create_line_graph, 'ax'):
        create_line_graph.ax.clear()
    else:
        # Create a line chart using Matplotlib for the first time
        fig, ax = plt.subplots()
        ax.set_xlabel('Steps')
        ax.set_ylabel('Values')
        ax.set_title('Input Numbers')
        create_line_graph.ax = ax

    # Draw the new graph
    create_line_graph.ax.plot(range(len(numbers)), numbers, marker='o')

    # Embed the Matplotlib graph in the Tkinter window
    if hasattr(create_line_graph, 'canvas'):
        create_line_graph.canvas.get_tk_widget().destroy()

    create_line_graph.canvas = FigureCanvasTkAgg(create_line_graph.ax.figure, master=learning_page)
    canvas_widget = create_line_graph.canvas.get_tk_widget()
    canvas_widget.pack()

# Main program part
window = tk.Tk()
window.geometry('800x600')
window.title("Graph Creation Phase")

# Create a notebook for navigation
notebook = ttk.Notebook(window)

# Create a page for Learning Page
learning_page = tk.Frame(notebook)
notebook.add(learning_page, text="Learning Phase")

# Create a button to upload a file
upload_button = tk.Button(learning_page, text="Upload File", command=upload_file)
upload_button.pack()

# Create a label and entry widget for input on the graph page
input_label = tk.Label(learning_page, text="Enter numbers (separated by space) or upload a file: ")
input_label.pack()

entry = tk.Entry(learning_page)
entry.pack()

# Create a button to trigger the calculation on the graph page
calculate_button = tk.Button(learning_page, text="Show", command=get_numbers)
calculate_button.pack()

# Create a label to display the result on the graph page
result_label = tk.Label(learning_page, text="Result: ")
result_label.pack()

# Create a page for Prediction Page
predict_page = tk.Frame(notebook)
notebook.add(predict_page, text="Predict Phase")

# Create a label for Prediction Page
predict_page_label = tk.Label(predict_page, text="Prediction Phase")
predict_page_label.pack()

# Create a page for Evaluation Page
evaluation_page = tk.Frame(notebook)
notebook.add(evaluation_page, text="Evaluation Phase")

# Create a label for Evaluation Page
evaluation_page_label = tk.Label(evaluation_page, text="Evaluation Phase")
evaluation_page_label.pack()

# Pack the notebook
notebook.pack(fill=tk.BOTH, expand=True)

# Start the tkinter event loop
window.mainloop()
