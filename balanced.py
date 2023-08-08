class Stack:
    # Write a program to check whether a given string has balanced parentheses
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)
    
    
def is_balanced(input_string):
    stack = Stack()
    
    for char in input_string:
        print(char)
        if char in ['(', '[', '{']:
            stack.push(char)
            
        if char == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
        if char == ']':
            if stack.is_empty() or stack.pop() != '[':
                return False 
        if char == '}':
            if stack.is_empty() or stack.pop() != '{':
                return False
            
    return stack.is_empty()
            
            
if __name__ == '__main__':
    test_string = '(string[{int256 amount}, {address sender}])'
    if is_balanced(test_string):
        print("Given String is balanced")
    else:
        print("Given String is not balanced")
    