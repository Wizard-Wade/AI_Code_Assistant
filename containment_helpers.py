import os

def in_working_directory(working_directory, specific_path):
    abs_working = os.path.abspath(working_directory)
    if specific_path != None:
        abs_path = os.path.abspath(os.path.join(abs_working, specific_path))
    else:
        abs_path = abs_working
    if not os.path.exists(abs_path):
        abs_path = remove_duplicate_folders(abs_path)
    return abs_path.startswith(abs_working), abs_path

def remove_duplicate_folders(path):
    # Split the path into parts
    parts = path.split(os.sep)
    # Remove consecutive duplicates
    unique_parts = [parts[i] for i in range(len(parts)) if i == 0 or parts[i] != parts[i - 1]]
    # Reconstruct the path
    cleaned_path = os.sep.join(unique_parts)
    return cleaned_path
        