import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "WikipediaSearchTool",
    version = "0.1",
    description = "A simple python script that searches for wikipedia summaries of certain questions, things or persons.",
    executables = [Executable("app.py", base=base)]
)
