# rhokBangalore2018
## Using a pre-trained model to identify plant and animal species.
An inception v3 based convoutional neural network is trained using a dataset provided by Google with pictures of over 35,000 species of organisms, plants and animals. The dataset was slightly skewed as some rare species had as low as 5 images which were insufficient for training the neural network.
The convoutional neural network was trained based on a part of the dataset with varied epoch cycles from 0.3 to 55.
##  Computation
The project was trained on a powerful server with 32 cores and 64gb of memory running Ubuntu operationg system which allowed for fast download speeds and short training times.
## Results
The convoutional neural network churned out an average of 60% accuracy. The accuracy could be improved by decreasing the number of species that were to be identified, treating outliers in early stages and by using more images of species which were rare and didn't have enough images.