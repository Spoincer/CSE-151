

import copy
import math

###Training data
f = open("hw6train.txt").readlines()
lst = []
for i in range(len(f)):
	lst.append(f[i].strip('\n'))

lst2 = []
for i in range(len(lst)):
	j = lst[i].split()
	lst2.append(j)
	
Vectors = [[int(x) for x in lst2] for lst2 in lst2]
dt = copy.deepcopy(Vectors)

###Testing data
g = open("hw6test.txt").readlines()
lst3 = []
for i in range(len(g)):
	lst3.append(g[i].strip('\n'))

lst4 = []
for i in range(len(lst3)):
	j = lst3[i].split()
	lst4.append(j)
	
testVectors = [[int(x) for x in lst2] for lst2 in lst2]

###Dictionary
h = open("hw6dictionary.txt").readlines()
for i in range(len(h)):
	h[i] = h[i].split()
dictionary = [y for x in h for y in x]



for i in range(len(dt)):
	dt[i] = dt[i][:-1]

for i in range(len(dt)):
	for j in range(len(dt[i])):
		dt[i][j] = 1/len(dt[i])


#for i in range(len(Vectors2)):
#	for j in range(len(Vectors2[i])):
#		Vectors2[i][j] = round(Vectors2[i][j],5)
#print(Vectors2)


dtplus = copy.deepcopy(dt)
blah = copy.deepcopy(dt)

errorp = [0]*len(dt[0])
errorm = [0]*len(dt[0])

weight = [1/len(Vectors)]*500

hterm = 0
p = 2
m = 1
def error():
	result = 0
	for i in range(len(dt)):
		for x in range(len(dt[i])):
			if dt[i][x] == 1:
				result = 1
			else:
				result = -1
	
			if result != Vectors[i][-1]:
				errorp[x] += weight[i]
			else:
				errorm[x] += weight[i]
	
	if(min(errorp) <= min(errorm)):
		hterm = p
	else:
		hterm = m

	return min(min(errorp), min(errorm))

w = [0]*500

for t in range(0, 2):
	
	err = error()

	for i in range(len(dt)):

		alpha = 1/2*math.log((1-err)/err)
		yht=1

		for j in range(len(dt[i])):
			if(hterm >1):
				use hplus
				if(dt[i][j] == 1):
					hi = 1
				else:
					hi = -1
			else:
				if(dt[i][j] == 0):
					hi = 1
				else:	
					hi = -1

		w[i] = weight[i]*math.exp(-alpha*yht)

		


