import os

def chdirUI():
    print(os.getcwd())
    print(os.listdir())
    inp = input("file: ")
    os.chdir(inp)
    chdirUI()
chdirUI()