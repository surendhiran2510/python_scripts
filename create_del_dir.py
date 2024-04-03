import os

def create_del_dir(directory, name, operation):
    if os.path.exists(directory):
        print (f"path exists: going to {operation} directory")
    else:
        print (f"path does not exist {directory}")
    if operation == 'create':
        path = os.path.join(directory, name)
        os.mkdir(path)
    elif operation == 'delete':
        path = os.path.join(directory, name)
        os.remove(path)
    else:
        print (f"operation {operation} not supported")

directory = input("enter the directory path:")
Name = input("Enter the dir namE:")
operation = input("enter the operation create or delete:")
create_del_dir(directory, Name, operation)