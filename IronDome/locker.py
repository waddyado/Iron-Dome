import time
import os


time.sleep(15)
ok = windll.user32.BlockInput(True) #enable block
time.sleep(5)
os.system("shutdown /s /t 1");
