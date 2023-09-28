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
                print(f'Renamed {dir_name} to {new_dir_name}')

def main():
    base_dir = input("Enter the directory to process: ")

    # Check if directory exists
    if not os.path.isdir(base_dir):
        print(f"'{base_dir}' is not a valid directory.")
        return

    delimiter = input("Enter the delimiter: ")

    rename_directories(base_dir, delimiter)

if __name__ == "__main__":
    main()