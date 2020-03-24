# Random Hacks of Kindness | Bangalore 2018
## Using a pre-trained model to identify plant and animal species.
An inception v3 based convoutional neural network is trained using a dataset provided by Google with pictures of over 35,000 species of organisms, plants and animals. The dataset was slightly skewed as some rare species had as low as 5 images which were insufficient for training the neural network.
The convoutional neural network was trained based on a part of the dataset with varied epoch cycles from 0.3 to 55.
##  Computation
The project was trained on a powerful server with 32 cores and 64gb of memory running Ubuntu operationg system which allowed for fast download speeds and short training times.
## Dependencies
  1. Tensorflow
  2. Inception
  3. Python3
## Executing
 Read all the .md files in each folder to get a clear understanding of how exactly to excute the model.
## Results
The convoutional neural network churned out an average of 60% accuracy. The accuracy could be improved by decreasing the number of species that were to be identified, treating outliers in early stages and by using more images of species which were rare and didn't have enough images.
## Application
The project can be used to understand ecosystems and develop insights on how ecosystems are affected by species present. Researchers may use the project to understand and identify biotic life better and conduct scientific studies.

