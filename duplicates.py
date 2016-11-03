import os
import sys


def get_files_list(file_path):
    file_in_dirs = []
    for d, dirs, files in os.walk(file_path):
        for file in files:
            if not file.startswith('.'):
                file_in_dirs.append(os.path.join(d, file))
    return file_in_dirs


def find_duplicates(file_list):
    file_with_sum = {}
    file_duplicates = []
    for file_path in file_list:
        path, file = os.path.split(file_path)
        if file not in file_with_sum:
            file_with_sum[file] = path
        elif os.path.getsize(file_path) == os.path.getsize(os.path.join(file_with_sum[file], file)):
            file_duplicates.append((file_path, os.path.join(file_with_sum[file], file)))
    return file_duplicates


if __name__ == '__main__':
    file_list = get_files_list(sys.argv[1])
    print(find_duplicates(file_list))

