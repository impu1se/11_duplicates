import os
import sys


def are_files_duplicates(file_path):
    file_in_dirs = []
    for d, dirs, file in os.walk(file_path):
        for f in file:
            if not f.startswith('.') and os.path.isfile(os.path.join(d, f)):
                file_in_dirs.append(os.path.join(d, f))
    return file_in_dirs

def find_file_duplicates(file_list):
    pass


if __name__ == '__main__':
    file_list = are_files_duplicates(sys.argv[1]))
    find_file_duplicates(file_list)

