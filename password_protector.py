import pyzipper
import os

def create_encrypted_zip(file_paths, zip_file_name, password):
    with pyzipper.AESZipFile(zip_file_name, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode('utf-8'))
        for file_path in file_paths:
            zipf.write(file_path, arcname=os.path.basename(file_path))
            print(f"Files added and encrypted: {file_path}")
    print(f"Archive {zip_file_name} created successfully with encryption.")

# Sample input
file_paths = ['file1.txt', 'file2.jpg', 'file3.pdf']
zip_file_name = 'encrypted_archive.zip'
password = 'securepassword'

# Create encrypted zip archive
create_encrypted_zip(file_paths, zip_file_name, password)
