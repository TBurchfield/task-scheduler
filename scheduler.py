#!/usr/bin/env python3
# A command line interface to use the schedule and task modules.

import sys
import schedule
import task

# Function
def usage(exit_code=0):
	print(''' Usage: scheduler.py add_task taskname  due_date
	scheduler.py remove_task taskname
	scheduler.py get_task_list
	scheduler.py add_dependency d1 d2
	
	Note: taskname must be unique
	''')
	sys.exit(exit_code)

# Main Execution

if __name__ == '__main__':
	
	# Parse command line arguments
	args = sys.argv[1:]
	while args and len(args[0]) > 1:
		arg = args.pop(0)
		if arg == '-h':
			usage(0)		
		if sys.argv[2] == 'add_task':
			taskname = args.pop(1)
			due_date = args.pop(0)
			add_task(taskname)
		elif sys.argv[2] == 'remove_task':
			taskname = args.pop(0)
			remove_task(taskname)
		elif sys.argv[2] == 'get_task_list':
			get_task_list()
		elif sys.argv[2] == 'add_dependency':
			d1 = args.pop(1)
			d2 = args.pop(2)
			add_dependency(d1, d2)		# not sure about this one bc in task.py add_dependcy take 1arg
		else:
			usage(1)
		
