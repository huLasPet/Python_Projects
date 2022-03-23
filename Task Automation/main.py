import os
import pyautogui
import pyperclip
import re
import time
import pygetwindow as gw
import pytesseract
from dotenv import load_dotenv

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hulaspet\DEV\Python_shared_files\Tesseract\tesseract.exe"
load_dotenv(r"C:\Users\hulaspet\DEV\Python_env\.env")


def enter_db():
    """Focuses on the window with the SSH session to the DB server
    Enters the DB and lists all tills with their delta count."""
    win = gw.getWindowsWithTitle(os.getenv('focus_window'))[0]
    win.activate()
    win.maximize()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.write('clear\n')
    pyautogui.write('mongo\n')
    pyautogui.write(os.getenv('dfm'))
    pyautogui.press('enter')
    time.sleep(1)
    pyperclip.copy(os.getenv('list_tills'))
    pyautogui.click(button='right')
    pyautogui.press('enter')


class DataBaseCleanUp:
    """Handles the daily DB cleanup that was done manually before."""
    def __init__(self):
        self.data = ""
        self.ids = []
        self.im = ""

    def get_screenshot(self):
        """Creates a screenshot of the listed tills."""
        self.im = pyautogui.screenshot()
        time.sleep(1)

    def get_ids(self):
        """Gets the text from the screenshot and finds all till IDs."""
        self.data = pytesseract.image_to_string(self.im, config="--psm 6")
        self.ids = re.findall('"\d\d\d"|"\d\d\d\d"?', self.data)



cleanup = DataBaseCleanUp()
enter_db()
cleanup.get_screenshot()
cleanup.get_ids()
for till_id in cleanup.ids:
    pyperclip.copy(f'db.dfm_nodeBatchList.deleteMany({{"nodeId": {till_id}}})')
    pyautogui.click(button='right')
    pyautogui.press('enter')
    time.sleep(0.5)
