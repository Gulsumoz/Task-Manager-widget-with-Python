# classes
class Tasks:

    def __init__(self):
        # sample data for testing
        self.tasks = ["shopping", "cooking", "homework"]

    def add_new_task(self, new_task):
        self.tasks.append(new_task)


    def delete_task_name(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("{} has been removed from the to do list.".format(task))
        else:
            print("That task is not in on your to do list.")

    def delete_task_number(self, task_number):
        if self.tasks[task_number] in self.tasks:
            self.tasks.remove(self.tasks[task_number])
        else:
            print("This task number is not on your to do list.")

    def delete_all_tasks(self):
        for _ in self.tasks:
            self.tasks.remove(_)


    def reset_tasks(self, response):
        if response:
            self.tasks = []
        else:
            pass

    def print_tasks(self):
        for _ in range(0, len(self.tasks)):
            print(_, '|', self.tasks[_])

