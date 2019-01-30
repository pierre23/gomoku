#!/usr/bin/python3

import os
os.system("pip install pyinstaller")
os.system("pyinstaller --onefile src/communication.py")
os.rename('dist/communication.exe', 'pbrain-PARIS-Lundh.Sandra.exe')