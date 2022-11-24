from flask import Flask
from rotas import main

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)