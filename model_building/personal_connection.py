import sqlalchemy
def create_connection():
    username = 'postgres'  # DB username
    password = 'djru'  # DB password
    host = '34.86.10.136'  # Public IP address for your instance
    port = '5432'
    database = 'homes'  # Name of database ('postgres' by default)

    db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        username, password, host, port, database)

    engine = sqlalchemy.create_engine(db_url)

    conn = engine.connect()
    return conn
