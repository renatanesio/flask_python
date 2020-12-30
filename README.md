# Flask Applications

Repositório com códigos desenvolvidos durante o curso Python and Flask Bootcamp.

### SQL Databases with Flask
  - export FLASK_APP=script.py
  - flask db init
  - flask db migrate -m "message here"
  - flask db upgrade
  - python script.py

### Large Flask Applications
```
project
└─── app.py # main app.py file to be called to start server for web app
└─── requirements.txt # File of pip install statements for your app
└─── migrations # folder created for migrations by calling
└─── myproject # main project folder, sub-components will be in separate folders
│   │   data.sqlite
│   │   models.py
│   │   __init__.py
│   │
│   └─── owners
│   │    │     forms.py
│   │    │     views.py
│   │    └─── templates
│   │         └─── owners
│   │                add_owner.html
│   └─── puppies
│   │    │     forms.py
│   │    │     views.py
│   │    └─── templates
│   │         └─── puppies
│   │                add.html
│   │                delete.html
│   │                list.html
│   └─── static # Where you store your CSS, JS, Images, Fonts, etc...
│   └─── templates
│           base.html
│           home.html

```
