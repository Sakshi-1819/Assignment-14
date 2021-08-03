#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".

# In[5]:


def longestCommonPrefix( a):
     
    size = len(a)
 
    if (size == 0):
        return ""
 
    if (size == 1):
        return a[0]
 
    a.sort()
     
    end = min(len(a[0]), len(a[size - 1]))
 
    i = 0
    while (i < end and
           a[0][i] == a[size - 1][i]):
        i += 1
 
    pre = a[0][0: i]
    return pre

if __name__ == "__main__":
 
    input = ["flower","flow","flight"]
    print("The longest Common Prefix is :",
                 longestCommonPrefix(input))


# In[6]:


def longestCommonPrefix( a):
     
    size = len(a)
 
    if (size == 0):
        return ""
 
    if (size == 1):
        return a[0]
 
    a.sort()
     
    end = min(len(a[0]), len(a[size - 1]))
 
    i = 0
    while (i < end and
           a[0][i] == a[size - 1][i]):
        i += 1
 
    pre = a[0][0: i]
    return pre

if __name__ == "__main__":
 
    input = ["dog","racecar","car"]
    print("The longest Common Prefix is : ' ' " ,
                 longestCommonPrefix(input))


# # Q2. Given an array arr[] of distinct integers of size N and a sum value X, the task is to find count of triplets with the sum smaller than the given sum value X.

# In[9]:


def countTriplets(arr, n, sum):
 
    ans = 0
 
    for i in range( 0 ,n-2):
     
        for j in range( i+1 ,n-1):
     
            for k in range( j+1, n):
                if (arr[i] + arr[j] + arr[k] < sum):
                    ans+=1
     
    return ans
 
arr = [-2, 0, 1, 3]
n = len(arr)
sum = 2
print(countTriplets(arr, n, sum))


# In[7]:


def countTriplets(arr, n, sum):
 
    ans = 0
 
    for i in range( 0 ,n-2):
     
        for j in range( i+1 ,n-1):
     
            for k in range( j+1, n):
                if (arr[i] + arr[j] + arr[k] < sum):
                    ans+=1
     
    return ans
 
arr = [5, 1, 3, 4, 7]
n = len(arr)
sum = 12
print(countTriplets(arr, n, sum))


# # Q4. Given a Binary Tree, print Left view of it.Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.The task is to complete the function leftView(), which accepts root of the tree as argument.

# In[15]:


class newNode:
 
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0
 
 
def printLeftView(root):
 
    if (not root):
        return
 
    q = []
    q.append(root)
 
    while (len(q)):
 
        n = len(q)
 
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
 
            if (i == 1):
                print(temp.data, end=" ")

            if (temp.left != None):
                q.append(temp.left)

            if (temp.right != None):
                q.append(temp.right)
 
if __name__ == '__main__':
 
    root = newNode(1)
    root.left = newNode(3)
    root.right = newNode(2)
    printLeftView(root)


# # Q5. Given a Binary Tree, find Right view of it.Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

# In[20]:


from collections import deque
 
class Node:
     
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
 
def rightView(root):
     
    if root is None:
        return
 
    q = deque()
    q.append(root)
 
    while q:
         
        n = len(q)
 
        while n > 0:
            n -= 1
             
            node = q.popleft()
 
            # Print the last node of each level
            if n == 0:
                print(node.data, end = " ")
 
            if node.left:
                q.append(node.left)
 
            if node.right:
                q.append(node.right)
 
root = Node(1)
root.left = Node(3)
root.right = Node(2)
rightView(root)


# 

# In[ ]:





# In[ ]:




