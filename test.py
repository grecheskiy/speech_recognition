import zipfile
import os

myzip = zipfile.ZipFile('g\\file.zip', 'w')



for folder, subfolders, files in os.walk('F:\\contacts\\Project Germes\\ff'):

    for file in files:
            myzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'F:\\contacts\\Project Germes\\ff'), compress_type = zipfile.ZIP_DEFLATED)


myzip.close()
