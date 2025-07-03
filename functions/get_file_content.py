import os


def get_file_content(working_directory, file_path):
    """
    Read the contents of a file with security restrictions.
    
    Args:
        working_directory: The base directory that restricts where we can operate
        file_path: Relative path to the file within the working_directory
    
    Returns:
        String contents of the file or error message
    """
    try:
        MAX_CHARS = 10000
        
        full_path = os.path.join(working_directory, file_path)
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_full_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            
        # Check if file was truncated
        if len(file_content) == MAX_CHARS:
            # Check if there's more content to read
            with open(abs_full_path, "r") as f:
                f.seek(MAX_CHARS)
                if f.read(1):  # If there's at least one more character
                    file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content
    
    except Exception as e:
        return f"Error: {str(e)}" 