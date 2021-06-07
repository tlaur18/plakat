import Familie

bestået, i_live, job = True, False, True
final = None
const = None
readonly = None

class Den_Falske_Tysker():
    pass

def sov():
    pass

def nyd():
    pass

def make_it_rain():
    pass

# ---------------- ALT HEROVER KOMMER IKKE MED PÅ PLAKATEN --------------------------

# To Victor
import sys
from urllib.request import urlopen
from flask import Flask, render_template
from SDU import Tolvtal
from Familie import Glæde, Gaver, Kage

class Victor():
    def __init__(self):
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
            for værdi in værdier: nyd(værdi)

        if job:
            make_it_rain()
        else:
            hjemløs = True

        final const readonly Signe = Den_Falske_Tysker("Cand.mag. i Kultur og Formidling")

        app = Flask("Victor Final Final")
        @app.route('/Tillykke') # Fra Thomas og Rosa
        def fejring_24062021():
            # return render_template("HipHipHurra.html")
            return urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/templates/HipHipHurra.html').read()

        @app.route('/favicon.ico')
        def hjerteligt_tillykke():
            return urlopen('https://raw.githubusercontent.com/tlaur18/plakat/main/static/flotfyr.ico').read()

        app.run(host='0.0.0.0', port=5005)

        # TODO: *Noget der skal gøres i fremtiden*


# ---------------- ALT HERUDNER KOMMER IKKE MED PÅ PLAKATEN --------------------------
        if hjemløs and titel and Signe:
            pass
            fejring_24062021
            hjerteligt_tillykke
            Tolvtal
            Glæde
            Gaver

Victor()