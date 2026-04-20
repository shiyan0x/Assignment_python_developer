import os
import shutil
import datetime

folder_path = "test_folder"
log_file = "organizer_log.txt"

file_type = {
    "images"    : [".jpg", ".jpeg", ".png", ".gif"],
    "documents" : [".pdf", ".doc", ".docx", ".txt", ".csv"],
    "videos"    : [".mp4", ".avi", ".mkv"],
    "audios"    : [".mp3", ".wav", ".aac"],
    "others"    : []
}

def log_action(message):
    # Writing log to the file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    with open(log_file, "a") as f:   
        f.write(log_entry)

def rename_file(file_name):
    # Renaming files by adding a timestamp prefix
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(file_name)
    return f"{name}_{timestamp}{ext}"

def create_subdirectories():
    """Create category subdirectories inside the target folder."""
    for folder in file_type:
        path = os.path.join(folder_path, folder)
        try:
            os.makedirs(path, exist_ok=True)
            log_action(f"Directory ensured: {path}")
        except OSError as e:
            log_action(f"ERROR creating directory {path}: {e}")

def organize_files():
    # Error handling: check if source folder exists (file read requirement)
    if not os.path.exists(folder_path):
        log_action(f"ERROR: Folder '{folder_path}' does not exist.")
        return

    try:
        files = os.listdir(folder_path)   # FILE READ
    except PermissionError as e:
        log_action(f"ERROR: Cannot read folder '{folder_path}': {e}")
        return

    if not files:
        log_action("No files found to organize.")
        return

    create_subdirectories()

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Skip subdirectories
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        destination_folder = "others"   # default category

        # Determine correct category folder
        for folder, extensions in file_type.items():
            if ext in extensions:
                destination_folder = folder
                break

        # Rename the file with a timestamp prefix
        new_name = rename_file(file)
        target_path = os.path.join(folder_path, destination_folder, new_name)

        # Error handling: move the file safely
        try:
            shutil.move(file_path, target_path)
            log_action(f"Moved & renamed: '{file}' -> '{destination_folder}/{new_name}'")
        except FileNotFoundError as e:
            log_action(f"ERROR: File not found '{file}': {e}")
        except PermissionError as e:
            log_action(f"ERROR: Permission denied for '{file}': {e}")
        except shutil.Error as e:
            log_action(f"ERROR: Could not move '{file}': {e}")

# ── Entry point ───
if __name__ == "__main__":
    log_action("=== File Organizer Started ===")
    organize_files()
    log_action("=== File Organizer Finished ===")