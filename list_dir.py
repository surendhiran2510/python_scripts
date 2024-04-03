import os

def list_dir(path):
    response = os.listdir(path)
    for files in response:
        print(files)

path = os.getcwd()
list_dir(path)



