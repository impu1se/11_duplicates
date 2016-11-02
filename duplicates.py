import os
import sys
import binascii


def get_files_list(file_path):
    file_in_dirs = []
    for d, dirs, files in os.walk(file_path):
        for file in files:
            if not file.startswith('.'):
                file_in_dirs.append(os.path.join(d, file))
    return file_in_dirs


def find_file_duplicates(file_list):
    file_with_sum = {}
    for file_path in file_list:
        file = os.path.basename(file_path)
        if file not in file_with_sum:
            file_with_sum[file] = file_path
        else:
            print(file_path, '\t\t' + os.path.join(file_with_sum[file], file))
    return file_with_sum


if __name__ == '__main__':
    file_list = get_files_list(sys.argv[1])
    find_file_duplicates(file_list)

