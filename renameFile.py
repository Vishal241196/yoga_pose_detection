import os

# Specify the directory containing the images and XML files
directory = r'C:\Users\admin\yogaPose\data\TRAIN\\warrior2'

# Prefix for the new filenames
prefix = 'yogaPose_'

# Specify the starting index for renaming
starting_index = 401  # Set the starting range to 201

# Initialize a counter for numbering the images
counter_jpg = starting_index
counter_xml = starting_index

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the current file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Generate the new filename
        new_filename = f"{prefix}{counter_jpg:04d}.jpg" # Format the counter with leading zeros
        # Construct the full paths for the old and new files
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)
        # Increment the counter
        counter_jpg += 1
    """if filename.endswith('.xml'):
        # Generate the new filename
        new_filename = f"{prefix}{counter_xml:04d}.xml" # Format the counter with leading zeros
        # Construct the full paths for the old and new files
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)
        # Increment the counter
        counter_xml += 1"""

print('Files renaming completed.')
