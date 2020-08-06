#Imports

from PIL import Image, ImageGrab
from pathlib import Path
import pytesseract as tess
# (optinal) import time (will highly needed if you want proceed the automation into a complex one)

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#Taking and Resizing the Screenshot

image = ImageGrab.grab(bbox=(113, 340, 312, 450))  # X1,Y1,X2,Y2
image.save("images/image.PNG")
openedImage = Image.open("images/image.PNG")


text = tess.image_to_string(openedImage)
print(text)



