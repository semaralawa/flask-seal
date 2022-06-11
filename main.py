import os
from flask import (Flask, redirect, url_for)
from flask_mysqldb import MySQL

app = Flask(__name__, instance_relative_config=True)
HTTP_PORT = 80

# configure database mysql
app.config['MYSQL_HOST'] = 'sib-seal-bali-sm2.cbjgmdgmfjls.us-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'sayalupa'
app.config['MYSQL_DB'] = 'seal'

mysql = MySQL(app)


def create_app(test_config=None):
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
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

    import home
    app.register_blueprint(home.bp)

    # first route
    @app.route("/")
    def start():
        return redirect(url_for('home.home'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=HTTP_PORT, debug=True, host='0.0.0.0', use_reloader=True)
