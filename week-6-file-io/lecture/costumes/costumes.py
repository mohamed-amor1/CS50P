import sys  # Import the `sys` module to access command line arguments
from PIL import Image  # Import the Python Imaging Library module to work with images

images = []  # Create an empty list to store image objects

# Loop through each command line argument (excluding the script name)
for arg in sys.argv[1:]:
    image = Image.open(arg)  # Open the image file using the PIL Image class
    images.append(image)  # Append the image object to the list of images

# Save the first image as a GIF and append the second image to create an animated GIF
images[0].save(
    "costumes.gif",  # Specify the filename to save as
    save_all=True,  # Save all frames of the animation, not just the first one
    append_images=[images[1]],  # Append the second image to the first one
    duration=200,  # Set the duration (in milliseconds) for each frame of the animation
    loop=0,  # Set the number of loops (0 means infinite)
)
