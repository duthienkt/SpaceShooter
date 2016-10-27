import sys
from cx_Freeze import setup, Executable

setup(
    name = "Appname",
    version = "1.0",
    description = "Assignment XXXX, dd/mm/yyy",
    executables = [Executable("main.py", base = "Win32GUI")])