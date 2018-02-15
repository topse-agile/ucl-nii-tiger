import flask

from flask import render_template
from flask import request,session

app = flask.Flask(__name__)

@app.route('/')
def index(sport=0,price=0):
    return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport, price=price)

@app.route('/price', methods = ['GET','POST'])
def price(sport=0,price=0):
    sport = request.form['sports']
    if requst.method == 'GET':
        price = request.form['price']
        return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport, price = price)
    else:
    #calculator = PriceCalculating()
    #calculator.setSport(sport)
    #price = calculator.calculate()
        return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport, price = price)

class PriceCalculating():
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
    app.run(debug=True)
