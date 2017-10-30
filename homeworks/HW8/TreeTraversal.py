class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):     
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
    
    def _insert(self, val, node):
        if val <= node.val:
            if node.left is not None:
                self._insert(val, node.left)
            else:
                node.left = TreeNode(val)
                node.left.parent = node
        else:
            if node.right is not None:
                self._insert(val, node.right)
            else:
                node.right = TreeNode(val)
                node.right.parent = node
    
    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)
    
    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)
        else:
            return None
              
    def getValues(self, depth):
        if self.root is None:
            return []
        else:
            val_list = []
            self._getValues(depth, self.root, val_list)
            return val_list
            
    def _getValues(self, depth, node, vals=[]):
        if depth == 0:
            vals.append(node.val)
        else:
            if node.left is not None:
                self._getValues(depth-1, node.left, vals)
            else:
                for i in range(int(2**(depth-1))):
                    vals.append(None)
            if node.right is not None:
                self._getValues(depth-1, node.right, vals)
            else:
                for i in range(int(2**(depth-1))):
                    vals.append(None)
        return vals
    
    def max_depth(self, root):
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
    def __len__(self):
        return self.max_depth(self.root)
    
from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    

class DFSTraversal:
    def __init__(self, tree, traversalType):
        self.traversalType = traversalType.name
        self.tree = tree
        self.pre_list = []
        self.in_list = []
        self.post_list = []
        self.preorder(self.tree.root)
        self.inorder(self.tree.root)
        self.postorder(self.tree.root)
        self.index = 0
        
    def changeTraversalType(self, traversalType):
        self.traversalType = traversalType.name
        self.index = 0
                 
    def preorder(self, node):
        if node is not None:
            self.pre_list.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)
                  
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.in_list.append(node.val)
            self.inorder(node.right)
            
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.post_list.append(node.val)
            
     
    def __next__(self):        
        if self.traversalType == 'PREORDER':
            try:
                value = self.pre_list[self.index]
            except IndexError:
                raise StopIteration()
            self.index += 1
            return value        
            
        elif self.traversalType == 'INORDER':
            try:
                value = self.in_list[self.index]
            except IndexError:
                raise StopIteration()
            self.index += 1
            return value 
            
        elif self.traversalType == 'POSTORDER':
            try:
                value = self.post_list[self.index]
            except IndexError:
                raise StopIteration()
            self.index += 1
            return value 
        
        
    def __iter__(self):
        return self