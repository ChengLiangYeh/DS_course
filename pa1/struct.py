
class node:
    # this class infor testing
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self
        
    def __repr__(self):
        return 'Node{}'.format(self.value).strip()


class stack:
    def __init__(self):
        self.num_element = 0
        self.root = node(None) #root = head
        self.top = node(None)
        self.dummy = node(None)
        self.forprint = node(None)
        self.a = str()  #####

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
            # TODO:
            # Connect the second last element >> root
            # Connect root >> the second last element 
            self.top = self.top.left
            self.top.right = self.dummy
            self.dummy.left = self.top
            self.num_element -= 1

    def push(self, node):
        # TODO:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        if self.num_element == 0:
            self.root.right = node
            self.forprint.right = node
            node.right = self.dummy
            self.dummy.left = node
            node.left = self.root
            node.left = self.forprint
            self.top = node
            self.top.left = self.root
            self.top.right = self.dummy
            self.num_element += 1
        else:
            new_node = node
            new_node.left = self.top
            new_node.right = self.dummy
            self.dummy.left = new_node
            self.top.right = new_node
            self.top = new_node
            self.num_element += 1

    def printstack(self):
        count = self.num_element 
        while count > 0:
            #print('>>', self.forprint.right, end="") #這行可以print結果

            self.a = '>>' + str(self.forprint.right)  #####存成output.txt
            #print(self.a)                             #####這行test
            self.f = open("output.txt", "a")              #####
            self.f.write(self.a)                           #####

            self.forprint = self.forprint.right
            count -= 1
        #將self.forprint指回self.root
        self.forprint = self.root
        self.forprint.right = self.root.right
        #print('\n')        print時換行!
        self.f.write('\n')  ######
        #self.f.close()     ######不知道怎麼關...放到外面?

    #沒用到
    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret

class queue:
    def __init__(self):
        self.num_element = 0
        self.root = node(None)
        self.rear = node(None)
        self.dummy = node(None)
        self.last = node(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty queue')
        elif self.num_element == 1:
            self.rear = self.rear.right
            self.last = self.last.right
            self.rear.left = self.root
            self.last.left = self.root
            self.num_element -= 1
        else:
            self.rear = self.rear.right
            self.rear.left = self.root
            self.root.right =self.rear
            self.num_element -= 1
            
            # TODO:
            # Connect the second element >> root
            # Connect root >> the second element 
    
    def push(self, node):
        # TODO:
        # Connect the root >> inserted node
        # Connect the inserted node >> first element
        if self.num_element == 0 :
            self.root.right = node
            self.rear.right = node
            self.last.right = node
            node.left = self.root
            node.left = self.last
            node.left = self.rear
            self.last = node
            self.rear = node
            self.last.right = self.dummy
            self.rear.right = self.dummy
            self.dummy.left = self.last
            self.dummy.left = self.rear
            self.num_element += 1
        elif self.num_element == 1:
            new_node = node
            new_node.left = self.last
            new_node.left = self.rear
            self.last.right = new_node
            self.rear.right = new_node
            new_node.right = self.dummy
            self.dummy.left =new_node
            self.last = new_node
            self.num_element += 1
        else:
            new_node = node
            new_node.left = self.last
            self.last.right = new_node
            new_node.right = self.dummy
            self.dummy.left =new_node
            self.last = new_node
            self.num_element += 1

    def printqueue(self):
        count = self.num_element 
        while count > 0:
            #print('>>',self.root.right, end='')

            self.a = '>>' + str(self.root.right)  #####
            self.f = open("output.txt", "a")      #####
            self.f.write(self.a)                  #####

            self.root = self.root.right
            count -= 1
        #將self.root指回self.root原來的位置 = self.rear.left
        self.root = node(None)
        self.root.right = self.rear
        self.rear.left =self.root
        #print('\n')
        self.f.write('\n')    #####

    #沒用到
    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret







#test stack  -> test good
'''
stack = stack()
stack.push(node(1))
stack.push(node(2))
stack.push(node(3))
stack.printstack()
stack.push(node(4))
stack.printstack()
stack.push(node(5))
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.pop()
stack.printstack()
stack.push(node(6))
stack.printstack()
'''
'''
print(stack.root)
print(stack.root.left)
print(stack.root.right)
print(stack.top)
print(stack.top.left)
print(stack.top.right)
#stack.__repr__()
print('-------------------------')
stack.pop()
stack.pop()
stack.pop()
print(stack.root)
print(stack.root.left)
print(stack.root.right)
print(stack.top)
print(stack.top.left)
print(stack.top.right)
print(stack.dummy)
print(stack.dummy.right)
'''

#test Queue
'''
queue = queue()
queue.push(node(10))
queue.printqueue()
queue.push(node(9))
queue.printqueue()
queue.push(node(8))
queue.printqueue()
queue.pop()
queue.printqueue()
queue.pop()
queue.printqueue()
queue.pop()
queue.printqueue()
queue.push(node(6))
queue.printqueue()
queue.push(node(5))
queue.printqueue()
queue.pop()
queue.printqueue()
queue.pop()
queue.printqueue()
'''