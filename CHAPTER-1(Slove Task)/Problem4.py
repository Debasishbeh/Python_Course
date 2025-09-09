import os

# Use current directory (.) or give full path like "C:/Users/Banty/Desktop"
directory_path = '/DEBASISH'

# List contents
contents = os.listdir(directory_path)

# Print each item
for item in contents:
    print(item)
