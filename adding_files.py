import os
import shutil
import zipfile

def add_files_to_zip(zip_file_path, new_files):
    # Create a backup of the original zip file
    backup_zip_path = zip_file_path.replace('.zip', '_backup.zip')
    shutil.copy(zip_file_path, backup_zip_path)
    print(f"Backup created: {backup_zip_path}")
    
    # Open the existing zip file in append mode
    with zipfile.ZipFile(zip_file_path, 'a') as zipf:
        existing_files = zipf.namelist()
        manifest_content = ""

        for new_file in new_files:
            if os.path.exists(new_file):
                file_name = os.path.basename(new_file)
                if file_name in existing_files:
                    print(f"Warning: {file_name} already exists in the archive.")
                else:
                    zipf.write(new_file, file_name)
                    print(f"Added: {file_name}")

                file_size = os.path.getsize(new_file)
                manifest_content += f"{file_name}: {file_size} bytes\n"
            else:
                print(f"Error: {new_file} does not exist.")

        # Update the manifest file inside the zip archive
        if 'manifest.txt' in existing_files:
            with zipf.open('manifest.txt', 'r') as manifest_file:
                manifest_content = manifest_file.read().decode('utf-8') + manifest_content

        with zipf.open('manifest.txt', 'w') as manifest_file:
            manifest_file.write(manifest_content.encode('utf-8'))

        print("Manifest updated.")

# Sample input
zip_file_path = 'my_archive.zip'
new_files = ['new_file1.txt', 'new_file2.jpg']

# Create sample new files if they don't exist for testing
if not os.path.exists('new_file1.txt'):
    with open('new_file1.txt', 'w') as f:
        f.write("This is the content of new_file1.txt.")

if not os.path.exists('new_file2.jpg'):
    with open('new_file2.jpg', 'w') as f:
        f.write("This is the content of new_file2.jpg.")

# Add new files to the existing zip archive
add_files_to_zip(zip_file_path, new_files)
