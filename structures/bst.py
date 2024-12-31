class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self, value_compare, key_compare):
        self.root = None
        self.value_compare = value_compare
        self.key_compare = key_compare

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if self.value_compare(value, node.value) < 0:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self.insert_recursive(node.right, value)

    def search(self, value):
        return self.search_recursive(self.root, value)
    
    def search_recursive(self, node, value):
        if node is None:
            return node
        compare = self.key_compare(value, node.value)
        if compare == 0:
            return node
        elif compare < 0:
            return self.search_recursive(node.left, value)
        else:
            return self.search_recursive(node.right, value)
        
    def inorder(self):
        values = []
        self.inorder_recursive(self.root, values)
        return values

    def inorder_recursive(self, node, values):
        if node:
            self.inorder_recursive(node.left, values)
            values.append(node.value)
            self.inorder_recursive(node.right, values)