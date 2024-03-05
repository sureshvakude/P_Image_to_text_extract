import pytesseract
from PIL import Image

# path of the installed tesseract.exe 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# image path
image_path = "image2.jpg"
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)
cleaned_text = extracted_text.strip()

print("Extracted text:")
print(cleaned_text)