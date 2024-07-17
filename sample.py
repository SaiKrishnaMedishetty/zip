import zipfile
import os

# Define file paths
file_paths = ['file1.txt', 'file2.jpg', 'file3.pdf']

# Create sample files
for file_path in file_paths:
    with open(file_path, 'w') as f:
        f.write(f"Content of {file_path}")

# Define zip file path
zip_file_path = 'sample.zip'

# Create a zip file with the sample files
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for file_path in file_paths:
        zipf.write(file_path, os.path.basename(file_path))

print(f"{zip_file_path} created with sample files.")
