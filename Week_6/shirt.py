#https://cs50.harvard.edu/python/psets/6/shirt/

import sys
from PIL import Image, ImageOps


x = len(sys.argv)
extensions = (".jpg", "jpeg", ".png")

if x == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.lower().endswith(extensions):
        for s in extensions:
            if input_file.lower().endswith(s):
                ending = s
                break
    else:
        sys.exit("Invalid input")



    if output_file.lower().endswith(extensions):
        if not(output_file.lower().endswith(ending)):
            sys.exit("Input and output have different exetensions")
    else:
        sys.exit("Invalid output")

    try:
        shirt = Image.open("shirt.png")
        size = shirt.size

        image_to_overlay = Image.open(input_file)
        image = ImageOps.fit(image_to_overlay, size)

        image.paste(shirt,shirt)
        image.save(output_file)


    except FileNotFoundError:
        sys.exit("Input does not exist")



elif x < 3:
    sys.exit("Too few command-line arguments")


else:
    sys.exit("Too many command-line arguments")