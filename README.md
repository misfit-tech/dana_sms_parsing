# Dana SMS Parsing is designed with Django.

## Requirements 
* Python 3.6 or above
* Django 3.1.1

## Install Dependencies

Create a virtual environment using ```pip``` or ```pip3``` before installing dependencies

```
pip3 install virtualenv
```
```
virtualenv venv
```

Activate the virtual environment ```venv```

```
source venv/bin/activate
```

For development and production install ```requirements.txt``` 

``` 
pip install -r requirements.txt
```


Create and configure the ```.env``` file. Run the project with

```
python manage.py runserver
```


Check the ```urls.py``` inside ```core``` folder to navigate to the urls to view the outputs.