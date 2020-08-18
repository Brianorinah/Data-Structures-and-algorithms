def preorder(tree):
    #the base case is to check if the tree exists if the tree is none the function returnw withot doing anything
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    #In postorder you only move the  print statement to the end
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def postorder_evalutaion(tree):
    #parse_tree evaluation using the postoder design
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_evalutaion(tree.get_left_child())
        res2 = postorder_evalutaion(tree.get_right_child())

        #the only thing that changed is that indead of printing as in the post order function 
        # we evaluate the left and right children 
        if res1 and res2:
            return opers[tree.get_root_val()](res1,res2)
        else:
            return tree.get_root_val()

def inorder(tree):
    #move the print in between the left and the right inorder recursive functions
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

#If we perform a simple inorder traversal of a parse tree we get our original expression back,
#without any parentheses . The following function prints the parse tree in the original way with its parenthesis

def print_expr(tree):
    str_val = ""
    if tree:
        str_val = "(" + print_expr(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_expr(tree.get_right_child()) + ")"
    
    return str_val


    
