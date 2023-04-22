import sys
import os
from PIL import Image, ImageOps


# Check if input and output image file paths are valid and have the same extension
if (
    len(sys.argv) == 3  # Check if exactly 2 command-line arguments were passed
    and sys.argv[1]
    .lower()
    .endswith((".jpg", ".jpeg", ".png"))  # Check if input file has a valid extension
    and sys.argv[2]
    .lower()
    .endswith((".jpg", ".jpeg", ".png"))  # Check if output file has a valid extension
    and os.path.splitext(sys.argv[1])[1]
    == os.path.splitext(sys.argv[2])[1]  # Check if input and output have same extension
):
    try:
        # Open input and shirt images using Image module
        input_img = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")

        # Resize and crop the input image to be the same size as the shirt image
        input_img = ImageOps.fit(
            input_img, shirt.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
        )

        # Calculate the position to paste the shirt image
        shirt_x = (input_img.width - shirt.width) // 2
        shirt_y = (input_img.height - shirt.height) // 2

        # Paste the shirt image onto the input image at the calculated position
        input_img.paste(shirt, (shirt_x, shirt_y), shirt)

        # Save the output image
        input_img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


# If input and output image file paths have different extensions, print error message and exit
elif (
    len(sys.argv) == 3
    and sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png"))
    and sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png"))
    and os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]
):
    sys.exit("Input and output have different extensions")


# If output image file path has an invalid extension, print error message and exit
elif len(sys.argv) == 3 and (
    sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png"))
    and not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png"))
):
    sys.exit("Invalid output")


# If too many or too few command-line arguments are passed, print error message and exit
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
