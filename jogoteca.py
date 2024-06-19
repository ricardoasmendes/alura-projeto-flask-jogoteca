<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import *


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import *


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 94297a76e657a1d2b6fbbd963dc469bd24a6eba1
