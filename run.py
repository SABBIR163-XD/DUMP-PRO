import os, platform, time
import os,base64,zlib,pip,urllib,time
os.system('termux-setup-storage')
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')  
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')

def mind():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print('\x1b[1;92m[✓] Congratulations Your Device Support This Tools!')
            time.sleep(3)
            os.system('git pull')
            os.system('clear')
            print('\x1b[1;92m[✓] Join My Facebook Group  ')
            time.sleep(2)
           os.system(f'xdg-open https://facebook.com/groups/587970852914505/')
           os.system('pip install requests')
           os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
           os.system('clear')
            import XD
        else:
            exit('\033[1;31m[×] Sorry, Your Device Not Support This Tool')
demon()
