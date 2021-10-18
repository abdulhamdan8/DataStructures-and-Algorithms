stack = []


def push():
    element = input("enter ele\n");
    stack.append(element)
    print(f'stack after push {stack}')


def pop_ele():
    if not stack:
        print("stack empty")
    else:
        stack.pop()
        print(f'stack after pop {stack}')


while True:
    x = int(input("select numbers to operate 1:push,2:pop,3:stop\n"))
    if x == 1:
        push()
    elif x == 2:
        pop_ele()
    elif x == 3:
        break

