import os

def MakeFile(Path, FileName):
    dir_list = os.listdir(Path)
    print("List of files before:\n")
    file = str(Path + FileName)
    with open(file, 'w') as fp:
        pass
    dir_list = os.listdir(Path)
    print("List of directories and files after creation:")
    print(dir_list)
def WriteFile(FileName):
    text = input("Text To Add to out.bin:\n").encode('ascii')
    map(bin,bytearray(text))
    print("")
    with open(FileName, "wb") as file:
        file.write(text)
def ReadFile(FileName):
    with open(FileName, "rb") as file:
        contents = file.read()
        print("Contents:\n")
        print(' '.join('{:02X}'.format(c) for c in contents))
        print("")
        print(contents)
    