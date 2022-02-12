from random import choice

from flask import Flask

app = Flask(__name__)

class RandomNumber:
    @property
    def value(self):
        return choice(range(0, 100000))

@app.route("/")
def homepage():
    return "Welcome to Randomizer!"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
