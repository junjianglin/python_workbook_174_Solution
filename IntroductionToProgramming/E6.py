meal_price = input('what is the price of your meal?')
tax_rate = 0.13  #assume tax rate is 0.13
tip = meal_price * 0.18
tax = meal_price * tax_rate
print "Your tax is ${0:.2f}, and your tip is ${1:.2f}, and the grand total is ${2:.2f}".format(tax,tip,meal_price+tax+tip)
