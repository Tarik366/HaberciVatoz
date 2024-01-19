# Importing the library
import psutil
import time

x = False
while x == False:
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    time.sleep(60)