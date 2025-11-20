from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################
        A.sum = A.item.val
        if A.left: A.sum += A.left.sum
        if A.right: A.sum += A.right.sum

        mid = A.item.val
        left = -float('inf')
        right = -float('inf')

        if A.left: 
            left = A.left.max_prefix
            mid += A.left.sum
        if A.right: 
            right = mid + A.right.max_prefix
        A.max_prefix = max(mid,right,left)
        if A.max_prefix == mid: A.max_prefix_key = A.item.key
        elif A.max_prefix == right: A.max_prefix_key = A.right.max_prefix_key
        else: A.max_prefix_key = A.left.max_prefix_key

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        ##################
        k = self.root.max_prefix_key
        s = self.root.max_prefix
        
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    toppings.sort(key = lambda topping: topping[0])
    for (x,y,t) in toppings:
        B.insert(Key_Val_Item(y,t))
        (Y_,T_) = B.max_prefix()
        if T<T_:
            X,Y,T = x,Y_,T_
    return (X, Y, T)
