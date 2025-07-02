import os


def get_files_info(working_directory, directory=None):
    """
    List the contents of a directory with security restrictions.
    
    Args:
        working_directory: The base directory that restricts where we can operate
        directory: Relative path within the working_directory (None for current dir)
    
    Returns:
        String representation of directory contents or error message
    """
    try:
        if directory is None:
            directory = "."
        
        full_path = os.path.join(working_directory, directory)
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_full_path):
            return f'Error: "{directory}" does not exist'
        
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'
        
        items = os.listdir(abs_full_path)
        
        result_lines = []
        for item in sorted(items):
            item_path = os.path.join(abs_full_path, item)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                result_lines.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                result_lines.append(f" - {item}: Error getting file info: {e}")
        
        return "\n".join(result_lines)
    
    except Exception as e:
        return f"Error: {str(e)}" 