stack = []
max_size = 10

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    if not isFull(stack):
        stack.append(item)

def pop(stack):
    if not isEmpty(stack):
        return stack.pop()

