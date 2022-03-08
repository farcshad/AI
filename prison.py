

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
    def size(self):
        return len(self.list)
class Stack:
    def __init__(self):
        self.list = []
    def add(self,item):
        self.list.append(item)
    def remove(self):
        size = len(self.list)
        output = self.list[size-1]
        self.list = self.list[:size-1]
        return output
    def size(self):
        return len(self.list)
    def print(self):
        print(self.list)
class State:
    x_player = y_player = x_computer = y_computer = mother_state = None
    def __init__(self,x_player,y_player,x_computer,y_computer,mother_state):
        self.x_player = x_player
        self.y_player = y_player
        self.x_computer = x_computer
        self.y_computer = y_computer
        self.mother_state = mother_state
    def status(self):   # returns player and computer's positions
        player_position = (self.x_player , self.y_player)
        computer_position = (self.x_computer , self.y_computer)
        return (player_position , computer_position)
    def get_mother_state(self):
        return self.mother_state

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.x_player == other.x_player and self.y_player == other.y_player and self.x_computer == other.x_computer and self.y_computer == other.y_computer
class Structure:
    def __init__(self,rows,cols,walls):
        self.rows = rows
        self.cols = cols
        self.walls = walls


#returns True if we are in a final state such as cop reaching to player or player being in the final state
def check_lose(state):
    if (state.x_player == state.x_computer and state.y_player == state.y_computer):
        return True
    else :
        return False
def is_final(state,x_final,y_final):
    if not (state.x_player == state.x_computer and state.y_player == state.y_computer):
        if (state.x_player == x_final and state.y_player == y_final):
            return True
        else:
            return False
    else :
        return False
def is_possible_for_player(state, action, structure):
    x = state.x_player
    y = state.y_player
    walls = structure.walls
    rows = structure.rows
    cols = structure.cols

    if x > 0 and x < cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == 0:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
def is_possible_for_computer(state, action, structure):
    x = state.x_computer
    y = state.y_computer
    walls = structure.walls
    rows = structure.rows
    cols = structure.cols

    if x > 0 and x < cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == 0:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
def player_move(state,action):
    new_state = None
    if action == 'r':
        new_state = State(state.x_player+1,state.y_player,state.x_computer,state.y_computer,state)
    if action == 'l':
        new_state = State(state.x_player-1,state.y_player,state.x_computer,state.y_computer,state)
    if action == 'u':
        new_state = State(state.x_player,state.y_player+1,state.x_computer,state.y_computer,state)
    if action == 'd':
        new_state = State(state.x_player,state.y_player-1,state.x_computer,state.y_computer,state)
    return new_state
def computer_move(state,structure):
    x_player = state.x_player
    y_player = state.y_player
    x_computer = state.x_computer
    y_computer = state.y_computer

    if x_player > x_computer:
        if is_possible_for_computer(state,'r',structure):
            x_computer += 1
        else:
            if y_player > y_computer:
                if is_possible_for_computer(state,'u',structure):
                    y_computer += 1
            elif y_player < y_computer:
                if is_possible_for_computer(state,'d',structure):
                    y_computer += -1

    elif x_player < x_computer:
        if is_possible_for_computer(state,'l',structure):
            x_computer += -1
        else:
            if y_player > y_computer:
                if is_possible_for_computer(state,'u',structure):
                    y_computer += 1
            elif y_player < y_computer:
                if is_possible_for_computer(state,'d',structure):
                    y_computer += -1
    else:
        if y_player > y_computer:
            if is_possible_for_computer(state, 'u', structure):
                y_computer += 1
        elif y_player < y_computer:
            if is_possible_for_computer(state, 'd', structure):
                y_computer += -1

    new_state = State(x_player,y_player,x_computer,y_computer,state.mother_state)
    return new_state
def print_path(state):
    have_not_reached_origin = True
    current_state = state
    length = 1
    while have_not_reached_origin:
        print(current_state.status())
        if (current_state.mother_state == None):
            have_not_reached_origin = False
        else :
            current_state = current_state.mother_state
            length +=1
    print(length)

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
    def size(self):
        return len(self.list)
class Stack:
    def __init__(self):
        self.list = []
    def add(self,item):
        self.list.append(item)
    def remove(self):
        size = len(self.list)
        output = self.list[size-1]
        self.list = self.list[:size-1]
        return output
    def size(self):
        return len(self.list)
    def print(self):
        print(self.list)
