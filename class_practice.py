import random
import shutil
from fashi_queue import Queue
class Queue:
    def __init__(self):
        self.list = []
    def add(self,item):
        new_list = []
        new_list.append(item)
        for x in self.list:
            new_list.append(x)
        self.list = new_list
    def remove(self):
        output = self.list[0]
        size = len(self.list)
        if size > 1:
            self.list = self.list[1:]
        elif size == 1:
            self.list = []
        else:
            print("theres nothing in there")
        return output
class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        size = len(self.list)
        output = self.list[size-1]
        self.list = self.list[:size-1]
        return output
    def print(self):
        print(self.list)
class State:
    x_player = y_player = x_computer = y_computer = None
    def __init__(self,x_player,y_player,x_computer,y_computer):
        self.x_player = x_player
        self.y_player = y_player
        self.x_computer = x_computer
        self.y_computer = y_computer
    def status(self):   # returns player and computer's positions
        player_position = (self.x_player , self.y_player)
        computer_position = (self.x_computer , self.y_computer)
        return (player_position , computer_position)

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.x_player == other.x_player and self.y_player == other.y_player and self.x_computer == other.x_computer and self.y_computer == other.y_computer

start_position = (2,10)
computer_position = (3,4)
state_1 = State(start_position[0],start_position[1],computer_position[0],computer_position[1])
(x_p,y_p) , (x_c ,y_c ) = state_1.status()
print(state_1.status())
print("===================================")
states_list = []
for i in range (0,100):
    new_state = State(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
    if (new_state in states_list):
        print(new_state.status(), " is already in the list")

    else:
        states_list.append(new_state)
        #print(new_state.status(), " is added")

print(len(states_list))

q = Queue()
state_1 = State(1,1,2,3)
state_2 = State(2,1,2,3)
state_3 = State(3,1,2,3)
state_4 = State(4,1,2,3)

q.add(state_1)
q.add(state_2)
q.add(state_3)
q.add(state_4)

o1 = q.remove()
o2 = q.remove()
o3 = q.remove()
o4 = q.remove()

print(o1.status())
print(o2.status())
print(o3.status())
print(o4.status())






