import subprocess
import os
import sys

def run_python_file(working_directory, file_path):
    """
    Execute a Python file within a specified working directory.
    
    Args:
        working_directory (str): The base directory for execution
        file_path (str): The path to the Python file to execute
        
    Returns:
        str: The formatted output or error message
    """
    try:
        # Get absolute paths for comparison
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Check if file_path is outside the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if file exists
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        # Check if file ends with .py
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Execute the Python file
        result = subprocess.run(
            [sys.executable, abs_file_path],
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Format the output
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
        
    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}" 