import sys
import subprocess
import os
path = "/root/Inception/ML/testImage/"
accuracy_dict = {}
acc = 0
total = 0
count = 0
for filename in os.listdir(path):
    count += 1
    num = filename.split('-')[0]

    model_output = subprocess.check_output(['python3', 'label_image.py', path + filename])
    output = model_output.decode('utf-8').split('\n')[0]
    accuracy = output.split(' ')[3]
    accuracy = accuracy[:len(accuracy) - 1]
    output = output[:4]
    total +=1
    if output == num:
        accuracy_dict[filename] = ["1", accuracy]
        print(filename, "accurate", str(accuracy) + '%', count)
        acc += 1
    else:
        accuracy_dict[filename] = ["0", accuracy]
        print(filename, "inaccurate", str(accuracy) + '%', count)

print(accuracy_dict)
print(acc/total)
#ython3 label_image.py ./testimage/
