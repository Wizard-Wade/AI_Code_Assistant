import os

def is_in_working_directory(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(abs_working, file_path))
    return abs_file.startswith(abs_working), abs_file
        