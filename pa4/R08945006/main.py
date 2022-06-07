import argparse

class Heap_Node():
    def __init__(self, key):
        self.value = key

    def __repr__(self):
        return 'Heap_Node({})'.format(str(self.value))

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value > other.value:
            return False
        else:
            return True

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def __repr__(self):
        return str(self.heapList)

    def insert(self, node):
        #TODO
        node_value_for_check = node
        #print(node_value_for_check.value)
        node = Heap_Node(node) 
        if (len(self.heapList)) > 2:
            for i in range(1,(len(self.heapList))):
                if node_value_for_check.value == (self.heapList[i]).value:
                    print(node_value_for_check.value,'already in the tree')
                    return
        self.heapList.append(node.value)   #跟在jupyter上寫的唯一不同之處! 
        self.currentSize = len(self.heapList)
        self.currentSize -= 1
        #print(self.currentSize)
        parentSize = int((self.currentSize) / 2) #取floor
        if parentSize == 0:
            parentSize += 1
        #print("起始cur:",self.currentSize)
        #print("起始par:",parentSize)
        while self.currentSize >= 1:
            if (self.heapList[self.currentSize]).value < (self.heapList[parentSize]).value:
                temp = (self.heapList[self.currentSize]).value
                (self.heapList[self.currentSize]).value = (self.heapList[parentSize]).value
                (self.heapList[parentSize]).value = temp
                self.currentSize = int((self.currentSize) / 2)
                parentSize = int((self.currentSize) / 2)
                if parentSize == 0:
                    parentSize += 1
                #print(self.currentSize)
                #print(parentSize)
                #print(minheap)
            else:
                #print(minheap)
                return
                

    def delMin(self):
        #TODO
        tempnode = self.heapList[1].value
        self.heapList[1].value = (self.heapList[len(self.heapList)-1]).value
        (self.heapList[len(self.heapList)-1]).value = tempnode
        delitem = self.heapList.pop()
        
        #調整min heap tree
        #print(self.heapList)    
        
        if len(self.heapList) == 1: #list只剩下零
            #print(delitem)
            return delitem
        
        followed_item = self.heapList[1]
        #print('followed_item=',followed_item)
        cur_loc = self.heapList.index(followed_item)
        #print('cur_loc=',cur_loc)
        
        #算tree level:
        n = (len(self.heapList)-1)
        #print('n=',n)
        level = 0
        while n > 0:
            n = n - 2**(level)
            level += 1
        #print('level=',level)
        
        while level > 1:
            #print('list total長度=',len(self.heapList)-1)
            left_child_loc = cur_loc*2
            #print('left_child_loc=',left_child_loc)
            right_child_loc = cur_loc*2 + 1
            #print('right_child_loc=',right_child_loc)
            if len(self.heapList)-1 > left_child_loc and len(self.heapList)-1 > right_child_loc:
                left_child_value = (self.heapList[(cur_loc)*2]).value
                right_child_value = (self.heapList[(cur_loc)*2 + 1]).value
                if left_child_value > right_child_value and self.heapList[cur_loc].value > right_child_value:
                    for_change_item_loc = (cur_loc)*2 + 1
                elif right_child_value > left_child_value and self.heapList[cur_loc].value > left_child_value:
                    for_change_item_loc = (cur_loc)*2
                else: 
                    for_change_item_loc = cur_loc
                tempnode2 = (self.heapList[cur_loc]).value
                (self.heapList[cur_loc]).value = (self.heapList[for_change_item_loc]).value
                (self.heapList[for_change_item_loc]).value = tempnode2
                cur_loc = for_change_item_loc 
                #print(self.heapList)
                level = level - 1
                #print('level',level)
            elif len(self.heapList)-1 > left_child_loc:
                left_child_value = (self.heapList[(cur_loc)*2]).value
                if self.heapList[cur_loc].value > left_child_value:
                    for_change_item_loc = (cur_loc)*2
                else:
                    for_change_item_loc = cur_loc
                tempnode2 = (self.heapList[cur_loc]).value
                (self.heapList[cur_loc]).value = (self.heapList[for_change_item_loc]).value
                (self.heapList[for_change_item_loc]).value = tempnode2
                cur_loc = for_change_item_loc 
                #print(self.heapList)
                level = level - 1
                #print('level',level)
                
            if level == 2:
                #print('cur_loc=',cur_loc)
                #print('list total長度=',len(self.heapList)-1)
                left_child_loc = cur_loc*2
                #print('left_child_loc=',left_child_loc)
                right_child_loc = cur_loc*2 + 1
                #print('right_child_loc=',right_child_loc)
                
                if left_child_loc <= (len(self.heapList)-1) and right_child_loc <= (len(self.heapList)-1):
                    left_child_value = (self.heapList[(cur_loc)*2]).value
                    right_child_value = (self.heapList[(cur_loc)*2 + 1]).value
                    if left_child_value > right_child_value and self.heapList[cur_loc].value > right_child_value:
                        for_change_item_loc = (cur_loc)*2 + 1
                    elif right_child_value > left_child_value and self.heapList[cur_loc].value > left_child_value:
                        for_change_item_loc = (cur_loc)*2
                    else:
                        for_change_item_loc = cur_loc
                    tempnode2 = (self.heapList[cur_loc]).value
                    (self.heapList[cur_loc]).value = (self.heapList[for_change_item_loc]).value
                    (self.heapList[for_change_item_loc]).value = tempnode2
                    cur_loc = for_change_item_loc 
                    #print(self.heapList)
                    level = level - 1
                    #print('level',level)
                elif left_child_loc <= (len(self.heapList)-1):
                    left_child_value = (self.heapList[(cur_loc)*2]).value
                    if self.heapList[cur_loc].value > left_child_value:
                        for_change_item_loc = (cur_loc)*2
                    else:
                        for_change_item_loc = cur_loc
                    tempnode2 = (self.heapList[cur_loc]).value
                    (self.heapList[cur_loc]).value = (self.heapList[for_change_item_loc]).value
                    (self.heapList[for_change_item_loc]).value = tempnode2
                    cur_loc = for_change_item_loc 
                    #print(self.heapList)
                    level = level - 1
                    #print('level',level)
                else:
                    return delitem
            
        #print(delitem)            
        return delitem

def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    minheap = MinHeap()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'print':
                print(minheap, file=output)
            else:
                operation = line.split(' ')[0]
                if operation.lower() == 'insert':
                    key = int(line.split(' ')[1])
                    minheap.insert(Heap_Node(key))
                elif operation.lower() == 'delmin':
                    print(minheap.delMin(), file=output)
                else:
                    raise NotImplementedError
    output.close()

if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input')
    parser.add_argument('--output', default='./output')
    args = parser.parse_args()

    main(args.input, args.output)


