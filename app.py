from random import choice

import emoji
from faker import Faker
from flask import Flask

app = Flask(__name__)

class RandomNumber:
    @property
    def value(self):
        return choice(range(0, 100000))

class RandomText:
    def __init__(self):
        self.faker = Faker()

    @property
    def value(self):
        return choice(
            [
                self.faker.catch_phrase(),
                "".join(self.faker.paragraphs()),
            ]
        )

class RandomPhoto:
    @property
    def value(self):
        pixels = [100, 150, 200, 250, 300, 350, 400]
        pixelw = choice(pixels)
        pixell = choice(pixels)
        return f"http://lorempixel.com/{pixelw}/{pixell}/animals/",

class RandomEmoji:
    @property
    def value(self):
        emojis = list(emoji.EMOJI_ALIAS_UNICODE_ENGLISH.values())
        number = choice([1,3,5,7,51])
        return "".join(sample(emojis, number))

@app.route("/")
def homepage():
    return "Welcome to Randomizer!"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
