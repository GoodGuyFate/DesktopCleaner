import os
import shutil

from functions import is_valid_path, clear_downloads_folder, organize_desktop

# Establish the downloads and desktop paths and check for valid paths.

downloads_folder_path = input("Enter Downloads folder path: ")
desktop_folder_path = input("Enter Desktop folder path: ")

while not (is_valid_path(downloads_folder_path) and is_valid_path(desktop_folder_path)):
    print("Invalid paths entered. Please try again.")
    downloads_folder_path = input("Enter Downloads folder path: ")
    desktop_folder_path = input("Enter Desktop folder path: ")

# print("Using paths:")
# print(f"Downloads: {downloads_folder_path}")
# print(f"Desktop: {desktop_folder_path}")

file_types = {
  "images": [".jpg", ".jpeg", ".png", ".gif"],
  "documents": [".pdf", ".docx", ".txt", ".xlsx"],
  "videos": [".mp4", ".avi", ".mkv"],
  "executables": [".exe"],
  "AHKScripts": [".ahk"],
}


clear_downloads_folder(downloads_folder_path)

organize_desktop(desktop_folder_path, file_types)

print("Cleaning Completed")