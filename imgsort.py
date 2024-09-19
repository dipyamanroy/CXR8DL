import os
import shutil

def collect_png_images(root_path, target_folder):
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Traverse all directories and subdirectories
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith('.png'):
                # Full path of the current file
                file_path = os.path.join(dirpath, filename)

                # Destination path for the file
                destination_path = os.path.join(target_folder, filename)

                # If the file already exists at the destination, append a unique number
                count = 1
                base, ext = os.path.splitext(filename)
                while os.path.exists(destination_path):
                    new_filename = f"{base}_{count}{ext}"
                    destination_path = os.path.join(target_folder, new_filename)
                    count += 1

                # Move the file
                shutil.move(file_path, destination_path)
                print(f"Moved: {file_path} -> {destination_path}")

if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ").strip()
    target_directory = os.path.join(root_directory, "collected_pngs")

    # Ensure the root path exists
    if not os.path.isdir(root_directory):
        print(f"The directory {root_directory} does not exist.")
    else:
        collect_png_images(root_directory, target_directory)
        print("PNG collection complete.")