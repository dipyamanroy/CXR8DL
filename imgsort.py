import os
import shutil

def copy_png_images(source_dir, destination_dir):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Walk through the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.png'):
                # Construct the full file path
                full_file_path = os.path.join(root, file)
                
                # Construct the destination path
                destination_path = os.path.join(destination_dir, file)
                
                # Copy the file to the destination directory
                shutil.copy2(full_file_path, destination_path)
                print(f"Copied: {full_file_path} -> {destination_path}")

if __name__ == "__main__":
    # Specify the source directory (where to look for .png files)
    source_directory = "data/CXR8/images"
    
    # Specify the destination directory (where to copy the .png files)
    destination_directory = "data/CXR8/all_images"
    
    # Call the function to copy the .png files
    copy_png_images(source_directory, destination_directory)