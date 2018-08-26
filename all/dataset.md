### This folder while named all, represents the json dataset which comes along with the images in [#trainingData](https://github.com/CryogenicPlanet/rhokBangalore2018/blob/master/trainingData/trainingData.md)
These are the json files required to understand the dataset. These file can be downloaded [here](https://github.com/visipedia/inat_comp#data) under annoted training files.

### Script.py
After copying the images from ``` trainingdata/ to Inception/ML/tf_files/Test ```
Excute **script.py** with arguments of the start number and the number of elements after.
For example, if you copy only mammalia into the Test folder, then you would execute command
``` python3 script.py 4030 233 ```
