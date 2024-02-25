import os

from flask import Flask, render_template, jsonify
from . import db
import requests


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/wordcount')
    def word_count():
        # Get the database connection
        database_connection = db.get_db()

        # Perform the SQL query to get word counts
        posts_with_word_counts = database_connection.execute(
            'SELECT id, title, LENGTH(body) - LENGTH(REPLACE(body, " ", "")) + 1 AS word_count '
            'FROM post '
            'ORDER BY word_count DESC'
        ).fetchall()
        posts_with_word_counts = [dict(row) for row in posts_with_word_counts]

        data = jsonify(posts_with_word_counts)
        

        return render_template('word-count.html', posts=posts_with_word_counts)


    @app.route('/robot')
    def robot():
        # Get the database connection
        database_connection = db.get_db()

        # Perform the SQL query to get word counts
        posts_with_word_counts = database_connection.execute(
            'SELECT id, title, LENGTH(body) - LENGTH(REPLACE(body, " ", "")) + 1 AS word_count '
            'FROM post '
            'ORDER BY word_count DESC'
        ).fetchall()
        posts_with_word_counts = [dict(row) for row in posts_with_word_counts]

        data = jsonify(posts_with_word_counts)
        

        return render_template('robot.html')

    @app.route('/connect')
    def connect():
        print("connect hit, sending")
        res = requests.get('http://localhost:5555/connect')
        print("sent")
        return jsonify(res.json())

    @app.route('/forward')
    def forward():
        print("before request to 5555")
        response = requests.get('http://localhost:5555/forward')
        print("after request to 5555")
        return jsonify(response.json())

    @app.route('/right')
    def right():
        print("before request to 5555")
        response = requests.get('http://localhost:5555/right')
        print("after request to 5555")
        return jsonify(response.json())
    
    @app.route('/left')
    def left():
        print("before request to 5555")
        response = requests.get('http://localhost:5555/left')
        print("after request to 5555")
        return jsonify(response.json())

    @app.route('/back')
    def back():
        print("before request to 5555")
        response = requests.get('http://localhost:5555/back')
        print("after request to 5555")
        return jsonify(response.json())
    
    @app.route('/disconnect')
    def disconnect():
        print("before request to 5555")
        response = requests.get('http://localhost:5555/disconnect')
        print("after request to 5555")
        return jsonify(response.json())

    return app