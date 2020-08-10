from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



username = 'postgres'  # DB username
password = 'djru'  # DB password
host = 'localhost'  # Public IP address for your instance
port = '5432'
database = 'class_prediction_api'  # Name of database ('postgres' by default)
db_uri = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    username, password, host, port, database)

class House(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    true = db.Column(db.String(100), nullable=False)
    pred = db.Column(db.String(100), nullable=False)
    sensors = db.Column(db.String(80))
    def __repr__(self):
        return '<csh %r>' % self.csh
