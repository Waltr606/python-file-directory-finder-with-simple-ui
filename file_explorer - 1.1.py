import os

def chdirUI():
    print(os.getcwd())
    print(os.listdir())
    inp = input("file: ")
    os.chdir(inp)
    buffer()

def read():
    print(os.getcwd())
    print(os.listdir())
    inp = input("file: ")
    with open(inp, 'r') as f:
        print(f.readline())
    buffer()

def buffer():
    print(os.getcwd())
    print(os.listdir())
    inp = input("chdir or read: ")
    if inp == "chdir":
        chdirUI()
    if inp == "read":
        read()

buffer()