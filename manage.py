import calendar
import datetime
import os
import time
from os.path import join, dirname
from time import strftime, gmtime

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean,  DECIMAL, DATE
from sqlalchemy.orm import relationship

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# OR, the same with increased verbosity:
from database import engine

url = os.environ["DB_URL_FORMAT"]
url = url.format(os.environ["DB_USER_NAME"], os.environ["DB_PASSWORD"], os.environ["DB_HOST"], os.environ["DB_PORT"],
                 os.environ["DB_NAME"])
app.config['SQLALCHEMY_DATABASE_URI'] = str(url)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def generate_uuid():
    import uuid
    return str(uuid.uuid4())


def gen_cursor():
    return str(time.time())



class BaseModel(object):
    id = Column(Integer, primary_key=True)
    object_id = Column(String(50), unique=True, index=True, default=generate_uuid)
    created_date = Column(VARCHAR,index=True, default=str(strftime("%Y-%m-%d %X", gmtime())))
    cursor = Column(DECIMAL, default=gen_cursor, index=True)
    is_disabled = Column(Boolean, default=False)
    updated_date = Column(VARCHAR,index=True, default=str(strftime("%Y-%m-%d %X", gmtime())))

class User(BaseModel)
    name=Column(VARCHAR)
    email=Column(VARCHAR)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()