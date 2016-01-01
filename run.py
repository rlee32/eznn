#!/usr/bin/python

import reader
training_data, validation_data, test_data = \
  reader.get_neural_network_data("../vault")

import network2
net = network2.Network([25, 15, 10, 3], cost=network2.CrossEntropyCost)
net.SGD(training_data, \
  epochs=300, mini_batch_size=10, eta=0.01, lmbda=.5, \
  evaluation_data=validation_data, monitor_evaluation_accuracy=True, \
  monitor_training_accuracy=True)

