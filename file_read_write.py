# File Read & Write with Error Handling

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nFile read successfully!")

        # Modify the content (Example: Convert text to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Prompt user for file names
input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the new file to write: ")

# Perform file read & write operation
read_and_modify_file(input_file, output_file)
