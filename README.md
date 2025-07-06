# Build AI Agent

An AI-powered code assistant that uses Google's Gemini AI to help developers with coding tasks. The agent can read, write, and execute files within a specified working directory, making it a powerful tool for code analysis, debugging, and development assistance.

## Course Information

This project is part of the Boot.dev curriculum: [Build AI Agent Course](https://www.boot.dev/lessons/44e182d7-c2c6-4c7e-9313-1b078e301344)

## Features

- **File System Operations**: List directories, read file contents, and write/overwrite files
- **Python Execution**: Run Python files with optional arguments
- **AI-Powered Assistance**: Uses Google's Gemini 2.0 Flash model for intelligent code analysis
- **Function Calling**: Structured tool usage for reliable file operations
- **Interactive Loop**: Continues conversation until the task is complete
- **Verbose Mode**: Optional detailed logging of AI interactions

## Prerequisites

- Python 3.13 or higher
- Google Gemini API key

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd build-ai-agent
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   # or if using uv:
   uv sync
   ```

3. Set up environment variables:
   ```bash
   # Create a .env file in the project root
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Basic Usage

```bash
python main.py "your prompt here"
```

### Examples

```bash
# Ask for help with code analysis
python main.py "How do I fix the calculator?"

# Request code improvements
python main.py "Can you optimize the calculator code?"

# Ask about project structure
python main.py "What files are in this project?"

# Enable verbose mode for detailed logging
python main.py "Explain how the calculator works" --verbose
```

## Project Structure

```
build-ai-agent/
├── main.py                 # Main entry point for the AI assistant
├── call_function.py        # Function calling logic and available tools
├── prompts.py             # System prompts for the AI agent
├── config.py              # Configuration settings
├── functions/             # Available functions for the AI agent
│   ├── get_files_info.py      # List files and directories
│   ├── get_file_content.py    # Read file contents
│   ├── run_python.py          # Execute Python files
│   └── write_file_content.py  # Write/overwrite files
├── calculator/            # Example calculator application
│   ├── main.py               # Calculator entry point
│   ├── pkg/                  # Calculator package
│   │   ├── calculator.py         # Core calculator logic
│   │   └── render.py            # ASCII output rendering
│   └── tests.py              # Calculator tests
└── tests.py              # Main project tests
```

## Available Functions

The AI agent has access to the following functions:

1. **get_files_info**: Lists files in directories with size information
2. **get_file_content**: Reads and returns file contents
3. **run_python_file**: Executes Python files with optional arguments
4. **write_file**: Creates or overwrites files with specified content

## Configuration

The project uses the following configuration (in `config.py`):

- `MAX_CHARS`: Maximum character limit for operations (10,000)
- `WORKING_DIR`: Default working directory (`./calculator`)
- `MAX_ITERS`: Maximum iterations for the AI loop (20)

## How It Works

1. The user provides a prompt describing their coding task
2. The AI agent creates a function call plan based on the prompt
3. The agent executes the necessary functions (reading files, running code, etc.)
4. The AI provides responses and continues until the task is complete
5. All operations are constrained to the specified working directory for security

## Example Calculator Application

The project includes a sample calculator application that demonstrates:

- Infix notation parsing with operator precedence
- Command-line interface
- Error handling for invalid expressions
- Beautiful ASCII box rendering for results

```bash
cd calculator
python main.py "3 + 5 * 2"
```

## Contributing

Feel free to extend the available functions, improve the prompts, or add new example applications.

## License

See LICENSE file for details.
