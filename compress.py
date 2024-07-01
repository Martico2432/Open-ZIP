import zipfile
def getlines(file:str):
    with open(file, 'rb') as f:
        lines = [line.rstrip(b'\n') + b'\n' for line in f.readlines()]
    return lines
def compress(level: int, filename: str, outputname: int, filewrite):
    """Level: 1-9 integer
    Filename: name of the file you want to compress
    Outputname: name of the output compressed file"""
    with zipfile.ZipFile(outputname, mode="w", compresslevel= level) as archive:
        with archive.open(filename, mode="w") as filecontent:
            for line in getlines(file=filename):
                filecontent.write(line)