# =================================================
# Create Date: 2024/04/23
# Modify Date: 2024/04/23
# Author: BIN WU
# Function:
#   1. Read file path to photo need to be proceed       
# =================================================

from src.ShowImage import show_image

#--------------------------------------------------
# read file of photo

file_path = 'PoseRegcognition/configuration.txt'
file_path_indicator = None
try:
    # Open configuration file
    with open(file_path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            if clean_line.startswith('file_path'):
                _, file_path_indicator = clean_line.split('=', 1)
                break  
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# test function output
# if file_path_indicator:
#     print(f"Found file path: {file_path_indicator}")
# else:
#     print("file_path not found in the file.")

# show the read file (photo)
# Notice! Please press 'ESC' to close the image window
if file_path_indicator:
    file_path_indicator = file_path_indicator.strip()  # 确保移除任何额外的空格
    print(f"Found file path: {file_path_indicator}")
    print("Attempting to display image at path:", file_path_indicator)
    show_image(file_path_indicator)
else:
    print("file_path not found in the file.")
