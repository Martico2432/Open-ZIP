from compress import compress
from decompress import decompress
def zipthatfile():
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
7: Ultra compression (more compression, slower execution)
8: Super compression (best possible compression, slowest execution)
9: Superior compression (best possible compression, slowest execution)
                     """))
    compress(level=level, filename=filetoget, outputname="Outputzip.zip")
def unzipthatfile():
    filetoget = input("Enter file name to decompress: ")
    decompress(filename=filetoget, outputfile="Outputfile.txt")
