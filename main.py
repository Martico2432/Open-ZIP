#Main file
import zipfile
from compress import compress
print("----------------")
print("    Open ZIP    ")
print("----------------")
level = 9
filetoget = input("Enter file name to compress: ")
compress(level=level, filename=filetoget, outputname="Outputzip.zip", filewrite="a")