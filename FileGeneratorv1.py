import os

def create_directories(base_dir):
    """
    For each subdirectory in the base_dir with a " -" in its name,
    create a new directory using the text before the " -".
    """
    for dir_name in os.listdir(base_dir):
        full_dir_path = os.path.join(base_dir, dir_name)

        # Check if it's a directory and contains "-"
        if os.path.isdir(full_dir_path) and " -" in dir_name:
            new_dir_name = dir_name.split(" -")[0]
            new_dir_path = os.path.join(base_dir, new_dir_name.strip())

            # Check if new directory does not exist already
            if not os.path.exists(new_dir_path):
                os.mkdir(new_dir_path)
                print(f'Created directory: {new_dir_name}')

def main():
    base_dir = input("Enter the directory to process: ")

    # Check if directory exists
    if not os.path.isdir(base_dir):
        print(f"'{base_dir}' is not a valid directory.")
        return

    create_directories(base_dir)

if __name__ == "__main__":
    main()