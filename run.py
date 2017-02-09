#!/usr/bin/env python

import List
import network2
import Reader

def Vanilla(layers, trainingData, evaluationData):
    net = network2.Network(layers, cost=network2.CrossEntropyCost)
    net.SGD(trainingData, \
        epochs=300, mini_batch_size=10, eta=0.01, lmbda=.5, \
        evaluation_data=evaluationData, monitor_evaluation_accuracy=True, \
        monitor_training_accuracy=True)

if __name__ == "__main__":
    data = Reader.ReadFolder("testdata")
    print data
    print List.Split(data)
    print List.Collate(List.Split(data))
    # (training, evaluation) = List.Collate(List.Split(data))
    # Vanilla([25, 15, 10, 3], training, evaluation)
