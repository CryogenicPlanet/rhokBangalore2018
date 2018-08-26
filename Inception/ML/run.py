import os
for i in range(1,10):
	os.system("python3 /root/Inception/ML/retrain.py --bottleneck_dir=/root/Inception/ML/bottlenecks --how_many_training_steps 100000  --model_dir=/root/Inception/ML/inception --output_graph=/root/Inception/ML/retrained_graph.pb --output_labels=/root/Inception/ML/retrained_labels.txt --image_dir=/root/Inception/ML/tf_files/Test")
