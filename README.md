# Python Course: "Ultimate Python: de cero a programador experto
Udemy resource, [link](https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/learn/lecture/36468872#overview), with Nicolás from _Hola Mundo_.

## VS Code Extensions & Format
- `python` by Microsoft
- `pylint` by Microsoft
- Open `palette` view and look for Format. Install `autopep 8`.
- Auto formatting: `manage > settings`, then type `formatOnSave` and tick first option _"Format a file on save"_.


## Concepts to keep in mind
### Params vs Arguments
* **_Params_**: the input variables of a function
* **_Arguments_**: the values we pass when calling a function

### Functions vs Methods
* **_Functions_**: Block of code to achieve a specific goal
* **_Methods_**: Similar as function but within a class.

### Magic method
1. Executed without explicit call
2. Starts and ends with `__`, e.g., `__init__`


## Useful links
- PEP 8 – Style Guide for Python Code -> [link](https://peps.python.org/pep-0008/)
- Fake API `(typicode)` -> [link](https://jsonplaceholder.typicode.com/)



## SQLITE

In case of the following error appears:

```
ModuleNotFoundError: No module named '_sqlite3'
```


... then, install `sqlite` dev package

```
> sudo apt-get update -y
> sudo apt-get install -y libsqlite3-dev
```
Cd your python installer directory and:
```
> ./configure --prefix=/opt/python3.7.4 --with-ssl --with-pydebugx --enable-loadable-sqlite-extensions --enable-optimizations
> make
> make install
```

## PIP, Virtual envs & pipenv

### PIP

```
pip install requests
pip list
pip uninstall requests
pip install requests==2.18.1
--pip install requests==2.18.*
--pip install requests==2.*
```

### venv
Create virtual environment within current folder
```
python3 -m venv env
deactivate
```

### pipenv
Create virtual environment and (un)install dependencies
```
pip install pipenv
pipenv install requests
pipenv --venv  # virtualenv location
pipenv shell  # activate virtualenv in cmd
exit  # 'deactivate'
#
pipenv install  # create virtualenv from Pipfile 
pipenv install --ignore-pipfile  # based on Pipfile.lock
```

**pipenv: dependencies mgmt**
```
pipenv graph
pipenv update --outdated  # packages outdated
pip update requests
pip update  # all packages
```

## Overall dependencies
```
pipenv install sendgrid  # emails
pipenv install beautifulsoup4  # web scrapping
pipenv install openpyxl  # excel
```