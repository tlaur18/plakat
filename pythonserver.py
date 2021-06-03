import urllib.request
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    # return render_template("index.html")
    return urllib.request.urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/templates/index.html').read()


@app.route('/favicon.ico')
def favicon():
    # return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    return urllib.request.urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/static/favicon.ico').read()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)