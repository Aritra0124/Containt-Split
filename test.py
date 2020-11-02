import os, shutil, random, time

path = os.getcwd()

try:
	os.mkdir(path + '/' + 'validation')
	os.mkdir(path + '/' + 'validation' + '/' + 'cracked')
	os.mkdir(path + '/' + 'validation' + '/' + 'uncracked')

except OSError:
	print("Already present")


rng1 = len(os.listdir(path+ '/' + 'train' + '/' + 'cracked'))import os, shutil, random

path = os.getcwd()

try:
	os.mkdir(path + '/' + 'validation')
	os.mkdir(path + '/' + 'validation' + '/' + 'cracked')
	os.mkdir(path + '/' + 'validation' + '/' + 'uncracked')

except OSError:
	print("Already present")


rng1 = len(os.listdir(path+ '/' + 'train' + '/' + 'cracked'))
rng2 = len(os.listdir(path+ '/' + 'train' + '/' + 'uncracked'))



print("\n---------CRACKED-------\n")

k = int(rng1 * .3)
count = 1
while count != 0:
	count = 0
	for i in range(0, k):
		print("\nPosition:  ", i)
		try:
			pos = random.randint(0,rng1)
			shutil.move(os.path.join(path+ '/' + 'train' + '/' + 'cracked', os.listdir(path + '/' + 'train' + '/' + 'cracked')[pos]), path + '/' + 'validation' + '/' + 'cracked')

		except:
			print("Cant Get Data \n")
			count += 1
	k = count
	

print("\n---------UNCRACKED-------\n")		

k = int(rng2 * .3)
count = 1
while count != 0:
	count = 0
	for i in range(0, k):
		print("\nPosition:  ", i)
		try:
			pos = random.randint(0,rng2)
			shutil.move(os.path.join(path+ '/' + 'train' + '/' + 'uncracked', os.listdir(path + '/' + 'train' + '/' + 'uncracked')[pos]), path + '/' + 'validation' + '/' + 'uncracked')

		except:
			print("Cant Get Data \n")
			count +=1
	k = count
	
print("DONE !!!")
rng2 = len(os.listdir(path+ '/' + 'train' + '/' + 'uncracked'))



print("\n---------CRACKED-------\n")


for i in range(0, (int(rng1 * .3))):
	print("\nPosition:  ", i)
	try:
		pos = random.randint(0,rng1)
		shutil.move(os.path.join(path+ '/' + 'train' + '/' + 'cracked', os.listdir(path + '/' + 'train' + '/' + 'cracked')[pos]), path + '/' + 'validation' + '/' + 'cracked')

	except:
		print("Cant Get Data \n")
		
		
print("\n---------UNCRACKED-------\n")		

for i in range(0, (int(rng2 * .3))):
	try:
		pos = random.randint(0,rng2)
		shutil.move(os.path.join(path+ '/' + 'train' + '/' + 'uncracked', uncrack[rng2]), path + '/' + 'validation' + '/' + 'uncracked')

	except:
		print("Cant Get Data \n")
