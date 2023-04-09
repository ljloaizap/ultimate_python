from pathlib import Path

# Path('/usr/bin')  # relative route
# Path()
# Path.home()
# Path('one/__init.py')  # absolute route


path = Path('hello-world/my-file.py')  # this is only a reference
path.is_file()
path.is_dir()
path.exists()

print(
    path.name, '\n',
    path.stem, '\n',
    path.suffix, '\n',
    path.parent, '\n',
    path.absolute()
)

p = path.with_name('chanchito.exe')
print(p)
p = path.with_suffix('.bat')
print(p)
p = path.with_stem('happy')
print(p)
