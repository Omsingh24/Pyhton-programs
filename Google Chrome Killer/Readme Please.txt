To build the files again copy the .py file in new folder and run the command below in cmd

use this command to build CUI version CkillerCUI.py file
pyinstaller --clean --onefile --icon="icon.ico" "CkillerCUI.py"

use this command to build GUI version CkillerGUI.py file
pyinstaller --clean --onefile --windowed --icon="icon.ico" "CkillerGUI.py"




-----------------------------------------------------------------------
For more info : https://blog.electroica.com/category/programming/python/