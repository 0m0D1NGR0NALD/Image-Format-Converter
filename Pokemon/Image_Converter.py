import sys
import os
from PIL import Image
    
# Capture first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Print input and output image folder paths
print(image_folder,output_folder)

# Check if output folder exists, if not create output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through input image folder path
for filename in os.listdir(image_folder):
    # Open image
    img = Image.open(f'{image_folder}{filename}') 
    # Split image path filename
    clean_name = os.path.splitext(filename)[0]
    # Print image name
    print(clean_name)
    # Save image in output folder as png file
    img.save(f'{output_folder}{clean_name}.png','png')
    # Print verification of loop success
    print('Done and Dusted')
