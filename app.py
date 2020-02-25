from flask import Flask
from apis import blueprint as api


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(debug=True)  # http://127.0.0.1:5000/api/1/

