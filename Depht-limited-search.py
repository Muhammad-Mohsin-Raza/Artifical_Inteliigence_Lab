from operator import le
from tkinter import font
# from tkinter import N
from tokenize import Expfloat
from unittest import removeResult


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.parent=None
        self.val = val

    def insert(self, val):
        # print('Insert: ', self.val,val,self.left)
        if not self.val:
            self.val = val            
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            self.left.parent=self
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        self.right.parent=self

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def level(self,node,level_limit,level_val=0):
        if node == None:
            return

        # print node value and its depht 
        #print(node.val,level_limit,level_val)
        
        if level_val == level_limit:
            # have to non left and right
            # print('true')
            node.left =None
            node.right=None
            return 0
        
        
        if node.left:
           level_val+=self.level(node.left,level_limit,level_val+1)
        #    print(node.val,':',level_val)
        
        if node.right:
        
           level_val+=self.level(node.right,level_limit,level_val+1)
        #    print('In right',node.val,':',level_val)

        return 0
        

    def dls(self,value,level_limit,level_val=0):
        
        self.level(self,level_limit,level_val)
        print(bst.inorder([]))
        print('Fun call')
        
        
        frontier=[]    
        explored_states=[]
        
        frontier.append(self)
        # if frontiers is empty then no sol
        while len(frontier) !=0 :
            f1=[]
            e1=[]
            for f in frontier:
                f1.append(f.val)
            print('frontier values:',f1)
            
            for e in explored_states:
                e1.append(e.val)
            print('explored states:',e1)
            print('\n')
            
            
            # remove a node from frontier
            tmp_node = frontier.pop()
            print('poping element:',tmp_node.val)


            # apply goal test
            print('Applying goal test')
            if tmp_node.val == value:
                self.reverse(tmp_node)
                return
            # add node to explored state
            explored_states.append(tmp_node)
            
            # Expande node  add resulting nodes  to frontier
            # if they aren't in ecplored set

            if tmp_node.left != None:
                if any(tmp_node.left.val != Nodes.val for Nodes in explored_states) :
                    frontier.append(tmp_node.left)

            if tmp_node.right != None:
                if any(tmp_node != nodes.val for nodes in explored_states) :
                    frontier.append(tmp_node.right)
            print('---------------------')

        print('No solution exist :')
            
            
            
    
    def reverse(self,Node):
        path=[]
        while Node is not None:
            
            path.append(Node.val)
            Node=Node.parent
        path.reverse()
        print('-----path found-----')
        print(*path,sep='->')



if __name__ == '__main__':
    nums = [12, 6,5,4,7,18,4,50,40]
    # nums=[1,2,3]
    # nums=[50,30,20,40,70,60,80]
    # nums=[50,30,20,40,70,60,80,35]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.inorder([]))
    print("#")

    # values to be searched , pass limit of depht as paramenter
    bst.dls(4,2)

    