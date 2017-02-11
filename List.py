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

def CollatePairs(tupleList):
    # Turns a list of 2-tuples into a 2-tuple of lists.
    output = ([tupleList[0][0]], [tupleList[0][1]])
    for t in tupleList[1:]:
        output[0].append(t[0])
        output[1].append(t[1])
    return output

if __name__ == "__main__":
    print "Tests."
    a = [0, 1, 2, 3, 4]
    print Shuffle(a)
    print a
    print Split(a)
    tupleList = [([0, 1], [1, 2]), ([2, 3], [3, 4]), ([4, 5], [5, 6])]
    print Collate(tupleList)

