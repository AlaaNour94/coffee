import os
from flask import Flask
from database.db import initialize_db

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost/coffee")
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'host': DATABASE_URL}

initialize_db(app)
