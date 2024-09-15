# program to get the full path of the current working directory
import pathlib
# path of given file
print(pathlib.Path('leap.py').parent.absolute())
# current working directory
print(pathlib.Path().absolute())