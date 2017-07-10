import os
import argparse


def get_files_list(file_path):
    file_in_dirs = []
    for d, dirs, files in os.walk(file_path):
        for file in files:
            if not file.startswith('.'):
                file_in_dirs.append(os.path.join(d, file))
    return file_in_dirs


def find_duplicates(list_file_with_path): 
    file_name_and_path = {}
    files_duplicates = []
    for file_path in list_file_with_path:
        path, file_name = os.path.split(file_path)
        if file_name not in file_name_and_path:
            file_name_and_path[file_name] = path  
        elif os.path.getsize(file_path) == \    
                os.path.getsize(os.path.join(file_name_and_path[file_name],
                                             file_name)):
            files_duplicates.append((file_path, os.path.join(
                file_name_and_path[file_name], file_name)))
    return files_duplicates


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find duplicates file')
    parser.add_argument('-path', dest='path',
                        help='Input pathname for find duplicates', default='.')
    args = parser.parse_args()
    files_list = get_files_list(args.path)
    if files_list:
        files_duplicates = find_duplicates(files_list)
        if files_duplicates:
            for files in files_duplicates:
                print('File 1: {0} \nFile 2: {1} \n-----------\n'.format(
                    files[0], files[1]))
        else:
            print('The duplicates of files are not founds')
    else:
        print('Possibly you input not the path')
