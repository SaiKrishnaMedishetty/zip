import os
import pyzipper

def create_zip_archive(file_paths, zip_file_name, password=None):
    with pyzipper.AESZipFile(zip_file_name, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:
        manifest_content = ""
        
        for file_path in file_paths:
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))
                print(f"Added: {os.path.basename(file_path)}")
                
                file_size = os.path.getsize(file_path)
                manifest_content += f"{os.path.basename(file_path)}: {file_size} bytes\n"
            else:
                print(f"Warning: {file_path} does not exist")
        
        # Add manifest file
        zipf.writestr("manifest.txt", manifest_content)
        print("Manifest created inside the archive.")
        
        # Set password if provided
        if password:
            zipf.setpassword(password.encode('utf-8'))

# Sample input
file_paths = ['file1.txt', 'file2.jpg', 'file3.pdf']
zip_file_name = 'my_archive.zip'
password = 'mypassword'

# Create zip archive
create_zip_archive(file_paths, zip_file_name, password)
