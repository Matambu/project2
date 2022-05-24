

from flask import Flask, Response, request
import random
app = Flask(__name__)




@app.route('/planet', methods=['GET'])
def planet():
    planets = ["Tatooine", "Coruscant", "Kamino", "Ryloth", "Shili"]
    randplanet = random.randint(0,4)
    return Response(planets[randplanet], mimetype="text/plain")


if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)