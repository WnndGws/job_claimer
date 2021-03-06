#!/usr/bin/env python3
"""
Takes a screenshot of android phone and looks for certain key words
"""

#standard imports
from PIL import Image

#3rd party imports
import pytesseract

filename = '/home/wynand/screen.png'
text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image

print (text)
