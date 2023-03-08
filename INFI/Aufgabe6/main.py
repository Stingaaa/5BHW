import collections
import numpy as np
import pandas as pd
from tensorflow import keras
from keras import layers
import os
from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
from tensorflow import keras
import json
from PIL import Image

classCount = 10
size = 128
ep = 3

categories = {
    0:'T-shirt_Top',
    1:'Hose',
    2:'Pullover',
    3:'Kleid',
    4:'Mantel',
    5:'Sandalen',
    6:'Hemd',
    7:'Sneaker',
    8:'Tasche',
    9:'Halbschuhe'
}

(trainingImages, trainingLabels), (testingImages, testingLabels)  = fashion_mnist.load_data()

#   1.1.1:

print("Dimension: ")
print(trainingImages.shape)

#   1.2.1:

for i in range(0,100):
    img = Image.fromarray(trainingImages[i])
    real = trainingLabels[i]

    #   1.2.2
    
    path = os.path.join('INFI/Aufgabe6/zalando', categories[real])
    os.makedirs(path, exist_ok=True)
    img.save("%s/%d_%d.jpeg" % (path, i, real))

#   1.1.2:
dir = 'INFI/Aufgabe6/zalando'
tenthPic = ''
for f in os.listdir(dir):
    d = os.path.join(dir, f)
    if os.path.isdir(d):
        if os.path.basename(d) != 'models':
            c = 0
            for subfile in os.listdir(d):
                if os.path.isfile(os.path.join(d, subfile)):
                    c += 1
                    if '10_0.jpeg' in subfile:
                        tenthPic = [os.path.join(d, subfile), os.path.basename(d)]
            print(f'Kategorie: {os.path.basename(d)}\t|\tAnzahl Bilder: {c}')

#   1.1.3:

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return f'{width}*{height}'

print(f'Anzahl an Pixel vom 10. Bild: {get_num_pixels(tenthPic[0])} | Kategorie: {tenthPic[1]}')

trainingImages = trainingImages.astype("float32") / 255
print(trainingImages.shape, "training samples")
testingImages = testingImages.astype("float32") / 255

trainingImages = np.expand_dims(trainingImages, -1)
testingImages = np.expand_dims(testingImages, -1)

print(trainingImages.shape, "trainingImages shape:")
print(trainingImages.shape[0], "number of training samples")
print(testingImages.shape[0], "number of testing samples")

label_count = collections.Counter(trainingLabels)
print(label_count, "Number of labels")

trainingLabels = keras.utils.to_categorical(trainingLabels, classCount)
labels = testingLabels
testingLabels = keras.utils.to_categorical(testingLabels, classCount)

trainingImages = trainingImages.reshape(60000, 784)
testingImages = testingImages.reshape(10000, 784)
trainingImages = trainingImages.astype('float32')
testingImages = testingImages.astype('float32')

#   2.1:

model = keras.Sequential(
    [
        keras.Input(shape=(784,)),
        layers.Dense(16, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(52, activation="relu"),
        layers.Dense(124, activation="relu"),
        layers.Dense(188, activation="relu"),
        layers.Dense(189, activation="relu"),
        layers.Dense(212, activation="relu"),
        layers.Dense(230, activation="relu"),
        layers.Dense(classCount, activation="softmax"),
    ]
)
model.summary()


#   2.2:

model.compile(loss ="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


history = model.fit(trainingImages, trainingLabels, batch_size=size, epochs=ep, validation_split=0.1)
print('history' + str(history.history))

#   3.1:

score = model.evaluate(testingImages, testingLabels, verbose=2)
print(score)


#   3.2:

pred = model.predict(testingImages)
print(pred[1])
pred_1 = np.argmax(pred[1])
print(pred_1)
print(labels[1])
print('highest value')
pred_dic = {
    "prediction" : [],
    "label" : []
}
for i in range(0,100):
    pred_i = np.argmax(pred[i])
    pred_dic["prediction"].append(pred_i)
    print(labels[i], pred_i)
    pred_dic["label"].append(labels[i])
print(pred_dic)


#   3.3:

model.save('INFI/Aufgabe6/zalando/models/model.mdl')
model.save_weights("INFI/Aufgabe6/zalando/models/model.h5")

weights = model.get_weights()
j =json.dumps(pd.Series(weights).to_json(orient='values'), indent=3)

model = keras.models.load_model('INFI/Aufgabe6/zalando/models/model.mdl')
model.load_weights("INFI/Aufgabe6/zalando/models/model.h5")

model_json = model.to_json()
print (model_json)

#   4:

pd.DataFrame(pred_dic).plot(figsize=(8,5))
plt.show()