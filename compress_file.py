import zipfile
import os

from zipfile import ZipFile as zip

def compress_file(file_path, zip_path):
    print(os.path.basename(file_path))
    with zip(zip_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    print(f"File '{file_path}' compressed to '{zip_path}' successfully.")

def decompress_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"File '{zip_path}' decompressed to '{extract_to}' successfully.")

if __name__ == "__main__":
    file_to_compress = input("Enter the path of the file to compress: ")
    zip_file = input("Enter the path of the ZIP file to create: ")
    compress_file(file_to_compress, zip_file)

    file_to_decompress = input("Enter the path of the ZIP file to decompress: ")
    extraction_folder = input("Enter the path of the folder to extract to: ")
    decompress_file(file_to_decompress, extraction_folder)
