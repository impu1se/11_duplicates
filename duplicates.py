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
    for file in file_list:
        with open(file, 'rb') as f:
            if binascii.crc32(f.peek()) in file_with_sum:
                print(file,'\t' + file_with_sum[binascii.crc32(f.peek())])
            else:
                file_with_sum[binascii.crc32(f.peek())] = file
    return file_with_sum


if __name__ == '__main__':
    file_list = get_files_list(sys.argv[1])
    find_file_duplicates(file_list)

