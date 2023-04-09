from pathlib import Path
from time import ctime

file = Path('files_7/test_file.txt')

# file.exists()
# file.rename()
# file.unlink() # delete file

# print(file.stat())

print('> Accessed: ', ctime(file.stat().st_atime))
print('> Created: ', ctime(file.stat().st_ctime))
print('> Modified: ', ctime(file.stat().st_mtime))
