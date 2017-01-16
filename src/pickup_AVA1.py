import os
import random
import shutil

data_dir = os.path.join(
	os.path.dirname(os.path.realpath(__file__)))

def create_AVA1label():
	f = open(os.path.join(data_dir, 'result.txt'), "r")
	zero = []
	one = []
	train = []
	val = []
	for lines in f.readlines():
		pre = lines.split(' ')
		if int(pre[1]) == 0:
			zero.append(lines)
		else:
			one.append(lines)
	f.close()
	val,zero,one = randomChoice(zero,one,5700, 14000)
	train = zero + one
	return train, val
def randomChoice(zero, one, num1, num2):
	slice1 = random.sample(zero, num1)
	zero = list(set(zero) - set(slice1))
	slice2 = random.sample(one, num2)
	one = list(set(one) - set(slice2))
	val = slice1 + slice2
	return val,zero,one
train,val = create_AVA1label()
for i in range(len(train)):
	f = open(os.path.join(data_dir, 'train.txt'), 'a')
	f.write(train[i])
	f.close()
for i in range(len(val)):
	f = open(os.path.join(data_dir, 'val.txt'), 'a')
	f.write(val[i])
	f.close()
