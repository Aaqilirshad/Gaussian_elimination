#!/usr/bin/env python
# coding: utf-8

"""Converts a given matrix to Row Echolen Form"""


import numpy as np


# In[336]:


def is_zero_matrix(A):
    #this function returns true is the matrix is a zero matrix else returns false
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i,j] != 0:
                return False
    return True


# In[337]:


def convert_leading_entries(m):
    n = m.astype(float)
    
    #for every row go through every column
    for row in range(n.shape[0]):
        for column in range(n.shape[1]):
            
            #if the n[row][column]'th index is not a zero, divide the row by that entry
            if n[row][column] != 0:
                n[row] = n[row] / n[row][column]
                break
            else:
                continue
                
        #handling negative zeros
        for i in range(n.shape[1]):
            if n[row][i] == 0.0:
                n[row][i] += 0
                
                
    return n.round(2)


# In[338]:


def zero_rows_to_bottom(matrix):
    # Compute row sums and use argsort to get the indices that would sort them.
    row_sums = np.sum(matrix, axis=1)
    sorted_indices = np.argsort(row_sums)
    
    # Reverse the order of the sorted indices to place zeros at the bottom.
    sorted_indices = sorted_indices[::-1]
    
    # Rearrange the rows based on the sorted indices.
    sorted_matrix = matrix[sorted_indices]
    
    return sorted_matrix


# In[363]:


def gaussian(m):
    
    #check if it is a zero matrix
    if is_zero_matrix(m):
        return m
    
    #if there is any zero rows place them at the bottom of the row
    m = zero_rows_to_bottom(m)
    
    #deal with single coloumn matrix
    if m.shape[1] == 1:
        m[0][0] = 1
        for i in range(len(m) - 1):
            m[i + 1][0] = 0
        return m
            
    
    #initialize variables
    l = len(m)-1
    i = 0
    
    
    while i < l:
        
        j = i + 1
        #for every column i,
        #check if the column is a zero column, if it is skip for the current i, else continue
        if not any(m[:, i]):
            i += 1
                
        
        #if the pivot index is zero, replace the row with a row that is not zero
        
        if m[i][i] == 0:
            for k in range(j, l):
                if m[j][i] != 0:
                    m[[i, j]] = m[[j , i]]
                    break
                    
                    
                    
        #convert the entries below the pivot index to 0
        #for every coloumn i, the rows starting from j = i + 1 are the entries below pivot index
        
        for row in range(j, len(m)):
            #check if the entry is already zero
            if m[row][i] != 0:
                """scaling and converting to zero"""
                
                pivot_row = m[i].copy()
                current_row = m[row].copy()
                pivot_index = m[i][i].copy()
                current_index = m[row][i].copy()
                
                m[row] = current_row * pivot_index - pivot_row * current_index  
                
        i += 1
           
    #turn the pivot indexes to 1, leading non zero entry in a column
    
    m = convert_leading_entries(m)
                
    return m
        
                
            


# In[364]:

#test matrixes
arr = np.array([[0,0,0], [0,0,0], [0,0,0]])
A = np.array([[3,2,3,5], [2,5,3,0], [8,3,2,0]])
B = np.array([[0,2,3,5], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
C = np.array([[1,2,3,5], [2,0,3,0], [8,3,0,0]])
D = np.array([[0,0,0,0], [0,1,2,1], [1,2,2,1]])
m = np.array([[1,2], [2,4], [0,7]])
j = np.array([[1], [2], [4]])


# In[375]:


a = A.copy()
print(a)


# In[376]:


print(gaussian(a))


