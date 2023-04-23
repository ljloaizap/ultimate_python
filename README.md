# Python Course
*"Ultimate Python* -- Udemy resource ([link](https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/learn/lecture/36468872#overview)), with Nicolás from _Hola Mundo_.

## Getting started

### VS Code Extensions & Format
- `python` by Microsoft
- `pylint` by Microsoft
- Open `palette` view and look for Format. Install `autopep 8`.
- Auto formatting: `manage > settings`, then type `formatOnSave` and tick first option _"Format a file on save"_.
- `Django` by Baptiste Darthenay


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
pipenv install pylint-django
```


# Useful links
- PEP 8 – Style Guide for Python Code -> [link](https://peps.python.org/pep-0008/)
- Fake API `(typicode)` -> [link](https://jsonplaceholder.typicode.com/)
- Complete list of github markdown emoji markup -> [link](https://gist.github.com/rxaviers/7360908)

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

### Pylint with Django
Pylint indicates some compilation errors because does not totally match with django instructions. In order to avoid that, follow these steps:
1. Install new package: `pipenv install pylint-django`
2. Create new file (only with extension): `.pylintrc`
3. Indicate plugins to load by adding this line in that newly created file (_.pylintrc_): `load-plugins=pylint-django` 
4. Voilà!

### Share base template across the apps
1. Go to root directory, which is at the same level as {app_dir} is, e.g., `productly` dir.
2. Create new directory `templates` at the same as {app_dir} is.
3. Add `base.html` file in `templates` new dir.
4. Modify `settings.py` to tell Django which templates dir to load in `TEMPLATES` list field.

### URLs with params
URLs params are useful for views such as detail pages. To do so:
1. Go to _urls_ file of {app_dir}: `products/urls.py`
2. Add new URL specifying name and params
3. If need to specify param type, put it before param name: `<int:product_id>`
4. Go to _views_ and add URL function in {app_dir}: `products/views.py`

### Forms
1. Register app. Go to `settings.py` and locate `INSTALLED_APPS` list
2. Add app `django.forms` **before** registering the rest of custom apps
3. Under {app_dir}, create _forms_ file: `products/forms.py`
4. In _forms.py_, create new class form, e.g., `class ProductForm(ModelForm)`
5. Go to _templates_ and create app form, e.g., `products/templates/product_form.html`
6. :warning: Add `csrf_token` for **security** purposes. **It always must be added.** :warning:
7. Open {app_dir} _views_ file: `products/views.py`
8. Add new function to render the template described above: `def form(request):`
9. Go to app URLs file: `products/urls.py`
10. Add url for that form page: `path('form', views.form, name='form')`

### Customize forms and fields
11. **Forms**: Add class `CustomFormRenderer` and `FORM_RENDERER` in `settings.py`
12. **Fields**: go to [django github site](https://github.com/django/django/tree/main/django/forms/templates/django/forms/widgets) to copy code for the needed elements, such as `input.html`, `select.html`, etc.
13. :warning: Those _html_ files must be copied using exactly the same structure as django github site.

### Create custom filters
A custom filter was used in this project for validation purposes in the forms, so the fields have some css class of bootstrap framework to be highlighted in red when data is invalid to be submitted. In order to create those filters:
1. Under _{app_dir}_ dir, create new folder `templatetags`
2. In prior dir, add module `add_attr.py` to register new filter
3. Open `form_snippet.html` file. At the beginning, add `{% load add_attr %}`
4. Using `|` operator, indicate the portion of code that needs to be added. For this case, it was `field|add_attr:"class:is-invalid"`
5. Later, go to the html element, e.g., `input.html` file and add widget class like `class="form-control {{ widget.attrs.class }}"`
6. Voilà!
