import math

a = input("please type the value of a:\n")
b = input("please type the value of b:\n")

sum = a+b
dif = a-b
prod = a*b
quot = a/b
remainder = a - quot*b
log = math.log10(a)
exp = a**b

print "sum is {0}, diff is {1}, product is {2}, quotient is {3}, remainder is {4}, log10(a) is {5}, a**b is {6}".format(\
sum,dif,prod,quot,remainder,log,exp)




