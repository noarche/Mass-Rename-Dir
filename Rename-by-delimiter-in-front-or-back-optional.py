import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_files(folder_path, delimiter, action):
    try:
        # List all files in the provided folder path
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for file_name in files:
            # Split the file name using the provided delimiter
            parts = file_name.split(delimiter)

            if len(parts) > 1:
                if action == "Remove Text in Front":
                    # Remove text in front of the delimiter and replace '-' with a space
                    new_name = parts[1].replace('-', ' ')
                elif action == "Remove Text Behind":
                    # Remove text behind the delimiter and replace '-' with a space
                    new_name = parts[0].replace('-', ' ')

                os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

        messagebox.showinfo("Success", "Files renamed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_about():
    about_text = "Coded by [Your Name]\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit."
    messagebox.showinfo("About", about_text)

def get_folder_path():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

def on_process_button_click():
    folder_path = folder_path_entry.get()
    delimiter = delimiter_entry.get()
    action = action_var.get()

    if action == "Choose Action":
        messagebox.showwarning("Warning", "Please choose an action.")
    else:
        # Display a message based on the selected action
        message = f"Text {action.lower()} the delimiter will be removed, and '-' will be replaced with a space.\n\nPress OK to continue."
        response = messagebox.askokcancel("Confirmation", message)

        if response:
            process_files(folder_path, delimiter, action)

if __name__ == "__main__":
    # Create the main window
    main_window = tk.Tk()
    main_window.title("File Renamer")

    # Set the theme to dark
    main_window.tk_setPalette(background='#2e2e2e', foreground='#00ff00')

    # Set window size and make it not resizable
    main_window.geometry("300x380")
    main_window.resizable(False, False)

    # Create and place widgets
    folder_path_label = tk.Label(main_window, text="Folder Path:", fg='#00ff00', bg='#2e2e2e')
    folder_path_label.pack(pady=5)

    folder_path_entry = tk.Entry(main_window, bg='#333333', fg='#00ff00')
    folder_path_entry.pack(pady=5)

    folder_path_button = tk.Button(main_window, text="Browse", command=lambda: folder_path_entry.insert(tk.END, get_folder_path()), bg='#2e2e2e', fg='#00ff00')
    folder_path_button.pack(pady=5)

    delimiter_label = tk.Label(main_window, text="Delimiter:", fg='#00ff00', bg='#2e2e2e')
    delimiter_label.pack(pady=5)

    delimiter_entry = tk.Entry(main_window, bg='#333333', fg='#00ff00')
    delimiter_entry.pack(pady=5)

    action_label = tk.Label(main_window, text="Action:", fg='#00ff00', bg='#2e2e2e')
    action_label.pack(pady=5)

    action_options = ["Choose Action", "Remove Text in Front", "Remove Text Behind"]
    action_var = tk.StringVar(main_window)
    action_var.set(action_options[0])
    action_dropdown = tk.OptionMenu(main_window, action_var, *action_options)
    action_dropdown.config(bg='#2e2e2e', fg='#00ff00', width=15)
    action_dropdown.pack(pady=5)

    process_button = tk.Button(main_window, text="Process", command=on_process_button_click, bg='#2e2e2e', fg='#00ff00')
    process_button.pack(pady=10)

    about_button = tk.Button(main_window, text="About", command=show_about, bg='#2e2e2e', fg='#00ff00')
    about_button.pack(pady=10)

    # Start the main loop
    main_window.mainloop()
