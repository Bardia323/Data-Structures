# Here is a universally applicable queue data structure in python.
# Queues store items in the order in which they were added.
#
# - ticket lines at movie theaters
# - printers in a lab
# - event-driven systems
# - simulation
# - web client requests
# - web server requests
# - OS processes

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print queue.pop(0)
print queue.pop(0)
print queue.pop(0)

# Here is a universally applicable stack data structure in python.
# Stacks store items in the order in which they were added,
# but you can remove items from any position.
#
# - undo/redo
# - web browser back/forward
# - HTML <head> <title> <body>
# - OS file system

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
