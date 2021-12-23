import os

print('The file name is: ', __file__)
print('The absolute path of the file is: ', os.path.abspath(__file__))
print('The directory of the file is: ', os.path.dirname(os.path.abspath(__file__)))