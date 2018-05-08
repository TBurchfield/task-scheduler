# Defines the Schedule class, should not be executed directly.
import pickle

class Schedule:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, name):
    ids = [ t.id for t in self.tasks ]
    del self.tasks[ids.index(name)]

  # Returns the optimal ordering of tasks
  def get_task_list(self):
    # Task ids that have been sorted
    done = set()
    fully_sorted_tasks = []
    self.tasks.sort(key=lambda task: task.get_due_date())
    i = 0
    while i < len(self.tasks):
      if self.tasks[i].id in done:
        i += 1
        continue
      sorted_component = order_component(done, self.tasks[i])
      fully_sorted_tasks.extend(sorted_component)
      i += 1
    return fully_sorted_tasks

  def save_schedule(self, filename):
    # open a file, where you want to store the data
    file = open(filename,'wb')

    # dump info to that file
    pickle.dump(self, file)

    # close file
    file.close()

  def load_schedule(self, filename):
    # open file, where we stored the pickled data
    file = open(filename, 'rb')

    # dump info to that file
    self = pickle.load(file)

    # close the file
    file.close()

def order_component(done, task):
  def order_component_r(task):
    if task.id in done:
      return
    seen.add(task.id)
    done.add(task.id)
    # Assumes get_dependencies() returns a list sorted by due date
    for child in task.get_dependencies():
      if child.id not in seen:
        order_component_r(child)
      else:
        raise AssertionError('This schedule has circular dependencies!')
    # We can be guaranteed tasks' time is after due_date, otherwise it would have been in done
    sorted_component.append(task)
  sorted_component = []
  # Seen is used to detect cycles
  seen = set()
  order_component_r(task)
  return sorted_component
