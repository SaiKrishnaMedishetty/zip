import os
import zipfile
from tqdm import tqdm

def zip_directory(directory_path, zip_file_name):
    file_paths = []
    # Collect all file paths
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_paths.append(os.path.join(root, file))

    # Create a zip file
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        summary_content = ""
        total_files = len(file_paths)

        for idx, file_path in enumerate(tqdm(file_paths, desc="Zipping progress", unit="file")):
            # Add file to zip
            zipf.write(file_path, os.path.relpath(file_path, directory_path))

            # Collect file details for summary
            original_size = os.path.getsize(file_path)
            zip_info = zipf.getinfo(os.path.relpath(file_path, directory_path))
            compressed_size = zip_info.compress_size
            compression_ratio = compressed_size / original_size if original_size else 0
            summary_content += f"{file_path}: Original size={original_size} bytes, Compressed size={compressed_size} bytes, Compression ratio={compression_ratio:.2f}\n"

        # Add summary file to zip
        zipf.writestr("summary.txt", summary_content)
        print("Summary report created in the archive.")

# Sample input
directory_path = 'large_files_directory'
zip_file_name = 'large_files.zip'

# Zip the directory
zip_directory(directory_path, zip_file_name)
