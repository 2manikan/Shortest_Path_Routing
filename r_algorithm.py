# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 18:32:44 2025

@author: manid
"""

from min_heap import MinHeap

#graph is an adjacency list: of form {node:{node:weight, node:weight...}...}. is called nw

#this goes into the fringe
class Pair:
    def __init__(self, value, cost):
        self.cost=cost
        self.value=value
    def __gt__(self, other):
        return self.cost > other.cost
    def __ge__(self, other):
        return self.cost >= other.cost
    def __lt__(self, other):
        return self.cost < other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    def __eq__(self, other):
        return self.cost == other.cost
    def __ne__(self, other):
        return self.cost != other.cost
        

def shortest_path(start_node, dest_node, nw):
    visited_nodes={start_node:[0, None]}  #current_node:[path length from start node, parent_node]
    
    fringe = MinHeap()
    fringe.insert(Pair(start_node,0))  #the cost is the path length from start node
    
    #run dijikstra
    while(len(fringe) > 0):
        current = fringe.delete()
        current_node = current.value
        current_cost = current.cost   #this is the new cost that the algorithm discovered at one point
        
        
        for adj_node in nw[current_node]:
            #only expanding a node (adding to fringe basically) if we discovered an even shorter path than recorded (for the adjacent node)
            if adj_node in visited_nodes:
                if current_cost+nw[current_node][adj_node] < visited_nodes[adj_node][0]:
                    visited_nodes[adj_node] = [current_cost+nw[current_node][adj_node], current_node]
                    fringe.insert(Pair(adj_node, visited_nodes[adj_node][0]))
            else:
                visited_nodes[adj_node] = [current_cost+nw[current_node][adj_node], current_node]
                fringe.insert(Pair(adj_node, visited_nodes[adj_node][0]))


    #calculate and return path
    node = dest_node
    path = [dest_node]
    while node!=start_node:
        node = visited_nodes[node][1]
        path.append(node)
    
    
    return path
        

#undirected graph here
net = {"0.0.0.0":{"1.1.1.1":1, "2.2.2.2":1, "3.3.3.3":1}, "1.1.1.1":{"0.0.0.0":1, "2.2.2.2":1, "3.3.3.3":1, "4.4.4.4":1, "5.5.5.5":1}, 
       "2.2.2.2":{"0.0.0.0":1, "1.1.1.1":1, "3.3.3.3":1}, "3.3.3.3":{"0.0.0.0":1, "1.1.1.1":1, "2.2.2.2":1, "4.4.4.4":1, "5.5.5.5":4}, 
       "4.4.4.4":{"1.1.1.1":1, "3.3.3.3":1, "5.5.5.5":1}, "5.5.5.5":{"1.1.1.1":1, "3.3.3.3":4, "4.4.4.4":1}}   


shortest = shortest_path("2.2.2.2", "5.5.5.5", net)     
print(shortest)

