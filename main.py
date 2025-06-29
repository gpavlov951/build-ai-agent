import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if len(sys.argv) < 2:
        print("Error: Please provide a prompt as a command line argument.")
        print("Usage: python3 main.py \"Your prompt here\"")
        sys.exit(1)

    user_prompt = sys.argv[1]

    client = genai.Client(api_key=api_key)

    messages = [
      types.Message(
        role="user",
        parts=[
          types.Part(
            text=user_prompt
          )
        ]
      )
    ]

    response = client.models.generate_content(
      model="gemini-2.0-flash-001",
      contents=messages
    )

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:", response.text)

if __name__ == "__main__":
    main()
