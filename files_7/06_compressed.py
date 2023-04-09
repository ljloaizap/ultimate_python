from pathlib import Path
from zipfile import ZipFile

ref_file = 'files_7/compressed.zip'

# # write
# with ZipFile(ref_file, 'w') as zip:
#     for path in Path().rglob('*.*'):
#         print(path)
#         if str(path) != ref_file:
#             zip.write(path)


with ZipFile(ref_file, 'r') as zip:
    # print(zip.namelist())
    info = zip.getinfo('files_7/06_compressed.py')
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall('files_7/decompressed')
