class Queue:
    list = None
    def __init__(self):
        self.list = []

    def push(self,item):
        new_list = [item]
        for x in self.list:
            new_list.append(x)
        self.list = new_list
    def pop(self):
        output = self.list[0]
        self.list = self.list[1:]
    def print(self):
        print(self.list)
