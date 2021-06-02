from flask import Flask, render_template
import urllib.request

app = Flask(__name__)


@app.route('/')
def hello():
    # return render_template("index.html")
    return urllib.request.urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/templates/index.html').read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
