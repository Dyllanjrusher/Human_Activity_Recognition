from flask import Flask,send_file, Response, render_template, jsonify, redirect, request, url_for
import sqlalchemy
from flask_migrate import Migrate
import os
from time import sleep
import json

username = 'postgres'  # DB username
password = 'djru'  # DB password
host = 'localhost'  # Public IP address for your instance
port = '5432'
database = 'class_prediction_api'  # Name of database ('postgres' by default)
db_uri = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    username, password, host, port, database)
engine = sqlalchemy.create_engine(db_uri)
conn = engine.connect()


app = Flask(__name__)
#
# @app.route('/page')
# def get_page():
#     return send_file('index.html')

@app.route('/')
def main():
    """
    Homepage: serve our visualization page, index.html
    """
    return render_template('/index.html')
# @app.route("/")
# def index():
#     if request.headers.get('accept') == 'text/event-stream':
#         def events():
#             for i in range(100000):
#                 cursor = conn.execute('SELECT * FROM {} LIMIT 1 OFFSET {}'.format(home, i))
#                 sleep(.15)
#                 yield '{}\n'.format(cursor.fetchall())
#         return Response(events(), content_type='text/event-stream')
#     return redirect('index.html')
def eventStream():
    for i in range(100000):
        cursor = conn.execute('SELECT * FROM {} LIMIT 1 OFFSET {}'.format('csh102', i))
        # yield '{}\n'.format(cursor.fetchall())
        results = cursor.fetchall()
        json_data = json.dumps(
            {'index': results[0][0],
            'true': results[0][1],
            'pred': results[0][2],
            'sensors': results[0][3]}
        )
        yield f"data:{json_data}\n\n"
        sleep(1)

@app.route("/csh102")
def listen_for_stream():
    return Response(eventStream(), mimetype='text/event-stream')

@app.before_first_request
def _run_on_start():
    eventStream()
    # return Response(eventStream(), mimetype="text/event-stream")

# @app.route('/static/<home>')
# def show_home(home):
#     def eventStream():
#         for i in range(100000):
#             cursor = conn.execute('SELECT * FROM {} LIMIT 1 OFFSET {}'.format(home, i))
#             sleep(.15)
#             yield '{}\n'.format(cursor.fetchall())
#     return Response(eventStream(), mimetype='text/event-stream')
# @app.route('/<home>')
# def show_home(home):
#     def generate():
#         for i in range(100000):
#             cursor = conn.execute('SELECT * FROM {} LIMIT 1 OFFSET i'.format(home))
#             sleep(1)
#     return render_template('print_items.html', items=cursor.fetchall())


if __name__ == '__main__':
    app.run(debug=True)
