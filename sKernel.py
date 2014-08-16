

import numpy as np

#Training Data
f= open("hw5train.txt").readlines()
lst = []
for i in range(len(f)):
	lst.append(f[i].strip('\n'))

lst2 = []
for i in range(len(lst)):
	j = lst[i].split()
	lst2.append(j)


for i in range(len(lst2)):
	lst2[i][-1] = int(lst2[i][-1])
	seq = lst2[i][0]
	label = lst2[i][1]

#Testing data
g = open("hw5test.txt").readlines()
lst3 = []
for i in range(len(g)):
	lst3.append(g[i].strip('\n'))

lst4 = []
for i in range(len(lst3)):
	j = lst3[i].split()
	lst4.append(j)


for i in range(len(lst4)):
	lst4[i][-1] = int(lst4[i][-1])
	testSeq = lst4[i][0]
	testLabel = lst4[i][-1]



def lcs(s,t,y):
	lst = []
	for i in range(len(s)):
		subseq = s[i:i+y]
		lst.append(subseq)
	#	print(lst)
	
	lst2 = []
	for j in range(len(t)):
		subseq2 = t[j:j+y]
		lst2.append(subseq2)
	
	lst3 = list(set(lst)&set(lst2))
	
	return len(lst3)

size = 4
wt = 0

for i in range(len(lst2)):
	for j in range(i, len(lst2)):
		if(i != j):
			if(lst2[i][1] * wt <= 0):
				wt += lst2[i][1]*lcs(lst2[i][0], lst2[j][0], size)


error =0

for i in range(len(lst4)):
	if(lst4[i][1]>0 and wt <= 0):
			error += 1
	if(lst4[i][1]<=0 and wt>0):
			error += 1



print(error/len(lst2))
