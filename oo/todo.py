from datetime import datetime


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description):
        self.tasks.append(ToDo(description))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def find(self, description):
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())}) task pending'


class ToDo:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.createdAt = datetime.now()

    def conclude(self):
        self.done = True

    def __str__(self):
        return self.description + ('(Concluída)' if self.done is True else '')


def main():
    house = Project('tasks from home')
    house.add('cleaning the house')
    house.add('washing dishes')
    print(house)

    house.find('washing dishes').conclude()
    for h in house:
        print(h)


if __name__ == '__main__':
    main()
