import os
import sys


def are_files_duplicates(file_path):
    res = []
    for d, dirs, file in os.walk(file_path):
        for f in file:
            res.append(os.path.join(d, f))
    return res

def find_file_duplicates(file_list):
    for file in file_list:
        for 

if __name__ == '__main__':
    print(are_files_duplicates(sys.argv[1]))

