#Main file
import zipfile
from operations import zipthatfile, unzipthatfile
print("----------------")
print("    Open ZIP    ")
print("----------------")
while True:
    operation = int(input("""
1: Zip a file
2: Unzip a file
"""))
    if operation == 1:
        zipthatfile()
    elif operation == 2:
        unzipthatfile()
