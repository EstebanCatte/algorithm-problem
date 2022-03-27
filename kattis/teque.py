from collections import deque
import sys

class Teque():

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def rearrange(self):
        if len(self.left) - len(self.right) >= 2:
            self.right.appendleft( self.left.pop())
        elif len(self.right) - len(self.left) >= 2:
            self.left.append(self.right.popleft())

    def push_back(self, x):
        self.right.append(x)
        self.rearrange()

    def push_front(self, x):
        self.left.appendleft(x)
        self.rearrange()

    def get(self, i):
        i = int(i)
        if i >= len(self.left):
            return self.right[i-len(self.left)]
        else:
            return self.left[i]

    def push_middle(self, x):
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
            self.right.appendleft(x)
        else:
            self.left.append(x)
        self.rearrange()

teque = Teque()
sys.stdin.readline()

for command in sys.stdin:
    instruction = command.split(" ")

    if instruction[0] == "push_back":
        teque.push_back(instruction[1])
    if instruction[0] == "push_front":
        teque.push_front(instruction[1])
    if instruction[0] == "push_middle":
        teque.push_middle(instruction[1])

    if instruction[0] == "get":
        sys.stdout.write( teque.get(instruction[1]) )

    #print("teque = {},{}".format(teque.left, teque.right))

