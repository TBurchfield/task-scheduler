#!/usr/bin/env python3
import task
import schedule
from datetime import datetime
t = task.Task("Paint house",  datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'))
v = task.Task("Buy paint",  datetime.strptime('Jun 1 2006  1:33PM', '%b %d %Y %I:%M%p'))
t.add_dependency(v)
s = schedule.Schedule()
s.add_task(t)
s.add_task(v)
for task in s.get_task_list():
  print(task.id)