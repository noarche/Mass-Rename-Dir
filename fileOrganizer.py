import os
import shutil

def process_files(base_dir):
    """
    For each file in the base_dir, if the file's name starts with a letter, 
    create/move it to a directory named after that letter.
    """

    for file_name in os.listdir(base_dir):
        full_file_path = os.path.join(base_dir, file_name)

        # Check if it's a file
        if os.path.isfile(full_file_path):

            # Get the first character of the filename
            first_char = file_name[0]

            # Check if the first character is alphabetic
            if first_char.isalpha():

                # Make directory name uppercase
                dir_name = first_char.upper()

                target_dir_path = os.path.join(base_dir, dir_name)

                # Check if the directory doesn't exist, if so create it
                if not os.path.exists(target_dir_path):
                    os.mkdir(target_dir_path)

                # Move file to the new directory
                shutil.move(full_file_path, os.path.join(target_dir_path, file_name))
                print(f'Moved {file_name} to {dir_name}')

def main():
    base_dir = input("Enter the directory to process: ")

    # Check if directory exists
    if not os.path.isdir(base_dir):
        print(f"'{base_dir}' is not a valid directory.")
        return

    process_files(base_dir)

if __name__ == "__main__":
    main()