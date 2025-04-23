import re
import os
import json
import subprocess
import shutil # To check if pandoc exists
import glob
import tempfile

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

def strip_frontmatter(content_lines):
    """Removes YAML frontmatter from a list of lines."""
    if len(content_lines) > 1 and content_lines[0].strip() == '---':
        try:
            end_index = content_lines[1:].index('---') + 1
            return content_lines[end_index+1:]
        except ValueError:
            # No closing '---' found, assume no frontmatter or malformed
            return content_lines
    return content_lines

def generate_pdf(output_pdf_path):
    """
    Assembles content from specific MDX files (stripping frontmatter)
    and generates a PDF using pandoc.
    """
    # Define the specific order and files/patterns to include for PDF assembly
    assembly_order = [
        "content/sections/main/index.mdx",
        "content/sections/foreword/foreword.mdx",
        "content/sections/foreword/section0.mdx",
        *sorted(glob.glob("content/sections/main/v[1-8].mdx")),
        "content/sections/annexes/index.mdx", # Renamed from addenda
        "content/sections/annexes/annexA.mdx",
        "content/sections/annexes/annexB.mdx",
        "content/sections/annexes/annexC.mdx",
        "content/sections/annexes/annexD.mdx",
        "content/sections/annexes/annexE.mdx",
        "content/sections/backmatter/index.mdx",
        # Note: formulas, resources-credits, how-to-help are currently excluded
        # based on previous assembly logic. Add them here if needed.
    ]

    print("\nAssembling content for PDF generation...")
    pdf_content_buffer = []
    for file_path_pattern in assembly_order:
        file_paths = glob.glob(file_path_pattern) if '*' in file_path_pattern or '[' in file_path_pattern else [file_path_pattern]

        for file_path in file_paths:
            normalized_path = os.path.normpath(file_path).replace(os.sep, '/')
            if os.path.exists(file_path):
                try:
                    print(f"  Adding content from: {normalized_path}")
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        lines = infile.readlines()
                    
                    # Strip frontmatter
                    content_lines = strip_frontmatter(lines)
                    
                    # Replace custom rules with standard Markdown HR
                    cleaned_lines = [line.replace('────────────────────────────────────────', '---').replace('──────────────────', '---') for line in content_lines]

                    pdf_content_buffer.extend(cleaned_lines)
                    pdf_content_buffer.append("\n\\newpage\n") # Add page break between files for PDF

                except IOError as e:
                    print(f"  Warning: Could not read file '{file_path}' for PDF assembly: {e}. Skipping.")
                except Exception as e:
                    print(f"  Warning: An unexpected error occurred processing '{file_path}' for PDF: {e}. Skipping.")
            else:
                print(f"  Warning: File '{file_path}' not found for PDF assembly. Skipping.")

    if not pdf_content_buffer:
        print("  Error: No content assembled for PDF generation.")
        return

    # Generate PDF using pandoc
    if shutil.which("pandoc"):
        print(f"Attempting to generate PDF '{output_pdf_path}' using pandoc...")
        
        # Use a temporary file for pandoc input to handle large content
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".md", delete=False, encoding='utf-8') as temp_md_file:
            temp_md_file.writelines(pdf_content_buffer)
            temp_md_path = temp_md_file.name
        
        pandoc_cmd = [
            "pandoc", 
            temp_md_path, 
            "-f", "markdown", 
            "--pdf-engine=xelatex", 
            "-o", output_pdf_path
        ]

        try:
            result = subprocess.run(pandoc_cmd, check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Successfully created '{output_pdf_path}'.")
        except FileNotFoundError:
             print("  Error: 'pandoc' command not found. Please install pandoc to generate PDFs.")
        except subprocess.CalledProcessError as e:
            print(f"  Error running pandoc to generate PDF:")
            print(f"  Command: {' '.join(e.cmd)}")
            print(f"  Return code: {e.returncode}")
            # Try decoding stderr with replacement for potential errors
            stderr_decoded = e.stderr.decode('utf-8', errors='replace') if isinstance(e.stderr, bytes) else e.stderr
            print(f"  Stderr: {stderr_decoded}")
        except Exception as e:
            print(f"  An unexpected error occurred during PDF generation: {e}")
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_md_path):
                os.remove(temp_md_path)
                
    else:
         print("Skipping PDF generation: 'pandoc' command not found. Please install pandoc.")


