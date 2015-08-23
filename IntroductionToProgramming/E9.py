savings = input("please tell me how much savings do you have")
rate = 0.04
print "after 1 year, your total saving is ${0:.2f}".format(savings*(1+rate))
print "after 2 year, your total saving is ${0:.2f}".format(savings*(1+rate)**2)
print "after 3 year, your total saving is ${0:.2f}".format(savings*(1+rate)**3)

