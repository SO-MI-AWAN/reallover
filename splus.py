import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from fp import xxxxworldxxxx
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    xxxxworldxxxx()
elif bit == '32bit':
    from sp import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
 
