from matplotlib import image
import matplotlib.pyplot as plt
from matplotlib.image import imread
from tensorflow import keras
from os import listdir
from numpy import asarray, save
from detecto import core


#mention you dataset path
dataset = core.Dataset('C:/Users/nhi/Desktop/CountingFish/dataset')
#mention you object label here
model = core.Model(['fish'])


#train data
model.fit(dataset, epochs=100, verbose=1)

#save data
model.save ('fish_model.pth')

