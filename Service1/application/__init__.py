from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)




@app.route('/', methods =['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    name = requests.get('http://Service2:5001/name').text
    planets = requests.get('http://Service3:5002/planet').text
    generate = planets + '-' + name
    home = requests.post("http://Service4:5003/databank", data=generate).text
    return render_template('index.html', name=name, planets=planets, home=home)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')