class State:
    x_player = y_player = x_computer = y_computer = mother_state = None
    def __init__(self,x_player,y_player,x_computer,y_computer,mother_state):
        self.x_player = x_player
        self.y_player = y_player
        self.x_computer = x_computer
        self.y_computer = y_computer
        self.mother_state = mother_state
    def status(self):   # returns player and computer's positions
        player_position = (self.x_player , self.y_player)
        computer_position = (self.x_computer , self.y_computer)
        return (player_position , computer_position)
    def get_mother_state(self):
        return self.mother_state

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.x_player == other.x_player and self.y_player == other.y_player and self.x_computer == other.x_computer and self.y_computer == other.y_computer
class Structure:
    def __init__(self,rows,cols,walls):
        self.rows = rows
        self.cols = cols
        self.walls = walls


#returns True if we are in a final state such as cop reaching to player or player being in the final state
def check_lose(state):
    if (state.x_player == state.x_computer and state.y_player == state.y_computer):
        return True
    else :
        return False
def is_final(state,x_final,y_final):
    if not (state.x_player == state.x_computer and state.y_player == state.y_computer):
        if (state.x_player == x_final and state.y_player == y_final):
            return True
        else:
            return False
    else :
        return False
def is_possible_for_player(state, action, structure):
    x = state.x_player
    y = state.y_player
    walls = structure.walls
    rows = structure.rows
    cols = structure.cols

    if x > 0 and x < cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == 0:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
