# prerequisites
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def loadData(fileName, inputVarNames, outputVarName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedInputs = [dataNames.index(varName) for varName in inputVarNames]
    inputs = [[float(data[i][selectedInputs[0]]), float(data[i][selectedInputs[1]])] for i in range(len(data))]
    selectedOutput = dataNames.index(outputVarName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputs, outputs

def plotData(x1, x2, y, title=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, x2, y, c='r', marker='o')
    ax.set_xlabel('PIB')
    ax.set_ylabel('Gradul de libertate')
    ax.set_zlabel('Gradul de fericire')
    plt.title(title)
    plt.show()

crtDir =  os.getcwd()
filePath = os.path.join(crtDir, 'data', 'v3_world-happiness-report-2017.csv')

inputs, outputs = loadData(filePath, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')

inputs = np.array(inputs)
# check the liniarity (to check that a linear relationship exists between the dependent variable (y = happiness) and the independent variable (x = capita).)
plotData(inputs[:,0], inputs[:,1], outputs, title='capita GDP and freedom vs. happiness')

# split data into training data (80%) and testing data (20%)
np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace = False)
validationSample = [i for i in indexes  if not i in trainSample]
trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]
validationInputs = [inputs[i] for i in validationSample]
validationOutputs = [outputs[i] for i in validationSample]

# training step
regressor = linear_model.LinearRegression()
regressor.fit(trainInputs, trainOutputs)
w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]

# makes predictions for test data
computedTestOutputs = [w0 + w1 * el[0] + w2 * el[1] for el in validationInputs]

# plot the predictions vs real test data
outputs = np.array(outputs)
validationInputs = np.array(validationInputs)
validationOutputs = np.array(validationOutputs)

plotData(validationInputs[:,0], validationInputs[:,1], validationOutputs, title="predictions vs real test data")

error = 0.0
for t1, t2 in zip(computedTestOutputs, validationOutputs):
    error += (t1 - t2) ** 2
error = error / len(validationOutputs)
print("prediction error (manual): ", error)

# compute the differences between the predictions and real outputs
error = mean_squared_error(validationOutputs, computedTestOutputs)
print("prediction error (tool): ", error)



# media erorilor pătratelor dintre predicțiile făcute de model
# și valorile reale (ground truth) din setul de date de testare.
# w0 reprezintă intercept-ul (ordonata la origine) al dreptei de regresie,
# w1 și w2 reprezintă panta dreptei pentru variabilele independente