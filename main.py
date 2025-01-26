import tkinter as tk
from tkinter import filedialog
import os

def browse_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file = file_path
        label.config(text=f"Selected File:\n{file_path}")
        convert_button.pack(pady=10)

def process_file():
    if selected_file:
        output_file = f"{os.path.splitext(selected_file)[0]}_output{os.path.splitext(selected_file)[1]}"
        
        with open(selected_file, "rb") as f:
            data = f.read()[12:]
        
        with open(output_file, "wb") as f:
            f.write(data)
        
        label.config(text=f"Processed file saved as:\n{output_file}")

root = tk.Tk()
root.title("Remove Header")
root.geometry("400x250")

selected_file = None

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

label = tk.Label(root, text="No file selected", wraplength=380)
label.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=process_file)
convert_button.pack_forget()

root.mainloop()