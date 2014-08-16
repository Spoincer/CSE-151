from numpy import matrix
import numpy as np
import math

f= open("hw2train.txt").readlines()
#print(f)

lst = []
for i in range(len(f)):
	lst.append(f[i].strip('\n'))

#print(lst)
lst2 = []
for i in range(len(lst)):
	j = lst[i].split()
	lst2.append(j)
	
#Vectors from training data
trVectors = [[int(x) for x in lst2] for lst2 in lst2]

#Labels from training data
lst3 = []
for i in range(len(trVectors)):
	lst3.append(trVectors[i][-1])

#e= open("hw2validate.txt").readlines()
e= open("hw2test.txt").readlines()
lst4 = []
for i in range(len(e)):
	lst4.append(e[i].strip('\n'))

lst5 = []
for i in range(len(lst4)):
	j = lst4[i].split()
	lst5.append(j)
	
#Vectors from validation/test data
valVectors = [[int(x) for x in lst5] for lst5 in lst5]

#Labels from validation/test data
lst6 = []
for i in range(len(valVectors)):
	lst6.append(valVectors[i][-1])


##### METHOD TO COMPUTE DISTANCE AND GET LABELS
#k = [1,3,5,11,16,21]
k=1
minDist = [99999999999]*k
output = [0]*k
labels = []
singleoutput = 0
temp = 0

#Calculations to get distance from points
for i in range(len(valVectors)):
	for j in range(len(trVectors)):
		a = matrix(valVectors[i][0:len(valVectors)-1])
		b = matrix(trVectors[j][0:len(trVectors)-1])

		sub = a-b
		sq = np.power(sub,2)
		sqsum = sq.sum()
		dist = math.sqrt(sqsum)

		if dist <  minDist[-1]:
			singleout = trVectors[j][-1]

		#Get the minimum distance and output resulting label
		for x in range(k):
			if dist < minDist[x]:

				temp = minDist[x]
				minDist[x] = dist
				dist = temp
			
				temp = output[x]
				output[x] = singleout
				singleout = temp
 

	#Get list of labels
	minDist = [99999999999]*k
	mostcommon = max(set(output), key = output.count)
	labels.append(mostcommon)


##### USED FOR NUMBER 3 PART 1
#Check for errors 
errors = 0
for i in range(0,300):
	if labels[i] != lst6[i]:
		errors += 1
print(errors/300)

##### USED FOR NUMBER 3 PART 2
#Make confusion matrix
matrix = [[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10,
	[0]*10]

for i in range(0,300):
	row=labels[i]
	col=lst6[i]
	matrix[row][col] += 1

for i in range(0,10):
	for j in range(0,10):
		matrix[i][j] = round(matrix[i][j]/count[j],4)

for i in range(0,10):
	print(matrix[i])






