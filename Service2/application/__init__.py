from flask import Flask, Response

import random


app = Flask(__name__)




@app.route('/name', methods=['GET'])
def name():
    names = ["Cal Kestis", "Kylo Ren", "Grand Inquisitor", "Ahsoka Tano", "Shaak-Ti"]
    randname = random.randint(0,4)
    return Response(names[randname], mimetype='text/plain')

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)