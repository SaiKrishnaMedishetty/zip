import os
import zipfile

def delete_files_from_zip(zip_file_path, files_to_delete):
    # Create a new zip file path
    new_zip_file_path = zip_file_path.replace('.zip', '_new.zip')
    
    # Open the original zip file and create a new one
    with zipfile.ZipFile(zip_file_path, 'r') as original_zip:
        original_files = original_zip.namelist()
        manifest_content = ""

        # Read the existing manifest if it exists
        if 'manifest.txt' in original_files:
            with original_zip.open('manifest.txt') as manifest_file:
                manifest_content = manifest_file.read().decode('utf-8')
        
        with zipfile.ZipFile(new_zip_file_path, 'w') as new_zip:
            for item in original_zip.infolist():
                if item.filename not in files_to_delete:
                    new_zip.writestr(item, original_zip.read(item.filename))
                else:
                    print(f"Deleted: {item.filename}")

            # Remove deleted files from manifest content
            updated_manifest_content = ""
            for line in manifest_content.splitlines():
                file_name = line.split(":")[0].strip()
                if file_name not in files_to_delete:
                    updated_manifest_content += line + "\n"

            # Write the updated manifest back to the new zip archive
            new_zip.writestr('manifest.txt', updated_manifest_content)

    # Check and print files that were supposed to be deleted but didn't exist
    for file_to_delete in files_to_delete:
        if file_to_delete not in original_files:
            print(f"Warning: {file_to_delete} does not exist in the archive.")

    # Compare the sizes of the original and new zip archives
    original_size = os.path.getsize(zip_file_path)
    new_size = os.path.getsize(new_zip_file_path)
    size_difference = original_size - new_size
    print(f"Original zip size: {original_size} bytes")
    print(f"New zip size: {new_size} bytes")
    print(f"Size difference: {size_difference} bytes")

# Sample input
zip_file_path = 'my_archive.zip'
files_to_delete = ['new_file1.txt', 'new_file2.jpg']

# Delete specified files from the zip archive
delete_files_from_zip(zip_file_path, files_to_delete)
