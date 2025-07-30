# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 17:06:26 2025

@author: manid
"""

#each child has three nodes, all of which are larger than (or equal to) than the parent
class MinHeap:
    def __init__(self):
        self.tree={}
        self.next_index=0
    
    def __len__(self):
        return self.next_index
    
    def insert(self, value):
        #add value to next available slot in tree
        self.tree[self.next_index] = value
        
        #up heapify
        current_index = self.next_index
        current_value = value
        self.next_index+=1
        
        
        while(True):
            parent_index = self.get_parent_index(current_index)
            #if we reached the root or the condition is satisfied that is the "base case"
            if parent_index not in self.tree:
                return
            if self.tree[parent_index] < self.tree[current_index]:
                return
            
            #else swap the values
            d = self.tree[parent_index]
            self.tree[parent_index] = self.tree[current_index]
            self.tree[current_index] = d
            
            #recurse
            current_index = parent_index
            
        
    
    def delete(self):
        if self.next_index==0:
            return
        
        #swap last element with root
        d = self.tree[0]
        self.tree[0] = self.tree[self.next_index-1]
        self.tree[self.next_index-1] = d
        
        #remove root
        root = self.tree[self.next_index - 1]
        self.tree.pop(self.next_index-1)
        self.next_index-=1
        
        #heapify down
        current_index = 0
        
        while(True):
            smallest_child_index = self.get_smallest_child(current_index)
            if smallest_child_index == None:
                return root
            if self.tree[smallest_child_index] >= self.tree[current_index]:
                return root
            
            d = self.tree[smallest_child_index]
            self.tree[smallest_child_index] = self.tree[current_index]
            self.tree[current_index] = d
            
            current_index = smallest_child_index
        
    
    def get_parent_index(self, index):
        if index%3 == 1:
            return (index-1)//3
        elif index%3 == 2:
            return (index-2)//3
        else:
            return (index-3)//3
    
    
    def get_smallest_child(self, index):
        #find minimum child
        min_child_index=None
        
        if (index*3+1 in self.tree):
            if(index*3+2 in self.tree):
                
                if(self.tree[index*3+2]>self.tree[index*3+1]):
                    min_child_index = index*3+1
                else:
                    min_child_index = index*3+2
                
                if(index*3+3 in self.tree):
                    if(self.tree[min_child_index]>self.tree[index*3+3]):
                        return index*3+3
                    else:
                        return min_child_index
                else:
                    return  min_child_index
                
            else:
                return index*3+1 #because only first child exists
        else:
            return None  #bc if there's no 'first child' there's definitely no second or third child 
        
        
        
        
    


# r = MinHeap()
# for i in range(10,0,-1):
#     r.insert(i)
#     #print(r.tree)
# print("--------------------------")

# for i in range(10,0,-1):
#     print(r.delete())
#     #print(r.tree)
# print("--------------------------")
