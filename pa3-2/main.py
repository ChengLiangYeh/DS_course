import argparse

class BSTree_Node():
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BSTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        # TODO
        if self.root == None:
            self.root = BSTree_Node(key)
        else:
            self._insert(key, self.root)
    
    def _insert(self, key, cur_node):
        if key < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = BSTree_Node(key)
            else:
                self._insert(key, cur_node.left_child)
        elif key > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = BSTree_Node(key)
            else:
                self._insert(key, cur_node.right_child)
        else:
            print('key is aleady in BST!')
    
    def find(self, key):
            if self.root != None:
                parent = None
                return self._find(key, self.root, parent)

    def _find(self, key, cur_node, parent):
        if key == cur_node.value:
            return cur_node, parent
        elif key < cur_node.value and cur_node.left_child != None:
            parent = cur_node
            return self._find(key, cur_node.left_child, parent)
        elif key > cur_node.value and cur_node.right_child != None:
            parent = cur_node
            return self._find(key, cur_node.right_child, parent)
        else:
            return None, None
        
###############################################################################################
        
    def delete(self, key):
        key, parent = self.find(key)
        return self.delete_node(key, parent)
    
    def delete_node(self, node, parent):
        def minvalue_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children
        
        ##
        if node == None and parent == None:
            return
        ##
        
        node_parent = parent
        #print(node_parent)
        node_children = num_children(node)

        if node_children == 0 :
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None
        
        if node_children == 1 :
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child
            
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent = node_parent
        
        if node_children == 2:
            #print(node, node_parent)
            rsubtree_min = minvalue_node(node.right_child)
            #print(rsubtree_min)
            temp = rsubtree_min.value
            self.delete(rsubtree_min.value)
            node.value = temp



            
    def inorder(self, output):
        if self.root != None:
            self._inorder(self.root)
            with open('output', 'a') as f:
                f.write('\n')
            
    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left_child)
            #print( cur_node.value )
            with open('output', 'a') as f:
                f.write(str(cur_node.value))
                f.write(' ')
            self._inorder(cur_node.right_child)


    def inorder(self, output):
        if self.root != None:
            self._inorder(self.root)
            with open('output', 'a') as f:
                f.write('\n')
            
    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left_child)
            #print( cur_node.value )
            with open('output', 'a') as f:
                f.write(str(cur_node.value))
                f.write(' ')
            self._inorder(cur_node.right_child)

            
    def preorder(self, output):
        if self.root != None:
            self._preorder(self.root)
            with open('output', 'a') as f:
                f.write('\n')
            
    def _preorder(self, cur_node):
        if cur_node != None:
            #print( cur_node.value )
            with open('output', 'a') as f:
                f.write(str(cur_node.value))
                f.write(' ')
            self._preorder(cur_node.left_child)
            self._preorder(cur_node.right_child)



def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    bstree = BSTree()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            #print('line=',line)
            if line.lower() == 'inorder':
                bstree.inorder(output)
            elif line.lower() == 'preorder':
                bstree.preorder(output)
            else:
                operation = line.split(' ')[0]
                #print(operation)
                key = int(line.split(' ')[1])
                #print(key)
                if operation.lower() == 'insert':
                    bstree.insert(key)
                elif operation.lower() == 'delete':
                    bstree.delete(key)
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

