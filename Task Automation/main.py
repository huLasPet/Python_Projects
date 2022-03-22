from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hulaspet\DEV\Python_shared_files\Tesseract\tesseract.exe"

im = Image.open("test.PNG")
data = pytesseract.image_to_string(im, config="--psm 6")
ids = re.findall('"\d\d\d"|"\d\d\d\d"?', data)
for id in ids:
    print(f"TILL ID: {id}")