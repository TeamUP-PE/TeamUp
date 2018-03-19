import os
from flask import Flask
from pool.hello_world import hello as hello_blueprint

config_name = os.getenv('FLASK_CONFIG')

app = Flask(__name__)
app.register_blueprint(hello_blueprint)
app.config.from_pyfile('config.py')

if __name__ == '__main__':
    app.run()
