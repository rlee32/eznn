#!/usr/bin/env python

import random

def Shuffle(data):
    copy = data[:]
    random.shuffle(copy)
    return copy

def Split(data, boundary=0.5):
    # splits list into 2 halves; boundary is in [0,1]
    i = int(boundary * len(data))
    return (data[:i], data[i:])

def Collate(tupleList):
    # Turns a list of tuple of elements into a tuple of a list of elements.
    elements = len(tupleList[0])
    output = []
    for element in tupleList[0]:
        output.append([element])
    for t in tupleList[1:]:
        for i in range(elements):
            output[i].append(t[i])
    return output

if __name__ == "__main__":
    print "Tests."
    a = [0, 1, 2, 3, 4]
    print Shuffle(a)
    print a
    print Split(a)
    tupleList = [([0, 1], [1, 2]), ([2, 3], [3, 4]), ([4, 5], [5, 6])]
    print Collate(tupleList)

