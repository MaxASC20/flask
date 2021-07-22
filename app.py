# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)
money = {
  "NY": 2650,
  "LA": 1995,
  "Houston": 1229
}
year = float(input('Enter your yearly income '))
months = float(input('Enter the number of months'))
var1 = float(year / months)
print(f'Your monthly income is {var1} dollars')

x = input('Enter the place you want to live between NY, LA, or Houston:')
print(f'The average cost of a one bedroom apartment is {money[x]} dollars.')

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "is this working??"
