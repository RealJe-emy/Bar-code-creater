# Install the required library
# pip install python-barcode

import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

# Define the barcode format and data
barcode_format = barcode.get_barcode_class('ean13')
barcode_number = '1234567895540'  # Make sure this is a valid EAN-13 number

# Generate the barcode image
barcode_image = barcode_format(barcode_number, writer=ImageWriter())

# Save the barcode image to a file
barcode_filename = 'barcode_image'
barcode_image.save(barcode_filename)

# Display the barcode image
display(Image(filename=f'{barcode_filename}.png'))
