# Python Course
*"Ultimate Python* -- Udemy resource ([link](https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/learn/lecture/36468872#overview)), with Nicolás from _Hola Mundo_.

## Getting started

### VS Code Extensions & Format
- `python` by Microsoft
- `pylint` by Microsoft
- Open `palette` view and look for Format. Install `autopep 8`.
- Auto formatting: `manage > settings`, then type `formatOnSave` and tick first option _"Format a file on save"_.


### Concepts to keep in mind
**Params vs Arguments**
* **_Params_**: the input variables of a function
* **_Arguments_**: the values we pass when calling a function

**Functions vs Methods**
* **_Functions_**: Block of code to achieve a specific goal
* **_Methods_**: Similar as function but within a class.

**Magic method**
1. Executed without explicit call
2. Starts and ends with `__`, e.g., `__init__`

<br>

# PIP, Virtual envs & pipenv

## PIP

```
pip install requests
pip list
pip uninstall requests
pip install requests==2.18.1
--pip install requests==2.18.*
--pip install requests==2.*
```

## venv
Create virtual environment within current folder
```
python3 -m venv env
deactivate
```

## pipenv
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

<br>

# SQLITE

In case of the following error appears:

```
ModuleNotFoundError: No module named '_sqlite3'
```


Install `sqlite` dev package

```
sudo apt-get update -y
sudo apt-get install -y libsqlite3-dev
```
Cd your _python installer_ directory and run:
```
./configure --prefix=/opt/python3.7.4 --with-ssl --with-pydebugx --enable-loadable-sqlite-extensions --enable-optimizations
make
make install
```

<br>

# Dependencies
(#TODO: This section must go in a _requirements_ file.)
```
pipenv install sendgrid  # emails
pipenv install beautifulsoup4  # web scrapping
pipenv install openpyxl  # excel
pipenv install selenium webdriver-manager  # automated tests with Selenium
pipenv install django==4.1.7
```


# Useful links
- PEP 8 – Style Guide for Python Code -> [link](https://peps.python.org/pep-0008/)
- Fake API `(typicode)` -> [link](https://jsonplaceholder.typicode.com/)

<br>

# Django project

## Installation
Within the virtual environment, cd the directory when Django project is expected to be located. 
For this sample, project name is `productly`. -- A _Django_ project can have >=1 apps.
```
pipenv shell  # activate virtual env
mkdir productly
cd productly  # cd project dir
django-admin startproject productly .  # make sure to type last dot.
python manage.py runserver  # run project  :star:
```


## Apps Creation
### Creating first app
1. Run `python manage.py startapp products` command
2. Go to _{app_dir}_ and open _apps.py_ file: `products/apps.py`
3. Copy class_name, e.g., `ProductsConfig`
4. Go to _{project_dir}_ and open _settings.py_ file: `productly/settings.py`
5. Edit `INSTALLED_APPS` list to add new entry `{app_dir}.apps.{class_name}`: `'products.apps.ProductsConfig'`

### Adding urls

6. Go to _{project_dir}_ and open _urls.py_ file: `productly/urls.py`
7. Append {app} url in `urlpatterns` array
8. Add _view_ reference in a new _urls.py_ file in _{app_dir}_ : `products/urls.py`
9. Go to _{app_dir}_ > _views_ file and add new method referenced in prior point: `products/views.py`, e.g., `def index(request)`

### ORM & db migrations
10. Add models (classes) in _{app_dir}_ > _models_ file: `products/models.py`
11. Make sure `productly/settings.py` has an entry for the app `products` in `INSTALLED_APPS` list, and
12. Make migrations: `python manage.py makemigrations`
13. Run migrations: `python manage.py migrate`  :star:

### Admin panel
14. Create admin user: `python manage.py createsuperuser`
15. Register models > Go to {app_dir} > _admin_ module: `products/admin.py`
16. Edit module to register each model, e.g., `admin.site.register(Category)`
15. Custom admin site: add admin classes in {app_dir} _admin_: `products/admin.py`
