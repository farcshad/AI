class stack_structure:

    stack = []
    size = 0

    def push(self,new_data):
        self.stack.append(new_data)

    def pop(self):
        current_size = len(self.stack)
        if(current_size == 0):
            raise Exception("exception")
        else:
            output = self.stack[current_size - 1]
            self.stack = self.stack[:current_size-1]
            return output

stack = stack_structure()
stack.push("hi")
stack.push("fashi")
stack.push("hello")
print(stack.pop())
print(stack.pop())
print(stack.pop())


print(stack_structure.push)
 