import os
from containment_helpers import in_working_directory

def get_file_content(working_directory, file_path):
    included, abs_file = in_working_directory(working_directory, file_path)
    if not included:
        return f'Error: Cannot read "{abs_file}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file):
        return f'Error: File not found or is not a regular file: "{abs_file}"'
    
    MAX_CHARS = 10000

    try:
        with open(abs_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        length = len(file_content_string)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'...File "{abs_file}" truncated at 10000 characters'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'