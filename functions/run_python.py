from containment_helpers import in_working_directory
import os
import subprocess
from google.genai import types

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file found at the specified location, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Required parameter. The file path to the specified .py file, relative to the working directory. if filepath does not contain .py extension it will return an error",
            ),
            # "args": types.Schema(
            #     type=types.Type.ARRAY,
            #     description="Optional parameter. Array of string arguments to pass to the command line along with the .py file.",
            # ),
        },
    ),
)

def run_python_file(working_directory, file_path, args = None):
    include, abs_file_path = in_working_directory(working_directory, file_path)
    if not include:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text=True,
            cwd= working_directory
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:{result.stderr}\n")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}\n")
        return "\n".join(output) if output else "No output produced."     
    except Exception as e:
        f"Error: executing Python file: {e}"
    