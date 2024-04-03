import shutil

def copy_files(src, dest):
    try:
        print(src)
        print(dest)
        shutil.copy(src, dest)
        print ("copied files :",  src + "to" + dest)
    except shutil.Error as err:
        print("Error copying file:", err)

if __name__ == "__main__":
    src = input("enter source file location: ")
    dest = input("enter destination file location: ") 
    copy_files(src, dest)