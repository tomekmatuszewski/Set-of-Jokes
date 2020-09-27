from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/jokes")
def jokes():

    jokes = requests.get("http://official-joke-api.appspot.com//jokes/ten").json()

    return render_template("jokes.html", jokes=jokes)


if __name__ == '__main__':
    app.run(debug=True)