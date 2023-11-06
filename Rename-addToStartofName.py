import os
import tkinter as tk
from tkinter import filedialog
import shutil

# Function to rename files
def rename_files(directory, user_input):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png', '.webp', '.txt', '.rar', '.gif', '.pdf', '.zip')):
            new_name = user_input + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

# Create a tkinter root window (this will not be shown)
root = tk.Tk()
root.withdraw()

# Ask the user for a directory containing the files to rename
directory = filedialog.askdirectory(title="Select a directory containing files to rename")

if directory:
    # Ask the user for the text to prepend to the file names
    user_input = tk.simpledialog.askstring("Input", "Enter the text to prepend to file names:")
    
    if user_input:
        # Rename the files in the selected directory
        rename_files(directory, user_input)
        print("Files renamed successfully!")
    else:
        print("User input is empty. No files were renamed.")
else:
    print("No directory selected. Operation canceled.")

root.destroy()
