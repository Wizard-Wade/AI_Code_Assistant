from pathlib import Path
from containment_helpers import in_working_directory
import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=None):
    included, abs_directory = in_working_directory(working_directory, directory)
    if not included:
        return f'Error: Cannot list "{abs_directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_directory):
        return f'Error: "{abs_directory}" is not a directory'
    
    contents = ""
    try:
        with os.scandir(abs_directory) as it:
            for entry in it:
                stats = entry.stat()
                contents += (f"- {entry.name}: file_size={stats.st_size} bytes, is_dir={entry.is_dir()}\n" )
    except Exception as e:
        contents = f'Error: {e}'
    return contents

