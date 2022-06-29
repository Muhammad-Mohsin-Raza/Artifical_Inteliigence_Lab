#!/usr/bin/env python
# coding: utf-8

# In[161]:


myGraph = {
1: [2,3,5],
2: [4,5],
3: [5,6],
5: [],
6: [7,9],
4: [5,8],
7: [4,5,8],
8: [],
9: [7,8]}


# In[162]:


def ids(node,i,goal):
    stack=[]
    goal=goal
    stack.append(node)
    explored=[]
    while stack:
        tmp_node=stack.pop()
        explored.append(tmp_node)
        print('Poping Element',tmp_node)
        if tmp_node == goal:
            print('Found')
            return True
        if i > 0:
            if myGraph[tmp_node] is not None:
                for child in myGraph[tmp_node]:
                    if child not in explored:
                        stack.append(child)
        else:
            tmp=[]
            for child in myGraph[tmp_node]:
                    if child not in explored:
                        tmp.append(child)
            while tmp:
                tmp_node=tmp.pop()
                explored.append(tmp_node)
                if tmp_node == goal:
                    print('Found')
                    return True
               
        i=i-1
        print('Explored:',explored,'\n')
    


# In[163]:


i=0
goal=9
while ids(1,i,goal) != True:
    i=i+1

