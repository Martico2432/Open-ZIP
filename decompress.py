import zipfile
def decompress(filename, outputfile):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(outputfile)