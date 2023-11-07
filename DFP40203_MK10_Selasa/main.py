import os
import glob


def filehandler():
    file_pattern = '../DFP40203_MK10_Selasa/*.txt'

    for file_path in glob.glob(file_pattern):
        print(os.path.basename(file_path))


if __name__ == '__main__':
    filehandler()
