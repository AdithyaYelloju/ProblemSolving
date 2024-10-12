# Queue using Stacks - Aviso
# Stack class
#Push and Pop
# Int data type


class Stack:
  
    def __init__(self) -> None:
        self.stack = []

    def push(self, element:int) -> None:
        self.stack.append(element)
   
    def pop(self) -> int:
        if(len(self.stack) == 0):
            return -1
            raise Exception("Seom")
          
        element = self.stack.pop()
        return element
   
    def print_stack(self):
        print(self.stack)




'''stack = Stack()
stack.push(1)
stack.print_stack()
stack.push(2)
stack.push(3)
stack.print_stack()
stack.pop()
stack.pop()
stack.pop()
stack.print_stack()
stack.pop()'''


# Queue, using Stack
# Enque and Deque
# Data Store class


class Queue:

    def __init__(self) -> None:
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, element: int) -> None:
        self.s1.push(element=element)
        #self.s1.print_stack()

    def deque(self) -> int:
        is_stack_not_empty = True
        #print("Poping S1")
        while(is_stack_not_empty):
            element = self.s1.pop()
            #print(element)
            if(element == -1):
                is_stack_not_empty = False
            else:
                self.s2.push(element)

        res = self.s2.pop()

        is_stack_not_empty = True
        while(is_stack_not_empty):
            element = self.s2.pop()
            if(element == -1):
                is_stack_not_empty = False
            else:
                self.s1.push(element)

        return res


    def print_queue(self):
        self.s1.print_stack()
               


queue = Queue()
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.print_queue()
print(queue.deque())
queue.print_queue()
