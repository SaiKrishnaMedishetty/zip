import os
import zipfile

def extract_files(zip_file_path, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    log_file_path = os.path.join(output_directory, 'extraction_log.txt')
    with open(log_file_path, 'w') as log_file:
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            for zip_info in zipf.infolist():
                file_name = zip_info.filename
                extracted_path = zipf.extract(file_name, output_directory)
                file_size = zip_info.file_size
                
                # Print the names of the files extracted
                print(f"Extracted: {file_name}")
                
                # Write to log file
                log_file.write(f"{file_name}, Size: {file_size} bytes\n")
                
                # Check if it's a text file and read its contents
                if file_name.endswith('.txt'):
                    with open(extracted_path, 'r') as text_file:
                        content = text_file.read(100)
                        print(f"Content of {file_name}: \"{content}\"")

    print(f"Log created at: {log_file_path}")

# Sample input
zip_file_path = 'sample.zip'
output_directory = 'extracted_files'

# Extract files from the zip archive
extract_files(zip_file_path, output_directory)
