import os
import sys
from pathlib import Path


def cli(args):
    if len(args) == 1:
        print("No arguments")
        return
    elif len(args) != 3:
        print("Two args are needed")
        return

    origin = args[1]
    o = Path(origin)
    if not o.exists():
        print("That origin does not exists")
        return

    destiny = args[2]
    d = Path(destiny)
    if d.exists():
        print("Destiny already exists. File cannot be renamed.")
        return

    try:
        os.rename(str(args[1]), str(args[2]))
        print("FIle renamed successfully")
    except Exception as ex:
        print(f"Error: {ex}")


cli(sys.argv)
