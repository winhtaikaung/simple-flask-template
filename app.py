#! usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)


url = os.environ["DB_URL_FORMAT"]
url = url.format(os.environ["DB_USER_NAME"], os.environ["DB_PASSWORD"], os.environ["DB_HOST"], os.environ["DB_PORT"],
                 os.environ["DB_NAME"])

if os.environ["ENV"] == 'local':
    engine = create_engine('sqlite:///lugyone.db', convert_unicode=True)
else:
    engine = create_engine(url, echo=True)


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(engine.url)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
alchemy_app = SQLAlchemy(app)

if os.environ["ENV"] != 'production':
    app.debug = True
else:
    app.debug = False

@app.route('/')
def hello_world():
    try:
        # Example SQL query
        query = text("SELECT version();")
        
        # Execute the query
        result = db_session.execute(query)
        
        # Fetch all rows
        rows = result.fetchall()
        
        # Convert rows to a list of dictionaries
        version = [dict(row) for row in rows]
        
        # Return the result as JSON
        return jsonify(version[0])
    
    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500
    
    finally:
        # Make sure to close the session
        db_session.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))