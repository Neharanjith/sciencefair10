import pandas
import matplotlib.pyplot as pt 
import numpy as np 
import keras
from keras import layers
from keras import ops 
from keras.layers import LSTM 
 

dataset = []
test = []
train = []
val = []



def create_dataset(dataset, look_back=1):   
    dataX = []
    dataY = []
    for i in range(len(dataset) -  look_back - 1):
        a = dataset[i: (i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array((dataX), np.array(dataY))

look_back = 1

trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
valX, valY = create_dataset(val, look_back)

trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))


model = keras.Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))




