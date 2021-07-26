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
months = float(input('Enter the number of months in a year'))
var1 = float(year / months)
print(f'Your monthly income is {var1} dollars')

x = input('Enter the place you want to live between NY, LA, or Houston:')
if var1 <= 1994 :
   print("Too poor to afford")
else:
    print(f'The average cost of a one bedroom apartment is {money[x]} dollars.')

savings = input('Enter how much of your montly income you want to save')
print("cool")

retirement = input('Enter how much of your montly income you want to save for retirement')
print("BADUM")

renters_insurance = input('Do you want Renters Insurance?')
if renters_insurance == ("yes"):
	print ("It will be added to the budget")
elif renters_insurance == ("no"):
	print ()

cable = input('Do you want cable?')
if cable == ("yes"):
	print ("It will be added to the budget")
elif cable == ("no"):
	print ()

internet = input('Do you want Internet?')
if internet == ("yes"):
	print ("It will be added to the budget")
elif internet == ("no"):
	print ()

phone_data = input('Do you plan on getting a 2 GB data plan or an unlimited plan')
if phone_data == ("2 GB data plan"):
	print ("It will be added to the budget")
elif phone_data == ("Unlimited plan"):
	print ('The cost of an unlimited plan is 100$ a month')

#average cost of gas/electricity = 163

transportation = input('Do you plan on using public transportation or using a car')
print("hole")
#neeed too addd more in this when talking about cars.

groceries = input('Which meal plan are you most likely to follow? Thrifty  Low Cost  Moderate Cost  Liberal Cost')
if groceries == ("Thrifty"):
	print ("It will be added to the budget")
elif groceries == ("Low Cost"):
	print ('The cost of this is 242$ a month')
elif groceries == ("Moderate Cost"):
	print ('The cost of this is 303$ a month')
elif groceries == ("Liberal Cost"):
	print ('The cost of this is 373$ a month')

dining = input('How many times a week do you intend to dining out? (Assuming each meal is 15$)')
if dining == ("Once a week"):
	print ("60$ Added")
elif dining == ("Twice a week"):
	print ("120$ Added")
elif dining == ("Three times a week"):
	print ("200$ Added")
elif dining == ("Five times a week"):
	print ("240$ Added")

h_insurance = input('Do you want Health Insurance?')
if h_insurance == ("yes"):
	print ("The cost of Health Insurance is 440$ a month")
elif h_insurance == ("no"):
	print ()

d_insurance = input('Do you want Dental Insurance')
if d_insurance == ("yes"):
	print ("The cost of Dental Insurance is 30$ a month")
elif d_insurance == ("no"):
	print ()

v_insurance = input('Do you want Vision Insurance')
if v_insurance == ("yes"):
	print ("The cost of Vision Insurance is 18$ a month")
elif v_insurance == ("no"):
	print ()

gym = input('Are you planning to get a gym membership?')
if gym== ("yes"):
	print ("The cost of gym is 53$ a month")
elif gym == ("no"):
	print ()

s_loan = input('Do you have any student loans?')
if s_loan == ("yes"):
	input("How much do you owe?")
elif d_insurance == ("no"):
	print ()

wants = input('How much do you want to spend on other stuff(ex. clothes, entertainment, etc).')
print("cool")


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "is this working?"
