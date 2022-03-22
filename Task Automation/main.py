# TODO:
#     Login will stay manual due to rolling admin password but it should:
#     1: Enter the MongoDB and connect to the correct collection
#     2: Get a list of TILLs where there are many stuck deltas
#     3. Grab the TILL IDs from the screenshot of the SSH session
#     4. Go through the IDs and delete the stuck deltas


from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hulaspet\DEV\Python_shared_files\Tesseract\tesseract.exe"


class DataBaseCleanUp:
    def __init__(self):
        self.data = ""
        self.ids = []
        self.im = ""

    def get_screenshot(self):
        # Temp version for testing
        self.im = Image.open("test.PNG")

    def get_ids(self):
        self.data = pytesseract.image_to_string(self.im, config="--psm 6")
        self.ids = re.findall('"\d\d\d"|"\d\d\d\d"?', self.data)


cleanup = DataBaseCleanUp()
cleanup.get_screenshot()
cleanup.get_ids()
for till_id in cleanup.ids:
    print(f"TILL ID: {till_id}")
