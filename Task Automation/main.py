import os
import pyautogui
import pyperclip
import re
import time
import pygetwindow as gw
import pytesseract
import webbrowser
from dotenv import load_dotenv

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hulaspet\DEV\Python_shared_files\Tesseract\tesseract.exe"
load_dotenv(r"C:\Users\hulaspet\DEV\Python_env\.env")


class DataBaseCleanUp:
    """Gets the till IDs for the daily cleanup."""
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
        self.ids = re.findall('"\d\d"|"\d\d\d"|"\d\d\d\d"?', self.data)

    @staticmethod
    def enter_db(list_status, delay):
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
        pyperclip.copy(os.getenv(list_status))
        pyautogui.click(button='right')
        pyautogui.press('enter')
        time.sleep(delay)
        pyautogui.write('it\n')
        time.sleep(delay)

    @staticmethod
    def get_count():
        """Get a count of all deltas in the DB."""
        pyperclip.copy(os.getenv('dfm_number'))
        pyautogui.click(button='right')
        pyautogui.press('enter')
        pyperclip.copy(os.getenv('dfm_status_number'))
        pyautogui.click(button='right')
        pyautogui.press('enter')

    @staticmethod
    def dfm_maintenance():
        """Remove entries older than 14 days from reporting."""
        webbrowser.open_new_tab(os.getenv('url1'))
        time.sleep(30)
        webbrowser.open_new_tab(os.getenv('url2'))


if __name__ == "__main__":
    cleanup = DataBaseCleanUp()
    #1 - List, 2 - Status, 3 - Both, 4 - Just DFM maint
    clean_what = 3

    #BatchList cleanup
    if clean_what == 1 or clean_what == 3:
        i = 0
        while i <= 2:
            cleanup.enter_db("list_tills", 5)
            cleanup.get_screenshot()
            cleanup.get_ids()
            for till_id in cleanup.ids:
                pyperclip.copy(f'db.dfm_nodeBatchList.deleteMany({{"nodeId": {till_id}}})')
                pyautogui.click(button='right')
                pyautogui.press('enter')
                time.sleep(1)
            i += 1
            print(f"Round {i} done.")
        cleanup.get_count()

    #BatchStatus cleanup
    if clean_what == 2 or clean_what == 3:
        i = 0
        while i <= 5:
            cleanup.enter_db("list_status", 10)
            cleanup.get_screenshot()
            cleanup.get_ids()
            for till_id in cleanup.ids:
                pyperclip.copy(f'db.dfm_nodeBatchStatus.deleteMany({{"nodeId": {till_id}}})')
                pyautogui.click(button='right')
                pyautogui.press('enter')
                time.sleep(3)
            i += 1
            print(f"Round {i} done.")
            cleanup.get_count()

    cleanup.dfm_maintenance()

