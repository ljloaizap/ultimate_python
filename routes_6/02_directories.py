from pathlib import Path

# path = Path('directory')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename('chanchito-feliz')

path = Path('routes_6')

files = [p for p in path.iterdir() if not p.is_dir()]
files = [p for p in path.glob("01_*.py")]
files = [p for p in path.glob("**/*.py")]  # (*)
files = [p for p in path.rglob("*.py")]  # recursive glob, same as (*)

for f in files:
    print(f)
