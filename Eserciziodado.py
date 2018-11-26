import random

I=0

numeri=[0, 0, 0, 0, 0, 0]

while I<1000000:
	num=random.randrange(1,7)


	if num == 1:
		numer1[0]+=1
	elif num == 2:
		numer1[1]+=1
	elif num == 3:
		numer1[2]+=1
	elif num == 4:
		numer1[3]+=1
	elif num == 5:
		numer1[4]+=1
	elif num == 6:
		numer1[5]+=1

	I+=1

print ("------------------------")
print ("numero 1 ==",numeri[0])
print ("------------------------")
print ("numero 2 ==",numeri[1])
print ("------------------------")
print ("numero 3 ==",numeri[2])
print ("------------------------")
print ("numero 4 ==",numeri[3])
print ("------------------------")
print ("numero 5 ==",numeri[4])
print ("------------------------")
print ("numero 6 ==",numeri[5])
print ("------------------------")
print ("Fine")