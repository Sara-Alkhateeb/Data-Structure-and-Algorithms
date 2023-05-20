from trees import Binary_Tree, Node

B_tree =Binary_Tree()

node1=Node("A")
B_tree.root=node1

node2=Node("B")
node1.left=node2

node3=Node("C")
node1.right=node3

node2.left=Node("D")
node2.right=Node("E")

node3.left=Node("F")

stack_pre_order= []
stack_in_order=[]
stack_post_order=[]

def pre_order(root):
    if root is not None:
        stack_pre_order.append(root.value)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)
    return stack_pre_order


def in_order(root):
    if root.left is not None:
        in_order(root.left)
    if root is not None:
        stack_in_order.append(root.value)
    if root.right is not None:
        in_order(root.right)
    return stack_in_order
    
def post_order(root):
    if root.left is not None:
        post_order(root.left)

    if root.right is not None:
        post_order(root.right)

    if root is not None:
        stack_post_order.append(root.value)
    return stack_post_order

print(pre_order(node1))
print("********************************")
print(in_order(node1))
print("********************************")
print(post_order(node1))
        
        
        

        
            
        
        






