
def isEmpty(q):
    return q == []

def enQueue(q, item):
    q.append(item)
    if len(q) == 1:
        front = rear = 0
    else:
        rear = len(q) - 1

def deQueue(q):
    if isEmpty(q):
        print("Underflow")
        return None
    else:
        item = q.pop(0)
    if len(q) == 0:
        front = read = None
    print("Dequeue-ed item is", item)
    return item

def peek(q):
    if isEmpty(q):
        print("Queue is empty.")
        return "Underflow"
    else:
        front = 0
    print("Frontmost item is", q[front])
    return q[front]

def display(q):
    if isEmpty(q):
        print("Empty Queue")
    elif len(q) == 1:
        print(q[0], "<== front, rear")
    else:
        front = 0
        rear = len(q) - 1
        print(q[front], "<- front")
        for i in range(1, rear):
            print(q[i])
        print(q[rear], '<- rear')


queue = []
front = None
print("\n"*100)
print("QUEUE OPERATIONS")
print("1 = Enqueue")
print("2 = Dequeue")
print("3 = Peek")
print("4 = Display queue")
print("5 = Exit")

def main():
    n = input("\nEnter your choice (1-5): ")

    if n == '1':
        item = input("Enter item: ")
        enQueue(queue, item)
        main()
    
    if n == '2':
        deQueue(queue)
        main()
    
    if n == '3':
        peek(queue)
        main()
    
    if n == '4':
        display(queue)
        main()
    
    if n == '5':
        exit()
    
    else:
        print("Invalid input")
        main()

main()
