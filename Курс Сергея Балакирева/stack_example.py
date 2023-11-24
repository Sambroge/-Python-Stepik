class Queue:
    __first_link = None
    
    def __init__(self, number, link=None):
        self.number = number
        self.previous_link = link if link else self
        if not Queue.__first_link:
            self.change_link(self)
            
    @classmethod        
    def change_link(cls, link):
        cls.__first_link = link
    
    def add(self, number):
        next_number = Queue(number, self)
        if not Queue.__first_link.number:
            self.change_link(next_number)
            next_number.previous_link = None
        else:
            self.next_link = next_number
        return next_number
    
    def pop(self):
        print(Queue.__first_link.number)
        if self != Queue.__first_link:
            self.change_link(Queue.__first_link.next_link)
        elif self.number is not None and self.previous_link == None:
            self.number = None
        Queue.__first_link.previous_link = None
        return self
    
    def head(self):
        print(Queue.__first_link.number)
        return self
    
    def close(self):
        exit(0)

    
command, *number = input().split()
stack = Queue(None)
while True:
    stack = eval(f'Queue.{command}(stack, {number[0]})') if number else eval(f'Queue.{command}(stack)')
    command, *number = input().split()
