small_cont = input("how many containers holding one liter or less?\n")
big_cont = input("how many containers holding more than one liter?\n")
refund = small_cont*0.1 + big_cont*0.25
print "your total refund will be ${0:.2f}".format(refund)
