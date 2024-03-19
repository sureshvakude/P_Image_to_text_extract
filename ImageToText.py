'''
# pip install cv2
# pip install matplotlib
# pip install numpy

# Installing the CPU and CUDA
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# pip install easyocr
'''
import easyocr

img_path = 'image.jpeg'

def recognize_text(path):
    '''Loads an image and recognizes text.'''
    # Initialize EasyOCR Reader with specified parameters
    reader = easyocr.Reader(['en'], gpu=True)
    # Recognize text with specified parameters
    return reader.readtext(path, batch_size=1, detail=0, allowlist='.%$() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

result = recognize_text(img_path)
# Print the recognized text
for text in result:
    print(text)