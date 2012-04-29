import os

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')
animal = app.config['ANIMAL']

@app.route("/")
def wombat():
    print
    return "You know what's cool? %s. %s are cool" % (animal, animal)

if __name__ == "__main__":
    app.run()
