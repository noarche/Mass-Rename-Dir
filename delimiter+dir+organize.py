import os
import tkinter as tk
from tkinter import filedialog

def move_files(directory_path, delimiter, status_text):
    try:
        # Get a list of all files in the specified directory
        files = os.listdir(directory_path)

        for file in files:
            # Check if the file name contains the specified delimiter
            if delimiter in file:
                # Extract the directory name up to the delimiter
                new_directory = file.split(delimiter)[0]

                # Create the new directory if it doesn't exist
                new_directory_path = os.path.join(directory_path, new_directory)
                os.makedirs(new_directory_path, exist_ok=True)

                # Move the file to the new directory
                old_file_path = os.path.join(directory_path, file)
                new_file_path = os.path.join(new_directory_path, file)
                os.rename(old_file_path, new_file_path)

        status_text.set("Files moved successfully!")

    except Exception as e:
        status_text.set(f"Error: {str(e)}")


def browse_button(entry_var):
    directory_path = filedialog.askdirectory()
    entry_var.set(directory_path)


def main():
    # Create the main window
    window = tk.Tk()
    window.title("File Organizer")
    window.geometry("300x200")
    window.resizable(False, False)
    window.configure(bg='black')

    # Create a label and entry for the directory path
    directory_label = tk.Label(window, text="Directory Path:", bg='black', fg='white')
    directory_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    directory_var = tk.StringVar()
    directory_entry = tk.Entry(window, textvariable=directory_var, width=30)
    directory_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')
    browse_button = tk.Button(window, text="Browse", command=lambda: browse_button(directory_var), bg='black', fg='white')
    browse_button.grid(row=0, column=2, padx=10, pady=5, sticky='w')

    # Create a label and entry for the delimiter
    delimiter_label = tk.Label(window, text="Delimiter:", bg='black', fg='white')
    delimiter_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    delimiter_var = tk.StringVar()
    delimiter_entry = tk.Entry(window, textvariable=delimiter_var, width=30)
    delimiter_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    # Create a button to trigger the file organization
    organize_button = tk.Button(window, text="Organize Files", command=lambda: move_files(directory_var.get(), delimiter_var.get(), status_text), bg='black', fg='white')
    organize_button.grid(row=2, column=0, columnspan=3, pady=10)

    # Create a label to display the status
    status_text = tk.StringVar()
    status_label = tk.Label(window, textvariable=status_text, bg='black', fg='white')
    status_label.grid(row=3, column=0, columnspan=3, pady=5)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
