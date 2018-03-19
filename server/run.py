from flask import Flask
from pool.hello_world import hello as hello_blueprint

app = Flask(__name__)
app.register_blueprint(hello_blueprint)

if __name__ == '__main__':
  app.run()