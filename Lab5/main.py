import csv
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

rows = []
realOutputs = []
computedOutputs = []
weight = []
waist = []
pulse = []
predictedWeight = []
predictedWaist = []
predictedPulse = []

def evalClassificationV1(realLabels, computedLabels, labelNames):
    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)
    return acc, precision, recall

def flowers():
    with open("flowers.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            realOutputs.append(row[0])
            computedOutputs.append(row[1])
    acc, prec, recall = evalClassificationV1(realOutputs, computedOutputs, ['Daisy', 'Tulip','Rose'])
    print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)

def sport():
    with open("sport.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            weight.append(row[0])
            waist.append(row[1])
            pulse.append(row[2])
            predictedWeight.append(row[3])
            predictedWaist.append(row[4])
            predictedPulse.append(row[5])

    weight1 = [eval(i) for i in weight]
    predictedWeight1 = [eval(i) for i in predictedWeight]
    waist1 = [eval(i) for i in waist]
    predictedWaist1 = [eval(i) for i in predictedWaist]
    pulse1 = [eval(i) for i in pulse]
    predictedPulse1 = [eval(i) for i in predictedPulse]
    errorL1 = sum(abs(r - c) for r, c in zip(weight1,predictedWeight1)) / len(weight1)
    print('Error (L1_1) MAE: ', errorL1)
    errorL2 = sum(abs(r - c) for r, c in zip(waist1,predictedWaist1)) / len(waist1)
    print('Error (L1_2) MAE: ', errorL2)
    errorL3 = sum(abs(r - c) for r, c in zip(pulse1,predictedPulse1)) / len(pulse1)
    print('Error (L3_1) MAE: ', errorL3)

sport()
flowers()

#diferența medie absolută între valorile prezise și valorile reale