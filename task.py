# Defines the Task class, should not be executed directly.
class Task:
  def __init__(self):
    self.dependencies = []
    self.due_date = None

  def get_dependencies(self, task):
    return self.dependencies

  def get_due_date(self, task):
   return self.due_date
