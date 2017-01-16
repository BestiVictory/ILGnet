import os
import random
import shutil

data_dir = os.path.join(
	os.path.dirname(os.path.realpath(__file__)))


def create_AVA2label():
	score = open(os.path.join(data_dir, 'scores.txt'), "r")
	temp2 = score.readlines()
	train,val = randomChoice(temp2, 25553)
	return train,val

def randomChoice(data, num):
	slice1 = random.sample(data, num)
	slice2 = list(set(data) - set(slice1))
	return slice1,slice2
train,val = create_AVA2label()
for i in range(len(train)):
	f = open(os.path.join(data_dir, 'train.txt'), 'a')
	temp = train[i].split(' ')
	if float(temp[1]) > 5.0:	
		f.write(temp[0] + ' 1\n')
	else:
		f.write(temp[0] + ' 0\n')
	f.close()
for i in range(len(val)):
	f = open(os.path.join(data_dir, 'val.txt'), 'a')
	temp = val[i].split(' ')
	if float(temp[1]) > 5.0:	
		f.write(temp[0] + ' 1\n')
	else:
		f.write(temp[0] + ' 0\n')
	f.close()
