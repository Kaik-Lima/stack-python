# Simple Implementation

def create_stack(capacity):
    return [], capacity


def is_empty(stack):
    return len(stack) == 0


def is_full(stack):
    global capacity
    return len(stack) == capacity


def push(stack, element):
    if not is_full(stack):
        stack.apprend(element)
    else:
        print('Error: Stack is full')


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print('ERROR! Stack is empty')


def peek(stack):
    if not is_empty:
        return stack(-1)
    else:
        print('ERROR! Stack is empty')
        return None


# Test Implementation

stack, capacity = create_stack(5)

print('Push elements at stack')
for i in range(capacity):
    push(stack, i)

print(stack)    # stack = [0, 1, 2, 3, 4]
print('\nIs stack Full?', is_full(stack))   # True

print('\nDelete elements at stack')
for _ in range(capacity):
    print(pop(stack), end=' ')

print('\n\nIs stack empty?', is_empty(stack))   # True
