from binary_tree_with_node_and_references import BinaryTree
from stack import Stack
import operator


def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    # use a stack to store the parent nodes
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree

    for token in fp_list:
        if token == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif token not in ['+', '-', '/', '*', ')']:
            current_tree.set_root_val(int(token))
            parent = p_stack.pop()
            current_tree = parent

        elif token in ['+', '-', '/', '*']:
            current_tree.set_root_val(token)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif token == ')':
            current_tree = p_stack.pop()

        else:
            raise ValueError

    return e_tree
# Algorithm that evaluates a parse tree by recursively evaluating each subtree.


def evaluate(parse_tree):
    #Dictionary that hold the operator functions eg operator.add(4,5) will give 9 etc.
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        #recursively generate the result to each tree
        return fn(evaluate(left),evaluate(right))
    #A natural base case for this recursive algorithms
    #that operate on trees is to check for a leaf node. Leaf nodes will always be operands.
    else:
        return parse_tree.get_root_val()

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))
# pt.postorder() #defined and explained in the next section
