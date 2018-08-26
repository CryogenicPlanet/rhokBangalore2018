import os
from sys import *
import json
valFile = []
arr = []
till = int(argv[1]) + int(argv[2])
with open("val2018.json") as tweetfile:
	pyresponse = json.loads(tweetfile.read())
	arr.append(pyresponse)
for elem in arr[0]["images"]:
	for  i in range(int(argv[1]),till+1):
		if elem["file_name"].find("Mammalia") != -1 and elem["file_name"].find("/"+str(i)+"/") != -1:
			#print(elem["file_name"])
			temp = elem["file_name"].split("/")
			#print()
			valFile.append(temp)
counter = 0
for elem in valFile:
	temp = "/"+elem[2]+"/"+elem[3]
	print(temp)
	os.system("mv /root/Inception/ML/tf_files/Test"+temp + " /root/Inception/ML/testImage/" + elem[2]+"-" + str(counter) + ".jpg")
	counter +=1
	
