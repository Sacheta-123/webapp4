import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Vanakkam Da Maxy, Medavakkathula irundhu 😎🤠😈😁🥳🎉❤️"

@app.route('/adei')
def adei():
    return 'Ena mayilu sirichikittu kanda meniku morachikitu 😡🤬😒😈😠'

@app.route('/how-are-you')
def how_are_you():
    return 'Nalla irukken da Mappla 😁😁❤️❤️'

@app.route('/test')
def test():
    return "Tha test work aayduchu da maapla (❁´◡`❁)☆*: .｡. o(≧▽≦)o .｡.:*☆(●'◡'●)╰(*°▽°*)╯"

@app.route('/hey')
def hey():
    return "Ena da Mappla ey nu koopudra 😒. Thakkali aruthu potruven rascolu 🤬😡😠"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
