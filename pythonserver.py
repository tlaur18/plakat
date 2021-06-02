from flask import Flask, render_template
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")
    # return urllib.request.urlopen('https://pastebin.com/raw/wp56iDH7').read()


# @app.route('/lookupsICAO', methods=['GET'])
# def lookupsICAO():
#     destination = request.args.get('dest').upper()
#     aircraft = request.args.get('aircraft').upper()

#     # dest, predicted_alternates = MLPclassifier_model.make_prediction(destination, aircraft)
#     dest, predicted_alternates = MLPclassifier_model_minmax.make_prediction(destination, aircraft)


#     dict_data = {"dest": dest.__dict__, "alternates": [ob.__dict__ for ob in predicted_alternates]}

#     json_data = json.dumps(dict_data)

#     if not json_data:
#         return "", 204  # No content

#     return json_data


# @app.route('/getairportinfo', methods=['GET'])
# def getairportinfo():
#     airport = request.args.get('icao').upper()

#     # airport_data = MLPclassifier_model.get_airport_data(airport)
#     airport_data = MLPclassifier_model_minmax.get_airport_data(airport)
#     airport_data["lat"] = airport_data["latitude"]
#     del airport_data["latitude"]
#     airport_data["lon"] = airport_data["longitude"]
#     del airport_data["longitude"]
#     airport_data["icao"] = airport

#     return json.dumps(airport_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
