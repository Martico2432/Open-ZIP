#Main file
import zipfile
from compress import compress
print("----------------")
print("    Open ZIP    ")
print("----------------")
level = 9
filetoget = input("Enter file name to compress: ")
level = int(input("""
----Compression Levels:----
0: No compression (store only)
1: Fastest compression (less compression, faster execution)
2: Fast compression (balance between compression and execution speed)
3: Fast compression (balance between compression and execution speed)
4: Normal compression (default level, good balance between compression and execution speed)
5: Normal compression (default level, good balance between compression and execution speed)
6: Maximum compression (more compression, slower execution)
7: Maximum compression (more compression, slower execution)
8: Ultra compression (best possible compression, slowest execution)
9: Ultra compression (best possible compression, slowest execution)
                     """))
compress(level=level, filename=filetoget, outputname="Outputzip.zip", filewrite="a")