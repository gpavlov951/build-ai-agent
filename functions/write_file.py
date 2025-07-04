import os


def write_file(working_directory, file_path, content):
    """
    Write content to a file with security restrictions.
    
    Args:
        working_directory: The base directory that restricts where we can operate
        file_path: Relative path to the file within the working_directory
        content: String content to write to the file
    
    Returns:
        String message indicating success or error
    """
    try:
        full_path = os.path.join(working_directory, file_path)
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Create directory if it doesn't exist
        directory = os.path.dirname(abs_full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        # Write content to file
        with open(abs_full_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {str(e)}" 