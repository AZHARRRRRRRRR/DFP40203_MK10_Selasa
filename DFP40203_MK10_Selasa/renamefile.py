import os


def renamefile():
    old_file = input("Enter your old file name : ")
    new_file = input("Enter the new name to rename the file : ")

    os.rename(old_file, new_file)


if __name__ == '__main__':
    renamefile()
