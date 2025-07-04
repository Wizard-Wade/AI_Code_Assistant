from containment_helpers import in_working_directory
import os
import subprocess

def run_python_file(working_directory, file_path):
    include, abs_file_path = in_working_directory(working_directory, file_path)
    if not include:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python", abs_file_path],
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
    