#! /usr/bin/env python3

import task
import schedule
from datetime import datetime

import time


def generateTasksCrazy (height):
    layers = []
    for i in range (height):
        layer = []
        for j in range (2**i):
            layer.append(task.Task("Layer {}, Task {}".format(i, j), datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p')))
            if len(layers) > 0:
                for t in layers[-1]:
                    t.add_dependency(layer[-1])
            s.add_task(layer[-1])
        layers.append(layer)

def generateTasksLinear(number):
    taskList = []
    for i in range(number):
        taskList.append(task.Task("Task {}".format(i), datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p')))
        if (len(taskList) > 1):
            taskList[-1].add_dependency(taskList[-2])
        s.add_task(taskList[-1])
        

for i in range(10000):
    s = schedule.Schedule()
    lastTime = time.time()
    generateTasksLinear(i)
    #print ("Layers: {}, Time: {}".format(i, time.time() - lastTime))
    print ("{},{}".format(i, time.time() - lastTime))

