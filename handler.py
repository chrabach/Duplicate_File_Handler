
import sys
import os


full_path = os.getcwd()
#for root, dirs, files in os.walk(full_path, topdown=False):


def print_file(directory):

    for root, dirs, files in os.walk(directory, topdown = False):
       for name in files:
          print(os.path.join(root, name))
       #for name in dirs:
       #   print(os.path.join(root, name))

def receive_user_input():
    print("Enter file format:")
    file_format = input()
    print("Size sorting options:\n\
           1. Descending\n\
           2. Ascending")
    sort_option = input()
    if sort_option not in [1,2]:
        print("Wrong option")
    else:
        return file_format, sort_option

def get_file_size(file):
    return os.path.getsize(file)




args = sys.argv

if len(args) != 2:
    print("Directory is not specified")

else:
    print_file(args[1])
    file_format,sort_option = receive_user_input()
    file_dict = {}
    for root, dirs, files in os.walk(args[1]):
        for file in files:
            file_size  = get_file_size(file)
            print(file_size)
            file_dict[file_size] = file
    print(file_dict)






