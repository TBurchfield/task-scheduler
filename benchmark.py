#! /usr/bin/env python3

import task
import schedule
from datetime import datetime

s = schedule.Schedule()

def generateTasks (height):
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

generateTasks(3)

for task in s.get_task_list():
    print(task.id)
