import re
import os

# Changed default input file
def slice_covenant(input_file="public/ciris_covenant.txt", base_output_dir="content/sections"):
    """
    Slices the input text file based on '// filepath' delimiters and writes
    the content to the corresponding files within the base output directory.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading input file '{input_file}': {e}")
        return

    current_file_path = None
    content_buffer = []
    delimiter_pattern = re.compile(r"^\s*//\s*(.+?)\s*$") # Matches // filepath

    print(f"Starting slicing process for '{input_file}'...")

    for line in lines:
        match = delimiter_pattern.match(line)
        if match:
            # Found a delimiter line
            new_file_path_relative = match.group(1).strip()

            # Write the previous buffer if it exists
            if current_file_path and content_buffer:
                # Construct full path relative to the script's location or CWD
                # Assuming the paths in the delimiter are relative to the project root
                output_path = os.path.normpath(new_file_path_relative) # Use the path from the delimiter directly

                # Ensure the target directory exists
                output_dir = os.path.dirname(output_path)
                if output_dir: # Check if there is a directory part
                    os.makedirs(output_dir, exist_ok=True) # Create directories if they don't exist

                # Now write the file
                try:
                    print(f"Writing content to: {output_path}")
                    # Corrected indentation for 'with open'
                    with open(output_path, 'w', encoding='utf-8') as outfile:
                        outfile.writelines(content_buffer)
                # Corrected indentation for 'except'
                except IOError as e:
                    print(f"Error writing to file '{output_path}': {e}")
                # Corrected indentation for 'except'
                except Exception as e:
                    print(f"An unexpected error occurred while writing to '{output_path}': {e}")


            # Start new buffer for the new file path found in *this* delimiter
            current_file_path = new_file_path_relative # Store the path for the *next* write
            content_buffer = [] # Clear buffer for the new section
            print(f"Found delimiter for: {current_file_path}")

        elif current_file_path:
            # It's a content line for the current section
            content_buffer.append(line)

    # Write the last buffer after the loop finishes
    # Corrected indentation for this entire block
    if current_file_path and content_buffer:
        output_path = os.path.normpath(current_file_path)
        # Ensure the target directory exists for the final write
        output_dir = os.path.dirname(output_path)
        if output_dir: # Check if there is a directory part
            os.makedirs(output_dir, exist_ok=True) # Create directories if they don't exist

        # Now write the final file
        try:
            print(f"Writing final content to: {output_path}")
             # Corrected indentation for 'with open'
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.writelines(content_buffer)
        # Corrected indentation for 'except'
        except IOError as e:
            print(f"Error writing final content to file '{output_path}': {e}")
        # Corrected indentation for 'except'
        except Exception as e:
            print(f"An unexpected error occurred while writing final content to '{output_path}': {e}")


    print("Slicing process finished.")

if __name__ == "__main__":
    # Changed default input file path here as well
    slice_covenant(input_file="public/ciris_covenant.txt")
