from containment_helpers import in_working_directory
import os

def write_file(working_directory, file_path, content):
    included, abs_file_path = in_working_directory(working_directory, file_path)
    if not included:
        return f'Error: Cannot write to "{abs_file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.makedirs(os.path.dirname(abs_file_path))
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written)'
    except Exception as e:
            return f'Error: {e}'