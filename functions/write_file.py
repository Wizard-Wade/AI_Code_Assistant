from containment_helpers import in_working_directory
import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to given file path, constrained to the working directory. if file or directories in file path do not exist, function will create the missing components in the filepath chain",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Required parameter. File path to the file targeted for being written, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Required parameter. Text content to be written to the targeted file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

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