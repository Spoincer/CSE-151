import math

f = open("hw3train.txt").readlines()

lst = []
for i in range(len(f)):
	lst.append(f[i].strip('\n'))

lst2 = []
for i in range(len(lst)):
	j = lst[i].split()
	lst2.append(j)


vectors = [[float(x) for x in lst2] for lst2 in lst2]
ResultLeft = []
ResultRight = []
zNum = 0
value = 0.0
dTreeAssign=0
ultimateR = []
ultimateL = []

def split(z):
	print("value",value, "z", z)
	Total = len(vectors)
	for i in range(0,Total):
		#print(len(ResultLeft))
		#print(len(ResultRight))
		if vectors[i][z] <= value:
			ResultLeft.append(vectors[i])
		else:
			ResultRight.append(vectors[i])

	print(ResultLeft)
	print(ResultRight)
	
	



def HX():
	labels = [0,0,0]
	total = len(vectors)
	first = 0
	for i in range(0,total):
		labels[int(vectors[i][4])-1] += 1


	for k in range(0, len(labels)):
		if(labels[k] == 0):
			first = first
		else:
			 
			first = first + (-labels[k]/total)*(math.log(labels[k]/total))
	
	return (first)

	#return (-(labels[0]/total)*(math.log10(labels[0]/total)))-((labels[1]/total)*(math.log10(labels[1]/total)))-((labels[2]/total)*(math.log10(labels[2]/total)))

def Pr(var):
	total = len(vectors)
	print("total pr", total)

	if var>0:
		return len(ResultLeft)/total
	else:
		return len(ResultRight)/total
	

def HXZ():
	Yes = 1
	No = 0

	return Pr(Yes)*HXZV(Yes) + Pr(No)*HXZV(No)

def HXZV(var):
	totalLeft = len(ResultLeft)
	totalRight = len(ResultRight)
	total = 0
	first = 0
	labels = [0,0,0]
	#print(total)
	
	print("len left = ", len(ResultLeft))
	print("len right = ", len(ResultRight))
	totalLeft = len(ResultLeft)
	totalRight = len(ResultRight)

	if var>0:
		for i in range(0,totalLeft):
			#print("something", vectors[i][4]-1)
			labels[int(vectors[i][4])-1] += 1
	
	else:
		for i in range(0,totalRight):
			labels[int(vectors[i][4])-1] += 1

		
	
	total = totalLeft+totalRight
	
	for k in range(0, len(labels)):
		if(labels[k] == 0):
			first = first
		else:
			 
			first = first + (-labels[k]/total)*(math.log10(labels[k]/total))
	
	return (first)
	
	#print(math.log10(0.0))
	#return (-(labels[0]/total)*(math.log10(labels[0]/total)))-((labels[1]/total)*(math.log10(labels[1]/total)))-((labels[2]/total)*(math.log10(labels[2]/total)))
	
def main():
	global vectors
	impure = len(vectors)
	pure = 0
	zList = [1,1,1,1]
	IG = 0.0
	maxIG = 0
	minIG = 99999
	maxIGsplit = [0,0]
	dTree = [0,0,0,0,0,0,0,0]
	counter = 0;
	side = 1;
	temp = 0;
	tempx=0;
	global value
	global dTreeAssign
	global ultimateR
	global ultimateL
	global zNum
	global vectors
	print(dTree)
	width = 0
	height = 0

	while True:
		#print("value up", len(vectors))
		llabel = [0,0,0]
		rlabel = [0,0,0]
		for i in range(0, 100):
			llabel = [0,0,0]
			rlabel = [0,0,0]
			value += 0.1
			i = value
			
			
			for j in range(len(zList)):
				zNum = j
				if zList[j] != 0:
)
					del ResultLeft[:]
					del ResultRight[:]
					split(j)
)

					IG = HX() - HXZ()
	)

					if IG > maxIG:
						print("IG", IG)
						print("max", maxIG)
						maxIG = IG
						maxIGsplit = [j,value]
						temp = j
						tempx=value
						print(ResultLeft)
						print(ResultRight)
						ultimateL = []
						ultimateR = []
						for i in range(0, len(ResultLeft)):
							ultimateL.append(ResultLeft[i])
						for i in range(0, len(ResultRight)):
							ultimateR.append(ResultRight[i])
						
						width = len(ultimateL)
						length = len(ultimateR)
						


		for k in range(0, 1):
			if dTreeAssign +k > len(dTree)-1:
				break
			if dTree[dTreeAssign + k]-1 < 0 :
				dTree[dTreeAssign+k] = maxIGsplit[0]
				dTree[dTreeAssign+k+1] = maxIGsplit[1]
			dTreeAssign += 2

		maxIGsplit=[0,0]
		for k in range(0, len(ultimateL)):
			llabel[int(ultimateL[k][4])-1] += 1 
		for k in range(0, len(ultimateR)):
			rlabel[int(ultimateR[k][4])-1] += 1

		del vectors[:]
		
		print(max(rlabel))
		print(max(llabel))

		break

		if(max(rlabel)>max(llabel)):
			for i in range (0, length):
				vectors.append(ultimateR[i])
			print("no")
		else:
			for i in range (0, width):
				vectors.append(ultimateL[i])
			print("yes")

		if(max(rlabel) == 0):
			if(max(llabel) == 0):
				print(dTree)
				break
		
		rlabel = []
		llabel = []
		del ultimateL[:]
		del ultimateR[:]
		
		
			#print("shouldn't be here yet")
		#	counter = len(ultimateR)
		#	vectors = ultimateR

		#else:
			#print("shouldn't be either here yet")
		#	vectors = ultimateL
		
		#print("value down", value)
		counter = 0
		side = 0
		value = 0.0

		if(impure == 0):
			break
	
	print(dTree)


if __name__ == "__main__":
    main()

