import math
import numpy as np

f= open("hw4atrain.txt").readlines()

def multi(y, x):
	for i in range( len(x)):
		x[i] = y*x[i]
	return x

###Training data
lst = []
for i in range(len(f)):
	lst.append(f[i].strip('\n'))

lst2 = []
for i in range(len(lst)):
	j = lst[i].split()
	lst2.append(j)
	
Vectors = [[int(x) for x in lst2] for lst2 in lst2]


###Testing data
g = open("hw4atest.txt").readlines()
lst3 = []
for i in range(len(g)):
	lst3.append(g[i].strip('\n'))

lst4 = []
for i in range(len(lst3)):
	j = lst3[i].split()
	lst4.append(j)
	
testVectors = [[int(x) for x in lst2] for lst2 in lst2]


tlabels = []
tvects = []
for i in range(len(testVectors)):
	tlabels.append(testVectors[i][-1])
	tlabels[i] = ((tlabels[i] - 3)/3)
	tvects.append(testVectors[i][0:-1])

vec = [0]*785
w0 = [0]*784
w1 = [0]*784

labels = []
vects = []
for i in range(len(Vectors)):
	labels.append(Vectors[i][-1])
	labels[i] = ((labels[i] - 3)/3)
	vects.append(Vectors[i][0:-1])


###Perceptron algorithm
for t in range(0,1):
	for i in range(len(vects)):
		if( (labels[i] * np.dot(w0, vects[i])) <= 0):
			a = np.array(w0)
			b = np.array(multi(labels[i], vects[i]))
			w1 = a+b
		else :
			w1 = w0
		w0 = w1
	
count = 0
count1 = 0
###Classifier
for i in range(len(tvects)):
	if (np.dot(w1, tvects[i])>0):
		if(tlabels[i]<= 0):
			count+=1

	else:
		if(tlabels[i]> 0):
			count+=1

###Error check
for i in range(len(vects)):
	if (np.dot(w1, vects[i])>0):
		if(labels[i]<= 0):
			count1+=1

	else:
		if(labels[i]> 0):
			count1+=1

print(count/1000)






