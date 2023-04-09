from pathlib import Path
from dependencies import db
from dependencies import api
from dependencies import graphql

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencies = {
    "db": db,
    "api": api,
    "graphql": graphql
}


def load(p):
    package = __import__(str(p).replace("/", "."))
    try:
        package.init(**dependencies)
    except:
        print("Package does not have init function")


list(map(load, paths))
