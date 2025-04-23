import re
import os
import json

def update_meta_json(meta_path, new_page_name):
    """
    Reads a meta.json file, adds a new page name to its 'pages' array,
    and writes the updated JSON back.
    """
    if not os.path.exists(meta_path):
        print(f"  Warning: meta.json not found at '{meta_path}'. Cannot update pages list.")
        return

    try:
        with open(meta_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"  Warning: Could not decode JSON from '{meta_path}'. Cannot update pages list.")
                return

        pages = data.get("pages", [])
        if not isinstance(pages, list):
            print(f"  Warning: 'pages' key in '{meta_path}' is not a list. Initializing.")
            pages = [] # Initialize if it's not a list

        if new_page_name not in pages:
            print(f"  Updating '{meta_path}' to include '{new_page_name}'...")
            if "..." in pages:
                # Insert before the "..."
                insert_index = pages.index("...")
                pages.insert(insert_index, new_page_name)
            else:
                # Append if "..." is not present
                pages.append(new_page_name)

            data["pages"] = pages

            try:
                with open(meta_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2) # Use indent=2 for readability
                    f.write('\n') # Add trailing newline
            except IOError as e:
                print(f"  Error writing updated meta.json to '{meta_path}': {e}")
        else:
            print(f"  '{new_page_name}' already exists in '{meta_path}'. No update needed.")

    except IOError as e:
        print(f"  Error reading meta.json file '{meta_path}': {e}")
    except Exception as e:
        print(f"  An unexpected error occurred while updating '{meta_path}': {e}")


# Changed default input file
def slice_covenant(input_file="public/ciris_covenant.txt", base_output_dir="content/sections"):
    """
    Slices the input text file based on '// filepath' delimiters and writes
    the content to the corresponding files. If a new file is created,
    it attempts to update the corresponding meta.json.
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

    current_file_path_for_buffer = None
    content_buffer = []
    delimiter_pattern = re.compile(r"^\s*//\s*(.+?)\s*$") # Matches // filepath

    print(f"Starting slicing process for '{input_file}'...")

    output_paths_written = set() # Keep track of files processed in this run

    for line in lines:
        match = delimiter_pattern.match(line)
        if match:
            # Found a delimiter line - this marks the *end* of the previous section
            # and the *start* of the section for the path *in this line*
            new_section_path_relative = match.group(1).strip()

            # --- Write the previous buffer to its corresponding file ---
            if current_file_path_for_buffer and content_buffer:
                output_path = os.path.normpath(current_file_path_for_buffer)
                output_paths_written.add(output_path) # Mark as processed

                # Check if file exists *before* writing
                is_new_file = not os.path.exists(output_path)

                # Ensure the target directory exists
                output_dir = os.path.dirname(output_path)
                if output_dir: # Check if there is a directory part
                    os.makedirs(output_dir, exist_ok=True) # Create directories if they don't exist

                # Now write the file
                write_successful = False
                try:
                    print(f"Writing content to: {output_path}")
                    with open(output_path, 'w', encoding='utf-8') as outfile:
                        outfile.writelines(content_buffer)
                    write_successful = True
                except IOError as e:
                    print(f"  Error writing to file '{output_path}': {e}")
                except Exception as e:
                    print(f"  An unexpected error occurred while writing to '{output_path}': {e}")

                # --- Update meta.json if it was a new file ---
                if write_successful and is_new_file:
                    base_name, ext = os.path.splitext(os.path.basename(output_path))
                    # Don't add index or meta files to the pages list
                    if base_name not in ["index", "meta"]:
                        meta_json_path = os.path.join(output_dir, "meta.json")
                        update_meta_json(meta_json_path, base_name)
            # --- End writing previous buffer ---


            # Start new buffer for the new file path found in *this* delimiter
            current_file_path_for_buffer = new_section_path_relative # Store the path for the *next* write
            content_buffer = [] # Clear buffer for the new section
            print(f"Found delimiter for: {current_file_path_for_buffer}")

        elif current_file_path_for_buffer:
            # It's a content line for the current section
            content_buffer.append(line)

    # --- Write the very last buffer after the loop finishes ---
    if current_file_path_for_buffer and content_buffer:
        output_path = os.path.normpath(current_file_path_for_buffer)
        output_paths_written.add(output_path) # Mark as processed

        # Check if file exists *before* writing
        is_new_file = not os.path.exists(output_path)

        # Ensure the target directory exists for the final write
        output_dir = os.path.dirname(output_path)
        if output_dir: # Check if there is a directory part
            os.makedirs(output_dir, exist_ok=True) # Create directories if they don't exist

        # Now write the final file
        write_successful = False
        try:
            print(f"Writing final content to: {output_path}")
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.writelines(content_buffer)
            write_successful = True
        except IOError as e:
            print(f"  Error writing final content to file '{output_path}': {e}")
        except Exception as e:
            print(f"  An unexpected error occurred while writing final content to '{output_path}': {e}")

        # --- Update meta.json if it was a new file ---
        if write_successful and is_new_file:
            base_name, ext = os.path.splitext(os.path.basename(output_path))
            # Don't add index or meta files to the pages list
            if base_name not in ["index", "meta"]:
                meta_json_path = os.path.join(output_dir, "meta.json")
                update_meta_json(meta_json_path, base_name)
    # --- End writing final buffer ---

    print(f"Slicing process finished. Processed {len(output_paths_written)} files.")

if __name__ == "__main__":
    # Changed default input file path here as well
    slice_covenant(input_file="public/ciris_covenant.txt")
