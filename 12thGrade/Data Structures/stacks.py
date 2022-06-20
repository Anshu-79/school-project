def isEmpty(stk):
    return stk == []

def push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if isEmpty(stk):
        print("Underflow! Stack is empty.")
        return None
    else:
        item = stk.pop()
        if isEmpty(stk):
            top = None
        else:
            top = len(stk) - 1
        print("Popped item is ", item)
        return item

def peek(stk):
    if isEmpty(stk):
        print("Empty queue")
        return "Underflow"
    else:
        top = len(stk) - 1
        print("Topmost item is", stk[top])
        return stk[top]
    
def display(stk):
    if isEmpty(stk):
        print("Empty stack")
    else:
        top = len(stk) - 1
        print(stk[top], "<- top")
        for i in range(top-1, -1, -1):
            print(stk[i])


stack = []
top = None
print("\n"*100)
print("1 = Push")
print("2 = Pop")
print("3 = Peek")
print("4 = Display Stack")
print("5 = Exit")

def main():
    n = input("\nEnter your choice (1-5): ")

    if n == '1':
        item = input("Enter item: ")
        push(stack, item)
        main()
    
    elif n == '2':
        pop(stack)
        main()
    
    elif n == '3':
        peek(stack)
        main()

    elif n == '4':
        display(stack)
        main()

    elif n == '5':
        exit()
    
    else:
        print("Invalid input")
        main()

main()