import Familie

bestået, i_live, job = True, False, True
pengepung = 0

def Den_Falske_Tysker(x):
    pass

def sov():
    pass

# ---------------- ALT HEROVER KOMMER IKKE MED PÅ PLAKATEN --------------------------

# To Victor
import os, sys, urllib.request
from flask import Flask, render_template, send_from_directory
from SDU import tolvtal
from Familie import glæde, gaver, Kage

app = Flask("Victor Final Final")

titel = "Computernørd"
if bestået:
    titel = "Cand.polyt. i Software Engineering"
    Familie.tillykke(stolthedsniveau=sys.maxsize)

værdier = ["Sejlads", "Vandring", "Mad", "Betænktsomhed", "Signe", "Siouxco", "Klogskab", "Bøger", "Kærlighed",
           "Vedholdenhed", "Rejser", "Computerspil", "Øl- og vinsmagning", "Italiensk", "Golf", "Bouldering",
           "Tolvtaller", "Kage", "10000 skridt", "Cremer", "Skygge", "Godhed", "Russisk", "Øl- og Dieselunionen",
           "Ildspyning", "Skæg", "Tegne/Male", "Anders And", "Venner", "Brætspil", "Fotografering", "Hygge"]
while i_live:
    Kage.spis()
    sov()
    for værdi in værdier: liv.nyd(værdi)

if job: pengepung += 1
else: hjemløs = True

final const readonly Signe = Den_Falske_Tysker("Cand.mag. i Kultur og Formidling")

@app.route('/Dannebrog')
def fejring_24062021():
    # return render_template("index.html")
    return urllib.request.urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/templates/index.html').read()

@app.route('/favicon.ico')
def hjerteligt_tillykke(): # Fra Thomas og Rosa
    # return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    return urllib.request.urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/static/favicon.ico').read()

app.run(host='0.0.0.0', port=5005)

# TODO:  