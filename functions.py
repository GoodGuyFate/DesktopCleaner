import os
import shutil


def is_valid_path(path):
    return os.path.isdir(path)


def clear_downloads_folder(folder_path):
    """
    Deletes all files from the Downloads folder with confirmation options.
    If user selects (r), then take user to review_and_delete function

    Args:
      folder_path: Path to the Downloads folder (str).
    """
    downloads_list = os.listdir(folder_path)
    if not downloads_list:  # List is empty if no files are found
        print("Downloads folder is empty.")
        return

    confirm = input(f"Delete all files from Downloads (y/n) or review files (r)? ")
    if confirm.lower() == "y":
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Deleting...")
    elif confirm.lower() == "r":
        review_and_delete_download_folder(folder_path)
    else:
        print("Downloads folder remains unchanged.")


def review_and_delete_download_folder(folder_path):
    """
    Presents a list of files in the Downloads folder for individual deletion.

    Args:
      folder_path: Path to the Downloads folder (str).
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(filename)  # Display filename
            confirm = input(f"Delete {filename}? (y/n) ")
            if confirm.lower() == "y":
                os.remove(file_path)
                print(f"Deleted: {filename}")


def organize_desktop(folder_path, file_types):
  """
  Moves files on the desktop to separate folders based on file types.

  Args:
    desktop_path: Path to the Desktop folder (str).
    file_types: Dictionary mapping extensions to categories (dict).
  """
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
      # Get file extension (lowercase for case-insensitive matching)
      extension = os.path.splitext(filename)[1].lower()

      category = "others"
      # Find matching category or use "others"
      for type_name, extensions in file_types.items():
        if extension in extensions:
          category = type_name
          break

      # Create category folder if it doesn't exist
      category_path = os.path.join(folder_path, category)
      if not os.path.exists(category_path):
        os.makedirs(category_path)

      # Move file to category folder
      new_path = os.path.join(category_path, filename)
      shutil.move(file_path, new_path)
      print(f"Moved: {filename} to {category} folder")