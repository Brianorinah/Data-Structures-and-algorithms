class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.root

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            #nb inch worm(do not change the reference to the root before assigning the previous reference to the new node)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            #nb inch worm(do not change the reference to the root before assigning the previous reference to the new node)
            t.right_child = self.right_child
            self.right_child = t

    #Accessor methods
    def get_root_val(self):
        return self.root
    
    def set_root_val(self,new_root):
        self.root = new_root
    
    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    #internal preorder
    def preorder(self):
        #print the root
        print(self.key)
        #If there is a left and right child perform preorder on them
        if self.get_left_child():
            self.left_child.preorder()
        if self.get_right_child():
            self.right_child.preorder()

if __name__ == "__main__":
    r = BinaryTree('a')
    r.insert_left("b")
    r.insert_right("c")
    r.set_root_val("d")
    c = r.get_left_child()
    print(c.root)
    # r.get_left_child().insert_right("d")
    # r.get_right_child().insert_left("e")
    # r.get_right_child().insert_right("f")
    # print(r.get_left_child())
    # print(r.get_right_child().get_left_child())


    # r = BinaryTree('a')
    # print(r.get_root_val())
    # print(r.get_left_child())
    # r.insert_left('b')
    # print(r.get_left_child())
    # print(r.get_left_child().get_root_val())
    # r.insert_right('c')
    # print(r.get_right_child())
    # print(r.get_right_child().get_root_val())
    # r.get_right_child().set_root_val('hello')
    # print(r.get_right_child().get_root_val())

