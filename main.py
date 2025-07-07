import os
from dotenv import load_dotenv
import sys
from call_function import *


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    with open("systemprompt.txt", "r") as f:
        systemprompt = f.read()
    
    generate_content(client, messages, verbose, systemprompt)


def generate_content(client, messages, verbose, config):
    message_copy = messages.copy()
    i = 0
    while i < 20:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=message_copy,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=config)
        )        
        for candidate in response.candidates:
            message_copy.append(candidate.content)
        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
            
        if response.function_calls:
            for function_call_part in response.function_calls:
                func_result = call_function(function_call_part, verbose)
                if not func_result.parts[0].function_response.response:
                    raise Exception("Fatal Error Occurred While Calling Function")
                if verbose:
                    print(f"-> {func_result.parts[0].function_response.response}")
                message_copy.append(func_result)
        else:
            print("Response:")
            print(response.text)
            break
        i +=1

if __name__ == "__main__":
    main()