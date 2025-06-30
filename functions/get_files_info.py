from pathlib import Path
import os

def get_files_info(working_directory, directory=None):
    abs_working = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(abs_working, directory))
    if not abs_directory.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    
    contents = ""
    try:
        with os.scandir(abs_directory) as it:
            for entry in it:
                stats = entry.stat()
                contents += (f"- {entry.name}: file_size={stats.st_size} bytes, is_dir={entry.is_dir()}\n" )
    except Exception as e:
        contents = f'Error: {e}'
    return contents

