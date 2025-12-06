import os
import json
import shutil


with open("config.json", "r") as file:
    FILE_TYPES = json.load(file)


target_folder = input("Enter folder path to organize: ").strip()

if not os.path.isdir(target_folder):
    print("Invalid folder path!")
    exit()

def get_category(extension):
    """Return the category for a given file extension."""
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_files(folder):
    """Organize files into categorized subfolders."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isdir(file_path):
            continue  

        _, ext = os.path.splitext(filename)
        category = get_category(ext)

        category_path = os.path.join(folder, category)
        os.makedirs(category_path, exist_ok=True)

        new_path = os.path.join(category_path, filename)
        shutil.move(file_path, new_path)

        print(f"✔ Moved: {filename} → {category}/")

    print("\n Organizing Completed!")


if __name__ == "__main__":
    organize_files(target_folder)



