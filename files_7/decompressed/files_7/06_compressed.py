from pathlib import Path
from zipfile import ZipFile

ref_file = 'files_7/compressed.zip'

with ZipFile(ref_file, 'w') as zip:
    for path in Path().rglob('*.*'):
        print(path)
        if str(path) != ref_file:
            zip.write(path)
