import os

def get_file_content(working_directory, file_path):
    
    abs_working = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(abs_working, file_path))
    if not abs_file.startswith(abs_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    try:
        with open(abs_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        length = len(file_content_string)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'...File "{file_path}" truncated at 10000 characters'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'