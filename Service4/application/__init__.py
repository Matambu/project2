from flask import Flask, Response, request
import requests

app = Flask(__name__)


@app.route('/databank', methods=['POST'])
def databank():
    generate = request.data.decode('utf-8')
    planet_name = generate.split('-')
    if planet_name[1] == "Cal Kestis" and planet_name[0] == "Tatooine":
        home = "Home of Cal Kestis"
    elif planet_name[1] == "Cal Kestis" and planet_name[0] == "Coruscant":
        home = "Home of Senate"
    elif planet_name[1] == "Cal Kestis" and planet_name[0] == "Kamino":
        home = "Home of Clones"
    elif planet_name[1] == "Cal Kestis" and planet_name[0] == "Ryloth":
        home = "Home of Twilek"
    elif planet_name[1] == "Cal Kestis" and planet_name[0] == "Shili":
        home = "Home of Ahsoka"
    elif planet_name[1] == "Kylo Ren" and planet_name[0] == "Tatooine":
        home = "Home of Uncle"
    elif planet_name[1] == "Kylo Ren" and planet_name[0] == "Coruscant":
        home = "Home of The Senate"
    elif planet_name[1] == "Kylo Ren" and planet_name[0] == "Kamino":
        home = "Home of The Clones"
    elif planet_name[1] == "Kylo Ren" and planet_name[0] == "Ryloth":
        home = "Home of The Twilek"
    elif planet_name[1] == "Kylo Ren" and planet_name[0] == "Shili":
        home = "Home of Ahsoka"
    elif planet_name[1] == "Grand Inquisitor" and planet_name[0] == "Kamino":
        home = "Home of The Clones"
    elif planet_name[1] == "Grand Inquisitor" and planet_name[0] == "Tatooine":
        home = "Home of The Skywalker"
    elif planet_name[1] == "Grand Inquisitor" and planet_name[0] == "Coruscant":
        home = "Home of The Senate"
    elif planet_name[1] == "Grand Inquisitor" and planet_name[0] == "Ryloth":
        home = "Home of The Twilek"
    elif planet_name[1] == "Grand Inquisitor" and planet_name[0] == "Shili":
        home = "Home of Ahsoka"
    elif planet_name[1] == "Ahsoka Tano" and planet_name[0] == "Ryloth":
        home = "Home of The Twilek"
    elif planet_name[1] == "Ahsoka Tano" and planet_name[0] == "Tatooine":
        home = "Home of The Skywalker"
    elif planet_name[1] == "Ahsoka Tano" and planet_name[0] == "Coruscant":
        home = "Home of The Senate"
    elif planet_name[1] == "Ahsoka Tano" and planet_name[0] == "Shili":
        home = "Home of Ahsoka"
    elif planet_name[1] == "Shaak-Ti" and planet_name[0] == "Shilli":
        home = "Home of Ahsoka"
    elif planet_name[1] == "Shaak-Ti" and planet_name[0] == "Tatooine":
        home = "Home of Skywalker"
    elif planet_name[1] == "Shaak-Ti" and planet_name[0] == "Coruscant":
        home = "Home of Senate"
    elif planet_name[1] == "Shaak-Ti" and planet_name[0] == "Kamino":
        home = "Home of Clones"
    elif planet_name[1] == "Shaak-Ti" and planet_name[0] == "Ryloth":
        home = "Home of Twilek"
    else:
        home = "No databank entry"
    return Response(home, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
    
    