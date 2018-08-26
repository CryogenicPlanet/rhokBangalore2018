### Inception v3
This where inception v3 is excuted, trainned and run

To execute this project you will neeed to download inception v3 from [here](https://www.kaggle.com/google-brain/inception-v3)
Please modify the file paths to **retrained_graphs.pb**
and **retrained_labels.txt**
in both **retrain.py** and **label_image.py**

You might also have to change paths to **retrain.py** and **label_image.py** in **run.py** and **check_label_image.py** respectively.

####Check Image Label
This tests all the test images with folder testImage(***change path according to convience***)
and give a final accurary for the model.

### Execute Retain.py
Either use the command in **trainingcommand.txt** or use **run.py**. Modify run.py to change the amount of times you want the model to train
