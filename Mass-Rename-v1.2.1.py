import os

def rename_directories(base_dir, delimiter):
    """
    Rename directories in the base_dir based on the delimiter.
    """
    for dir_name in os.listdir(base_dir):
        full_dir_path = os.path.join(base_dir, dir_name)

        # Check if it's a directory
        if os.path.isdir(full_dir_path):
            new_dir_name = dir_name.split(delimiter)[0]
            new_dir_path = os.path.join(base_dir, new_dir_name)

            # Check if new name is not the same as old name
            if new_dir_name != dir_name:
                os.rename(full_dir_path, new_dir_path)
                print(f'Renamed directory {dir_name} to {new_dir_name}')


def rename_files(base_dir, delimiter):
    """
    Rename files in the base_dir based on the delimiter.
    """
    for file_name in os.listdir(base_dir):
        full_file_path = os.path.join(base_dir, file_name)

        # Check if it's a file
        if os.path.isfile(full_file_path):
            new_file_name = file_name.split(delimiter)[0] + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(base_dir, new_file_name)

            # Check if new name is not the same as old name
            if new_file_name != file_name:
                os.rename(full_file_path, new_file_path)
                print(f'Renamed file {file_name} to {new_file_name}')


def rename_files_as_directory(base_dir):
    """
    Rename files in the base_dir to match directory's name.
    """
    dir_name = os.path.basename(base_dir)

    for file_name in os.listdir(base_dir):
        full_file_path = os.path.join(base_dir, file_name)

        # Check if it's a file
        if os.path.isfile(full_file_path):
            new_file_name = dir_name + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(base_dir, new_file_name)

            if new_file_name != file_name:
                os.rename(full_file_path, new_file_path)
                print(f'Renamed file {file_name} to {new_file_name}')


def main():
    base_dir = input("Enter the directory to process: ")

    # Check if directory exists
    if not os.path.isdir(base_dir):
        print(f"'{base_dir}' is not a valid directory.")
        return

    choice = input("Do you want to rename directories or files? (Enter 'd' for directories and 'f' for files): ")
    
    if choice == 'd':
        delimiter = input("Enter the delimiter: ")
        rename_directories(base_dir, delimiter)
    elif choice == 'f':
        secondary_choice = input("Do you want to rename files using a delimiter or the same as the directory name? (Enter 'delimiter' or 'directory'): ")

        if secondary_choice == 'delimiter':
            delimiter = input("Enter the delimiter: ")
            rename_files(base_dir, delimiter)
        elif secondary_choice == 'directory':
            rename_files_as_directory(base_dir)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
