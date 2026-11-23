class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None 
        self.lcount=0#initialisation of root node
    
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
def inorder(temp):#recursive
    if temp is None: #terminating condition in recursive call
        return
    else:
        # temp=self.count
        inorder(temp.left)
        print(temp.data, end=" ")
        
        # if self.left is not None or self.right is not None:
        # if temp.left and temp.right is None:
            # self.lcount+=1 count the no of leaf nodes
        # temp.count+=1 count the no of nodes only
        inorder(temp.right)
     
            #print(self.data, end=" ")
# def find_minmax(self,root):
#     temp=root
#     while temp.left:
#         temp=temp.left
#     print("\nminimun value:", temp.data)
#     temp=root
#     while temp.right:
#         temp=temp.right
#     print("\n Max value:", temp.data)
b=BST()
b.insert(Node(10))
b.insert(Node(88))
b.insert(Node(99))
b.insert(Node(96))
b.insert(Node(2))
inorder(b.root)
# find_minmax(b.root)
# print("Total Node", b.count)

