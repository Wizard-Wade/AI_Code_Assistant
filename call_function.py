from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python import *
from functions.write_file import *

from google import genai
from google.genai import types

available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python,
        schema_write_file,
    ]
)

func_dictionary = {
    "get_files_info": get_files_info, 
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
    }

def call_function(function_call_part: types.FunctionCall, verbose=False):
    function_name = function_call_part.name
    
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")
    
    working_directory = "./calculator"
    function_call_part.args["working_directory"] ="./calculator"
    
    if not function_name in func_dictionary.keys():
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    function_result = func_dictionary[function_name](**function_call_part.args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )