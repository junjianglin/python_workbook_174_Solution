# the solution in the book is optimal but too simple, here we give the optimal dynamic programming solution
coins = input("input a number of cents in integer\n")

pennies = 1
nickels = 6      #in order to make it harder, we make nickles to be 6
dimes = 10
quarters = 25    #limit the denominations to only 4 types

from collections import Counter
def reconstructCoins(pre_ls,cur):
	count = Counter()
	if pre_ls[cur] == -1:
		count[cur] += 1
		return count
	else:
		count[cur - pre_ls[cur]] += 1
		return count + reconstructCoins(pre_ls, pre_ls[cur])

def makeChange(coin,deno):
	ls = [0]*(coin+1)
	pre_ls = [0]*(coin+1)
	#print pre_ls
	for de in deno:
		if de <= coin:
			ls[de] = 1
			pre_ls[de] = -1
	for i in range(2,coin+1):
		if pre_ls[i] != -1:
			temp_min = []
			for de in deno:
				if i - de >= 0:
					temp_min.append((ls[i-de]+1,i-de))
			min_tuple = min(temp_min)
			ls[i] = min_tuple[0]
			pre_ls[i] = min_tuple[1]
	
	count = reconstructCoins(pre_ls,len(pre_ls)-1)
	print ls[-1]
	#print pre_ls
	print count
#	print "The minimum number of coins is {0}, combination is {1}"

deno = [1,6,10,25]
makeChange(coins,deno)




