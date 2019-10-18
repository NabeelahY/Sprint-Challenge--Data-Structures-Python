
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Base Case
        # if value is equals to none
        if self.value is None:
            # self.value = value
            self.value = BinarySearchTree(value)

        # Left case
        # check if value is less than current value
        if value < self.value:
            # check if current value has left child
            if self.left is None:
                # if there is no left child, left child is equals to value
                self.left = BinarySearchTree(value)
            # else repeat process (recursion)
            else:
                self.left.insert(value)

        # Right case
        # check if value is greater than current value
        elif value > self.value:
            # check if current value has right child
            if self.right is None:
                # if there is no right child, right child is equals to value
                self.right = BinarySearchTree(value)
            # else repeat process (recursion)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        # if self.value = target
        if self.value == target:
            # return true
            return True

        # Left case
        # check if current value is greater than target
        if self.value > target:
            # check if current node has a left child
            # if not return false
            if self.left is None:
                return False
            # else repeat process
            else:
                return self.left.contains(target)

        # Right case
        # check if current value is lesser than target
        if self.value < target:
            # check if current node has a right child
            # if not return false
            if self.right is None:
                return False
            # else repeat process
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Base case
        if self is None:
            return None
        # initialise max_val to be root
        max_val = self.value
        # check if root has right
        if self.right is not None:
            # check for max value
            return self.right.get_max()
        else:
            # else return root
            return max_val

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Base case
        if self.value is None:
            return None
        else:
            cb(self.value)
        # Right case
        if self.right:
            self.right.for_each(cb)
        # Left case
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue data structure
        q = Queue()
        # enqueue the starting node on to the queue
        q.enqueue(node)
        # loop while the queue has data
        while q.len() > 0:
            # dequeue the current item off the queue
            current_node = q.dequeue()
            # print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # enqueue the left child on to the queue
                q.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # enqueue right child on to the queue 
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack data structure
        s = Stack()
        # push the starting node on to the stack
        s.push(node)
        # loop while the stack has data
        while s.len() > 0:
            # pop the current it em off the stack
            current_node = s.pop()
            # print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # push the left child on to the stack
                s.push(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # push right child on to the stack
                s.push(current_node.right)      
                