# Main slicing function
def slice_covenant(input_file="public/ciris_covenant.txt", base_output_dir="content/sections"):
    """
    Slices the input text file based on '// filepath' delimiters and writes
    the content to the corresponding files. If a new file is created,
    it attempts to update the corresponding meta.json.
    Also attempts to generate a PDF from the *assembled content* after slicing.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return False # Indicate failure
    except Exception as e:
        print(f"Error reading input file '{input_file}': {e}")
        return False # Indicate failure

    current_file_path_for_buffer = None
    content_buffer = []
    delimiter_pattern = re.compile(r"^\s*//\s*(.+?)\s*$") # Matches // filepath

    print(f"Starting slicing process for '{input_file}'...")

    output_paths_written = set() # Keep track of files processed in this run
    slicing_success = True # Assume success initially

    for line in lines:
        match = delimiter_pattern.match(line)
        if match:
            new_section_path_relative = match.group(1).strip()

            if current_file_path_for_buffer and content_buffer:
                output_path = os.path.normpath(current_file_path_for_buffer)
                output_paths_written.add(output_path)
                is_new_file = not os.path.exists(output_path)
                output_dir = os.path.dirname(output_path)
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)

                write_successful = False
                try:
                    print(f"Writing content to: {output_path}")
                    with open(output_path, 'w', encoding='utf-8') as outfile:
                        # Write content *excluding* the frontmatter if it exists in buffer
                        # (Frontmatter should be added manually or by another process if needed in slices)
                        # For now, we assume frontmatter is handled in the source .txt
                        outfile.writelines(content_buffer) 
                    write_successful = True
                except IOError as e:
                    print(f"  Error writing to file '{output_path}': {e}")
                    slicing_success = False
                except Exception as e:
                    print(f"  An unexpected error occurred while writing to '{output_path}': {e}")
                    slicing_success = False

                if write_successful and is_new_file:
                    base_name, ext = os.path.splitext(os.path.basename(output_path))
                    if base_name not in ["index", "meta"]:
                        meta_json_path = os.path.join(output_dir, "meta.json")
                        update_meta_json(meta_json_path, base_name)

            current_file_path_for_buffer = new_section_path_relative
            content_buffer = [] # Clear buffer for the new section's content
            print(f"Found delimiter for: {current_file_path_for_buffer}")

        elif current_file_path_for_buffer:
            content_buffer.append(line)

    if current_file_path_for_buffer and content_buffer:
        output_path = os.path.normpath(current_file_path_for_buffer)
        output_paths_written.add(output_path)
        is_new_file = not os.path.exists(output_path)
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        write_successful = False
        try:
            print(f"Writing final content to: {output_path}")
            with open(output_path, 'w', encoding='utf-8') as outfile:
                 outfile.writelines(content_buffer)
            write_successful = True
        except IOError as e:
            print(f"  Error writing final content to file '{output_path}': {e}")
            slicing_success = False
        except Exception as e:
            print(f"  An unexpected error occurred while writing final content to '{output_path}': {e}")
            slicing_success = False

        if write_successful and is_new_file:
            base_name, ext = os.path.splitext(os.path.basename(output_path))
            if base_name not in ["index", "meta"]:
                meta_json_path = os.path.join(output_dir, "meta.json")
                update_meta_json(meta_json_path, base_name)

    print(f"Slicing process finished. Processed {len(output_paths_written)} files.")
    return slicing_success


if __name__ == "__main__":
    input_file_path = "public/ciris_covenant.txt"
    pdf_output_path = "public/ciris_covenant.pdf" # Define PDF path

    if slice_covenant(input_file=input_file_path):
        # Attempt PDF generation using the new assembly logic
        generate_pdf(output_pdf_path=pdf_output_path)
    else:
        print("\nSkipping PDF generation due to errors during slicing.")
