import os
import glob

# Changed default output file
def assemble_covenant(output_file="public/ciris_covenant.txt", base_input_dir="content/sections"):
    """
    Assembles content from various section files into a single text file,
    adding '// filepath' delimiters before each section's content.
    """

    # Define the specific order and files/patterns to include
    # Using relative paths from the project root
    assembly_order = [
        "content/sections/main/index.mdx",
        "content/sections/foreword/foreword.mdx",
        "content/sections/foreword/section0.mdx",
        # Use glob to get main sections v1-v8 in order
        *sorted(glob.glob("content/sections/main/v[1-8].mdx")),
        "content/sections/addenda/index.mdx",
        "content/sections/annexes/index.mdx",
        "content/sections/backmatter/index.mdx",
    ]

    # Sections not explicitly included based on user request:
    # - formulas
    # - resources-credits
    # - how-to-help

    print(f"Starting assembly process into '{output_file}'...")
    output_buffer = []

    for file_path_pattern in assembly_order:
        # Handle potential glob patterns (like for v1-v8)
        file_paths = glob.glob(file_path_pattern) if '*' in file_path_pattern or '[' in file_path_pattern else [file_path_pattern]

        for file_path in file_paths:
            # Normalize path for consistent delimiters
            normalized_path = os.path.normpath(file_path).replace(os.sep, '/')

            if os.path.exists(file_path):
                try:
                    print(f"Processing: {normalized_path}")
                    # Add the delimiter
                    output_buffer.append(f"// {normalized_path}\n")

                    # Read and add the file content
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        output_buffer.append(content)

                    # Add a newline after content if not already present
                    if content and not content.endswith('\n'):
                        output_buffer.append('\n')
                    # Add an extra newline for separation between files, unless it's empty
                    if content:
                         output_buffer.append('\n')


                except IOError as e:
                    print(f"Warning: Could not read file '{file_path}': {e}. Skipping.")
                except Exception as e:
                    print(f"Warning: An unexpected error occurred processing '{file_path}': {e}. Skipping.")
            else:
                print(f"Warning: File '{file_path}' not found. Skipping.")

    # Write the assembled content to the output file
    try:
        print(f"Writing assembled content to '{output_file}'...")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(output_buffer)
        print("Assembly process finished.")
    except IOError as e:
        print(f"Error writing output file '{output_file}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing '{output_file}': {e}")


if __name__ == "__main__":
    # Changed default output file path here as well
    assemble_covenant(output_file="public/ciris_covenant.txt")
