# Defines the Schedule class, should not be executed directly.
class Schedule:
  def __init__(self):
    pass

  def add_task(self, task):
    pass

  def remove_task(self, name):
    pass

  # Returns the optimal ordering of tasks
  def get_task_list(self):
    # Task ids that have been sorted
    done = set()
    fully_sorted_tasks = []
    self.tasks.sort(key=lambda task: task.get_due_date())
    i = 0
    while i < len(self.tasks):
      if self.tasks[i] in done:
        continue
      sorted_component = order_component(done, self.tasks[i])
      fully_sorted_tasks.extend(sorted_component)
      i += 1

  def save_schedule(self, filename):
    pass

  def load_schedule(self, filename):
    pass

def order_component(done, task):
  def order_component_r(task):
    if task in done:
      return
    seen.add(task)
    done.add(task)
    # Assumes get_dependencies() returns a list sorted by due date
    for child in task.get_dependencies():
      if child not in seen:
        order_component_r(child)
      else:
        raise AssertionError('This schedule has circular dependencies!')
    # We can be guaranteed tasks' time is after due_date, otherwise it would have been in done
    sorted_component.append(task)
  sorted_component = []
  # Seen is used to detect cycles
  seen = set()
  order_component_r(task)
  return sorted_component[::-1]
