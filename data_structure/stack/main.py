from stacks import Stack

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(f'Pushed 4 items: {stack.items}')

stack.pop()
stack.pop()
print(f'Popped twice: {stack.items}')

print(f'count of items: {stack.size()}')
print(f'Is stack empty: {stack.is_empty()}')
print(f'top item: {stack.peek()}')