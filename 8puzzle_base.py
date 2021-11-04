from queue import Queue
 #from graphviz import Digraph
import os

class Node:
    def _init_(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.id = "".join(str(n) for n in self.state)
    def _repr_(self):
        joined_string = " ".join(str(n) for n in self.state)
        return joined_string[0:5]+"\n"+joined_string[6:11]+"\n"+joined_string[12:17]

def possible_moves(state):
    pos_moves = []
    if state[0]==0: pos_moves.append(['right','down']) 
    if state[1]==0: pos_moves.append(['left','right','down']) 
    if state[2]==0: pos_moves.append(['left','down']) 
    if state[3]==0: pos_moves.append(['up','right','down']) 
    if state[4]==0: pos_moves.append(['left','up','right','down']) 
    if state[5]==0: pos_moves.append(['left','up','down']) 
    if state[6]==0: pos_moves.append(['up','right']) 
    if state[7]==0: pos_moves.append(['left','up','right']) 
    if state[8]==0: pos_moves.append(['left','up']) 
    return pos_moves
    

def generate_state(state, m):
    temp= copy.deepcopy(state)
    index=temp.index(0)
    if m=="up":
        if index not in range(0,1,2):
            a = temp[i-3]
            temp[index-3]=temp[index]
            temp[index]=a
       
    if m=="down":
        if index not in range(6,7,8):
            a = temp[index+3]
            temp[index+3]=temp[index]
            temp[index]=a
        
    if m=="left":
        if index not in range(0,3,6):
            a = temp[index-1]
            temp[index-1]=temp[index]
            temp[index]=a
        
    if m=="right":
        if index not in range(2,5,6):
            a = temp[index+1]
            temp[index+1]=temp[index]
            temp[index]=a
    return temp

def create_node(state, parent, action, depth):
    return Node(state, parent, action, depth)

def expand_node(node):
    expanded_nodes = []
    L = possible_moves(node)
    for i in L: 
        expanded_nodes.append(generate_state(node,L[i]) )
    return expanded_nodes

def dfs(node):
    stack = []
    visited = []
    visited_str = []
    depth_limit = 5
    stack.append(create_node(initial, "283164705", None, 0))
    while len(stack) > 0:
        if len(stack) == 0: 
            return None
        node = stack.pop(0)
        if node.id in visited_str:
            continue
        else:
                visited.append(node)
                visited_str.append(node.id)
        if node.state == goal:
                return visited
        if node.depth < depth_limit:
                if node.depth < depth_limit:
                    expanded_nodes = expand_node(node)
                    if(expanded_nodes not in visited):
                        expanded_nodes.extend(stack)
                        stack = expanded_nodes

 def bfs(initial):
     visited=[]
     queue=[initial]
     while queue:
         node=queue.pop(0)
         if node not in visited :
             if visited.state==goal:
                 return visited

             visited.append(node)
             next=expand_node(node)
             for nexts in next :
                 queue.append(nexts)
            


'''def display(title, path, file):
    # Start - Graphs init
    graph_dfs = Digraph(comment=title)
    step = 0
    color = "black"
    for node in path:
        node_str = node._str_()
        if node.state == goal: color = "green"
        graph_dfs.node(str(node.id), node_str, color=color)
        graph_dfs.edge(str(node.parent), str(node.id), str(node.action) + "\n" + str(step))
        step += 1


    # Start - Graphs rendering
    graph_dfs.render(str(os.getcwd() + '/outputs/' + file + '.gv'), view=True)
	# End - Graphs rendering
'''	
	
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial = [2, 8, 3, 1, 6, 4, 7, 0, 5]

 #display("DFS graph", dfs(), "dfs")
#display("BFS graph", bfs(), "bfs")