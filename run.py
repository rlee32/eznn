#!/usr/bin/env python

import List
import network2
import Reader
import numpy

def listset2vectorset(listset):
    return [numpy.reshape(x, (len(x), 1)) for x in listset]

def Vanilla(layers, trainingData, evaluationData):
    net = network2.Network(layers, cost=network2.CrossEntropyCost)
    net.SGD(trainingData, \
        epochs=300, mini_batch_size=10, eta=0.01, lmbda=.5, \
        evaluation_data=evaluationData, monitor_evaluation_accuracy=True, \
        monitor_training_accuracy=True)

if __name__ == "__main__":
    data = Reader.ReadFolder("testdata")
    print data
    data.append(data)
    (training, evaluation) = List.Split(data)
    print training
    print listset2vectorset(training)
    Vanilla([25, 15, 10, 3], \
        listset2vectorset(training), listset2vectorset(evaluation))
