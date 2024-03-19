# pip install cv2
# pip install matplotlib
# pip install numpy

# # Installing the CPU and CUDA
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# pip install easyocr

# Importing the different libraries
import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

img0_path = 'image.jpeg'

# Recognise the text
def recognize_text(img_path):
    ''' loads an image and recognizes text. '''
    reader = easyocr.Reader(['en'])        # For English - 'en'  And,  For Hindi - 'hi'
    return [text[1] for text in reader.readtext(img_path)]

result = recognize_text(img0_path)
print(result)