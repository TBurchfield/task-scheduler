# Defines the Task class, should not be executed directly.
class Task:
  def __init__(self, tid, dd):
    self.dependencies = []
    self.due_date = dd
    self.id = tid

  def get_dependencies(self):
    return self.dependencies

  def get_due_date(self):
   return self.due_date

  def add_dependency(self, task):
    self.dependencies.append(task)
    self.dependencies.sort(key=lambda task: task.get_due_date())
