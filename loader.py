import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep

from colorama import Fore
version = 2


def getver():
    
    return version

def update():
    ree = requests.get(url="https://raw.githubusercontent.com/mytix9999/loader/main/version.txt")
    old_ver = getver()
    
    ver = ree.text
    if "\n" in ver:
      ver = ver.replace("\n", "")
    if int(old_ver) < int(ver):
        print("Need update")
        verr = str(ver)
        verrr = f"{verr}.0.0"
        download = f"https://raw.githubusercontent.com/mytix9999/loader/main/loader.py"
        choice = input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.RED}')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"{Fore.WHITE}\nUpdating. . .")
            
            
            reee = requests.get(url="https://raw.githubusercontent.com/mytix9999/loader/main/version.txt")
            rrr = requests.get(url=download)
            print(rrr)
            print(rrr.text)
            load = rrr
                   
            ok = f"loader-v{verr}" 
            os.mkdir(ok)  

            
            open(f"loader-{ok}/loader.exe", 'wb').write(load)
            #with ZipFile("loader.zip", 'r') as zipp:
           #     zipp.extractall()
           #     os.remove("loader.zip")
             #   cwd = os.getcwd()+'\\loader\\'
                        
        #        try:
          #          shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'loader.py')
         #       except Exception:
         #           pass
        #                            
         #       shutil.rmtree('loader')
                        
       #         print(f"{Fore.GREEN}Update Successfully Finished!")
        #        sleep(2)
      #          os.startfile("loader.py")
         #       os._exit(0)
       #                         

        


    
   
    
update()





