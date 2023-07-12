import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text



app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    connection_string = "mysql+mysqlconnector://<username>:<password>@<host>:3306/<database name>"
    engine = create_engine(connection_string, echo=True)
    with engine.connect() as connection:
     connection.execute(text("INSERT INTO employees  VALUES(8,'test',57,75200.00)"))
     connection.commit()
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
