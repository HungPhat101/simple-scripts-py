'''
version: 1.1
This script helps to rename files quickly which in a specific folder on Windows OS
1. Input specific folder path to change all file name in that folder
2. Input prefix you want to change for new filename
3. Input suffix you want to change for new filename
'''

from pathlib import Path
import sys

file_path = Path(input("Please input a specific absolute file path: "))

if Path.is_dir(file_path) is False:
    print(f"File path {file_path} is invalid")
    sys.exit()

prefix = input("Input prefix for new file name: ")

suffix = 1

extension = input("Input extension to replace: ")

for child in file_path.iterdir():
    child.rename(f"{file_path}\\{prefix}-{suffix}.{extension}")
    print(child)
    suffix += 1