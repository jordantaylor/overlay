import platform
from os import system

ver = platform.architecture()[0]

if('64' in ver):
    system("pip3.6 install dependencies\\GDAL-2.2.4-cp36-cp36m-win_amd64.whl")
else:
    system("pip3.6 install dependencies\\GDAL-2.2.4-cp36-cp36m-win32.whl")

system("pip3.6 install pyqt5")