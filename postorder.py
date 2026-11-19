class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None #initialisation of root node
    
    def insert(self,new_node):
        if self.root is None: #creating the root node
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #new_node.data>=temp.data
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
def postorder(temp):#recursive
    if temp is None: #terminating condition in recursive call
        return
    else:
        postorder(temp.left)
        
        postorder(temp.right)
        print(temp.data, end=" ")
            #print(self.data, end=" ")
b=BST()
b.insert(Node(10))
b.insert(Node(88))
b.insert(Node(99))
b.insert(Node(96))
b.insert(Node(2))
postorder(b.root)
