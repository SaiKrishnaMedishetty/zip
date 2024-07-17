import os
import zipfile
import csv
from datetime import datetime

def read_zip_contents(zip_file_path, file_extension_filter=None):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            zip_infos = zipf.infolist()
            summary_data = []
            filtered_list = []

            for zip_info in zip_infos:
                file_name = zip_info.filename
                file_size = zip_info.file_size
                modification_date = datetime(*zip_info.date_time).strftime('%Y-%m-%d %H:%M:%S')

                # Print details of each file
                print(f"File: {file_name}, Size: {file_size} bytes, Modified: {modification_date}")

                # Check if the file is larger than 1MB
                if file_size > 1 * 1024 * 1024:
                    print(f"Warning: {file_name} is larger than 1MB.")

                # Add details to summary data
                summary_data.append([file_name, file_size, modification_date])

                # Apply file extension filter
                if file_extension_filter and file_name.endswith(file_extension_filter):
                    filtered_list.append(file_name)

            # Create a summary report as a CSV file
            with open('summary.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['File Name', 'Size (bytes)', 'Modification Date'])
                csv_writer.writerows(summary_data)

            print("Summary report saved as summary.csv.")

            # Print the filtered list
            if file_extension_filter:
                print("Filtered List:", ', '.join(filtered_list))
    except zipfile.BadZipFile:
        print("Error: The file is not a zip file or it is corrupted.")

# Sample input
zip_file_path = r'C:/Users/smedishetty1/OneDrive/Documents/Python/zip/my_archive.zip'
file_extension_filter = '.txt'

# Read zip contents and generate the report
read_zip_contents(zip_file_path, file_extension_filter)
