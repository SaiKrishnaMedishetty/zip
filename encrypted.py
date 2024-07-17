import pyzipper
import os

def extract_encrypted_zip(zip_file_name, extract_to_directory, password):
    try:
        with pyzipper.AESZipFile(zip_file_name, 'r') as zipf:
            zipf.setpassword(password.encode('utf-8'))
            zipf.extractall(path=extract_to_directory)
            print("Extraction successful. Files extracted to the specified directory.")
    except RuntimeError as e:
        print(f"Error: {e}")

# Sample input
zip_file_name = 'encrypted_archive.zip'
extract_to_directory = 'extracted_files'
password = 'securepassword'

# Extract encrypted zip archive
extract_encrypted_zip(zip_file_name, extract_to_directory, password)
