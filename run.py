#!/usr/bin/env python

import List
import network2
import Reader
import numpy

def listset2vectorset(listset):
    # takes in a list of (feature, result) tuples.
    # turns the feature/result list into feature/result ndarrays of size (n,1).
    # Note that the outputs are not vectors of size (n,)
    return [( \
            numpy.array([x]).transpose(), numpy.array([y]).transpose() \
            ) for x, y in listset]
    # return [numpy.reshape(x, (len(x), 1)) for x in listset]

def Vanilla(layers, trainingData, evaluationData):
    net = network2.Network(layers, cost=network2.CrossEntropyCost)
    net.SGD(trainingData, \
        epochs=300, mini_batch_size=len(trainingData), eta=0.01, lmbda=.5, \
        evaluation_data=evaluationData, monitor_evaluation_accuracy=True, \
        monitor_training_accuracy=True)

if __name__ == "__main__":
    data = Reader.ReadFolder("testdata")
    data += data
    (training, evaluation) = List.Split(data)
    print training
    print (listset2vectorset(training)[0][0]).shape
    Vanilla([3, 1], \
        listset2vectorset(training), listset2vectorset(evaluation))
    # Vanilla([3, 2, 1], training, evaluation)