def is_possible_for_computer(state, action, structure):
    x = state.x_computer
    y = state.y_computer
    walls = structure.walls
    rows = structure.rows
    cols = structure.cols

    if x > 0 and x < cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == 0:
        if y > 0 and y < rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                wallcheck = [x, y, x + 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'l':
                return False
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True

    if x == cols - 1:
        if y > 0 and y < rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
        if y == 0:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                wallcheck = [x, y, x, y + 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'd':
                return False
        if y == rows - 1:
            if action == 'r':
                return False
            if action == 'l':
                wallcheck = [x, y, x - 1, y]
                if wallcheck in walls:
                    return False
                else:
                    return True
            if action == 'u':
                return False
            if action == 'd':
                wallcheck = [x, y, x, y - 1]
                if wallcheck in walls:
                    return False
                else:
                    return True
def player_move(state,action):
    new_state = None
    if action == 'r':
        new_state = State(state.x_player+1,state.y_player,state.x_computer,state.y_computer,state)
    if action == 'l':
        new_state = State(state.x_player-1,state.y_player,state.x_computer,state.y_computer,state)
    if action == 'u':
        new_state = State(state.x_player,state.y_player+1,state.x_computer,state.y_computer,state)
    if action == 'd':
        new_state = State(state.x_player,state.y_player-1,state.x_computer,state.y_computer,state)
    return new_state
def computer_move(state,structure):
    x_player = state.x_player
    y_player = state.y_player
    x_computer = state.x_computer
    y_computer = state.y_computer

    if x_player > x_computer:
        if is_possible_for_computer(state,'r',structure):
            x_computer += 1
        else:
            if y_player > y_computer:
                if is_possible_for_computer(state,'u',structure):
                    y_computer += 1
            elif y_player < y_computer:
                if is_possible_for_computer(state,'d',structure):
                    y_computer += -1

    elif x_player < x_computer:
        if is_possible_for_computer(state,'l',structure):
            x_computer += -1
        else:
            if y_player > y_computer:
                if is_possible_for_computer(state,'u',structure):
                    y_computer += 1
            elif y_player < y_computer:
                if is_possible_for_computer(state,'d',structure):
                    y_computer += -1
    else:
        if y_player > y_computer:
            if is_possible_for_computer(state, 'u', structure):
                y_computer += 1
        elif y_player < y_computer:
            if is_possible_for_computer(state, 'd', structure):
                y_computer += -1

    new_state = State(x_player,y_player,x_computer,y_computer,state.mother_state)
    return new_state
def print_path(state):
    have_not_reached_origin = True
    current_state = state
    length = 1
    while have_not_reached_origin:
        print(current_state.status())
        if (current_state.mother_state == None):
            have_not_reached_origin = False
        else :
            current_state = current_state.mother_state
            length +=1
    print(length)
#rows = 4
#cols = 4
#
#walls = [
    #[0,1,1,1],[1,1,2,1],[1,1,1,2],[2,1,3,1],[3,1,3,2],[0,2,1,2]
#]

rows = 8
cols = 8

walls = [
    [4,0,5,0],[4,0,4,1],[2,1,3,1],[5,1,6,1],[6,0,6,1],[7,0,7,1],[3,1,3,2],[4,1,4,2],[0,2,1,2],[2,2,3,2],[1,2,1,3],
    [3,2,3,3],[6,2,6,3],[7,2,7,3],[1,3,2,3],[2,3,3,3],[3,3,4,3],[4,3,4,4],[1,4,2,4],[2,4,2,5],
    [0,5,1,5],[1,5,2,5],[5,5,6,5],[0,6,1,6],[1,6,2,6],[2,6,3,6],[5,6,6,6],[2,6,2,7],[3,6,3,7],[5,6,5,7],[7,6,7,7],
    [0,7,1,7],[4,7,5,7]
]



for i in range (0,len(walls)):
    x = walls[i]
    y = [x[2],x[3],x[0],x[1]]
    if not(y in walls):
        walls.append(y)

structure = Structure(rows,cols,walls)

player_start_position = (2,5)
computer_start_position = (6,5)
final_position = (7,7)
x_final = final_position[0]
y_final = final_position[1]


start_state = State(player_start_position[0],player_start_position[1],computer_start_position[0],computer_start_position[1],None)
states_to_check = Queue()
states_to_check.add(start_state)

explored_states = []
have_not_reached_there = True
final_state = None
while (states_to_check.size() > 0 and have_not_reached_there):
    current_state = states_to_check.remove()
    if current_state in explored_states:
        pass
    elif check_lose(current_state):
        pass
    elif is_final(current_state,x_final,y_final):
        final_state = current_state
        break

    else:
        explored_states.append(current_state)
        for action in ['r','l','u','d']:
            if is_possible_for_player(current_state,action,structure):
                new_state = player_move(current_state,action)
                new_state = computer_move(new_state,structure)
                new_state = computer_move(new_state,structure)
                states_to_check.add(new_state)

#
#print(final_state.status())
if final_state == None :
    print("NOT POSSIBLE")
else:
    print_path(final_state)
    print(len(explored_states))

#rows = 4
#cols = 4
#
#walls = [
    #[0,1,1,1],[1,1,2,1],[1,1,1,2],[2,1,3,1],[3,1,3,2],[0,2,1,2]
#]

rows = 8
cols = 8

walls = [
    [4,0,5,0],[4,0,4,1],[2,1,3,1],[5,1,6,1],[6,0,6,1],[7,0,7,1],[3,1,3,2],[4,1,4,2],[0,2,1,2],[2,2,3,2],[1,2,1,3],
    [3,2,3,3],[6,2,6,3],[7,2,7,3],[1,3,2,3],[2,3,3,3],[3,3,4,3],[4,3,4,4],[1,4,2,4],[2,4,2,5],
    [0,5,1,5],[1,5,2,5],[5,5,6,5],[0,6,1,6],[1,6,2,6],[2,6,3,6],[5,6,6,6],[2,6,2,7],[3,6,3,7],[5,6,5,7],[7,6,7,7],
    [0,7,1,7],[4,7,5,7]
]



for i in range (0,len(walls)):
    x = walls[i]
    y = [x[2],x[3],x[0],x[1]]
    if not(y in walls):
        walls.append(y)

structure = Structure(rows,cols,walls)

player_start_position = (2,5)
computer_start_position = (6,5)
final_position = (7,7)
x_final = final_position[0]
y_final = final_position[1]


start_state = State(player_start_position[0],player_start_position[1],computer_start_position[0],computer_start_position[1],None)
states_to_check = Queue()
states_to_check.add(start_state)

explored_states = []
have_not_reached_there = True
final_state = None
while (states_to_check.size() > 0 and have_not_reached_there):
    current_state = states_to_check.remove()
    if current_state in explored_states:
        pass
    elif check_lose(current_state):
        pass
    elif is_final(current_state,x_final,y_final):
        final_state = current_state
        break

    else:
        explored_states.append(current_state)
        for action in ['r','l','u','d']:
            if is_possible_for_player(current_state,action,structure):
                new_state = player_move(current_state,action)
                new_state = computer_move(new_state,structure)
                new_state = computer_move(new_state,structure)
                states_to_check.add(new_state)

#
#print(final_state.status())
if final_state == None :
    print("NOT POSSIBLE")
else:
    print_path(final_state)
    print(len(explored_states))
