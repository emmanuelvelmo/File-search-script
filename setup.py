from cx_Freeze import setup, Executable

setup(name="File search", executables=[Executable("File search script.py")], options={"build_exe": {"excludes": ["tkinter"]}})
