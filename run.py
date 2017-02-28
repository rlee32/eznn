#!/usr/bin/env python

import List
import network2
import Reader
import numpy

def list2vec(x):
    # this converts a list to a vector that the neural network code likes.
    return numpy.array([x]).transpose()


def listset2vectorset(listset):
    # takes in a list of (feature, result) tuples.
    # turns the feature/result list into feature/result ndarrays of size (n,1).
    # Note that the outputs are not vectors of size (n,)
    return [(list2vec(x), list2vec(y)) for x, y in listset]

def Vanilla(layers, trainingData, evaluationData):
    net = network2.Network(layers, cost=network2.CrossEntropyCost)
    net.SGD(trainingData, \
        epochs=300, mini_batch_size=len(trainingData), eta=0.01, lmbda=.5, \
        evaluation_data=evaluationData, monitor_evaluation_accuracy=True, \
        monitor_training_accuracy=True)

if __name__ == "__main__":
    data = Reader.ReadVectorSet("../stocksim/nn/pre/amdvec.csv")
    (training, evaluation) = List.Split(data)
    Vanilla([6, 4, 2, 1], \
        listset2vectorset(training), listset2vectorset(evaluation))
