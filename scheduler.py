#!/usr/bin/env python3
# A command line interface to use the schedule and task modules.

import sys
import schedule
import task

# Function
def usage(exit_code=0):
	print(''' Usage: scheduler.py add_task(taskname, due_date)
	scheduler.py remove_task(taskname, due_date)
	scheudler.py get_task_list
	
	Note: taskname must be unique
	''')
	sys.exit(exit_code)

# Main Execution

if __name__ == '__main__':
	
	# Parse command line arguments
	args = sys.argv[1:]
	while args and len(args[0]) > 1:
		arg = args.pop(0)
		# take care of add_task, remove_task, get_task_list
		if arg == '-h':
			usage(0)
		else:
			usage(1)
		
