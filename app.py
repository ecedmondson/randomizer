from random import choice
from random import sample

import emoji
from faker import Faker
from flask import Flask
from flask import request
from flaks import render_template
from flask import jsonify

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

class IPMsg:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    @property
    def value(self):
        return f"Hello person! Your ip address is {self.ip_address}."

class RandomResponse:
    def __init__(self):
        self.number = RandomNumber()
        self.text = RandomText()
        self.photo = RandomPhoto()
        self.emoji = RandomEmoji()
        self.randoms = [self.number, self.text, self.photo, self.emoji]
 
    def get_random_thing(self):
        return choice(self.randoms).value        
    
response_generator = RandomResponse()

@app.route("/api/random", methods=["POST"])
def get_random_thing():
    response_generator.randoms.append(IPMsg(request.remote_addr))
    random_value = response_generator.get_random_thing()
    response_generator.randoms.pop(len(response_generator.randoms) - 1)
    if "lorempixel" in str(random_value):
        return jsonify({"randomphoto": random_value})
    return jsonify({"random": random_value})

@app.route("/")
def homepage():
    return render_template("homepage.html")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
