import datetime

def read_file(filename):
    """
    Attempts to open and read a file, handling common exceptions.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        str: The file contents if successful, or an error message if an exception occurs
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def write_file(filename, content):
    """
    Attempts to write content to a file, with validation and exception handling.
    
    Args:
        filename (str): The name of the file to write to
        content (str): The content to write to the file
        
    Returns:
        str: "Success" if writing was successful, or an error message if an exception occurs
        
    Raises:
        TypeError: If content is not a string
    """
    if not isinstance(content, str):
        raise TypeError("Content must be a string")
    
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return "Success"
    except PermissionError:
        return "Permission denied"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def process_data(input_file, output_file):
    """
    Processes data from an input file and writes the result to an output file.
    
    Args:
        input_file (str): Path to the input file
        output_file (str): Path to the output file
        
    Returns:
        str: "Success" if processing was successful, or an error message if any step failed
    """
    # Read the input file
    content = read_file(input_file)
    
    # Check if reading failed
    if content.startswith("File not found") or content.startswith("Permission denied") or content.startswith("An error occurred"):
        return content
    
    # Process the content
    processed_content = content.upper()[::-1]  # Convert to uppercase and reverse
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    processed_content += f"\nProcessed on {current_date}"
    
    # Write to the output file
    result = write_file(output_file, processed_content)
    return result

def main():
    """
    Main program that interacts with the user and coordinates file operations.
    """
    print("File Processing Program")
    print("-----------------------")
    
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")
    
    result = process_data(input_file, output_file)
    print(result)

if __name__ == "__main__":
    main()