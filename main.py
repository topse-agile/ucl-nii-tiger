import flask

from flask import render_template
from flask import request

app = flask.Flask(__name__)
g_price = 0
@app.route('/')
def index(sport=0):
    global g_price
    g_price = 0
    return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport)

@app.route('/price', methods=['GET','POST'])
def price(sport=0):
    global g_price
    sport = request.form['sports']
    if sport != '':
        calculator = PrizeCalculating()
        calculator.setSport(sport)
        g_price = calculator.calculate()
    return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport)

@app.route('/poll', methods=['GET'])
def poll():
    local = request.args.get('price')
    while True:
        if local != str(g_price):
            return str(g_price)

class PrizeCalculating():
    #Initialize as 0,
    __sport = 0

    def setSport(self, sport):
        self.__sport = sport

    def calculate(self):
        if self.__sport == 'Diving':
            return 7500
        elif self.__sport == 'Snorkelling':
            return 5000
        else:
            return 0

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
