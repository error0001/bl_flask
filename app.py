from flask import Flask
# создали приложение с помощью модуля
app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome'


if __name__ == '__main__':
    app.run()
