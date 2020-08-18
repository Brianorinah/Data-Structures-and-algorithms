# Code class that represents the whole binary serach tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # def __iter__(self):
    #     return self.root.__iter__()

    # inorder iteration
    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    # Adding a node to the tree
    def put(self, key, val):
        # check if the current tree has a root(is empty) if not empty
        # traverse the tree to find the suitable place to add it
        if self.root:
            self._put(key, val, self.root)

        # if it is empty add the node as the root
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    # cecking to whether to put the node on the left subtree(key < current_node) or the right(key > current_node)
    def _put(self, key, val,  current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child())
            else:
                current_node.left_child = TreeNode(
                    key, val, parent=current_node)

        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, val, parent=current_node)

    # this is overloading the [] operator for assignment
    # This allows us to write Python statements like
    # my_zip_tree['Plymouth'] = 55446, just like a Python dictionary.
    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        # base case if if the current node evaluates to None
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    # By implementing the __getitem__ method we can write a Python statement that looks just
    # like we are accessing a dictionary, when in fact we are using a binary search tree, for example
    # z = my_zip_tree['Fargo'].
    def __getitem__(self, key):
        self.get(key)

    # method will simply call get and return True if get
    # returns a value, or False if it returns None.
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
        # __contains__ overloads the in operator and allows us to write statements such as:
        # if 'Northfield' in my_zip_tree:
        #print("oom ya ya")

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in the tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in the tree")

    # Overloading the del operator eg del 54
    def __delitem__(self, key):
        self.delete(key)

    # function to remove the found node
    def remove(self, current_node):
        # if the node to be deleted is a leaf(has no children)
        if current_node.is_leaf():
            # if it was a left child else if it was a right child
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

        # if the node has both children
        elif current_node.has_both_children():
            # find the sucessor
            succ = current_node.find_successor()
            # remove the successor from the tree
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload

        # if the node has only one child
        else:
            # if the found node has only a left child
            if current_node.has_left_child():
                # if found node was a left child
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                # if found node was a right child
                if current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                # if the found node was the root node
                else:
                    current_node.replace_node(current_node.left_child.key,
                                              current_node.left_child.payload,
                                              current_node.left_child.left_child,
                                              current_node.left_child.right_child)

            # if the found node has only a right child
            else:
                # if found node was a left child
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                # if found node was a right child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                # if the found node was the root node
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def find_successor(self):
        succ = None
        # If the node has a right child, then the successor is the smallest key in the right subtree]
        # Nb This is the only condition that matters when it comes to deleting a node from a binary search tree.
        if self.has_right_child():
            self.right_child.find_min()
        # the node has no right child
        else:
            if self.parent:
                # If the node has no right child and is the left child of its parent, then the parent is the successor.
                if self.is_left_child():
                    succ = self.parent
                # If the node has no right child and itself has no right child, then the successor
                # to this node is the successor of its parent, excluding this node
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    # You should convince yourself that the minimum valued key in any binary search tree is the leftmost child of the tree.
    # This method finds it.
    def find_min(self):
        current = self
        while current.has_left_child:
            current = current.left_child
        return current

    # The successor is guaranteed to have no more than one child, so we know how to remove it using the two
    # cases for deletion that we have already implemented . This function removes the successor.
    def splice_out(self):
        # if the successor had no childrea(leaf)
        if self.is_leaf():
            # if the successor was a left/right child
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # Check whicch child thae successor has either the right or left
        # Remember the successor cant have both children
        elif self.has_any_children():
            # If the successor has a left child
            if self.has_left_child():
                # if the successor was a left/right child
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            # If the successor has a right child
            else:
                # if the successor was a left/right child
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent


# Code class that represents each node(Each node is an object of this class)
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, left, right):
        self.key = key
        self.payload = value

        # Sometimes we will want to construct a new TreeNode that already has
        # both a parent and a child. With an existing parent and child, we can pass parent and child as
        # parameters.
        self.left_child = left
        self.right_child = right

        # At other times we will just create a TreeNode with the key value pair, and we will
        # not pass any parameters for parent or child. In this case, the default values of the optional
        # parameters are used.
        if self.has_left_child():
            self.left_child.parent = self

        if self.has_right_child():
            self.right_child.parent = self


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree[3] = "red"
    my_tree[4] = "blue"
    my_tree[6] = "yellow"
    my_tree[2] = "at"
    print(my_tree.get(6))
    print(my_tree.get(2))
    # Matters to do:-
    # ovrloadind does not work eg my_tree[6] gives None
