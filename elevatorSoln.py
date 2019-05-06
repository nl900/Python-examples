#!/usr/bin/env python3

"""
There is an elevator in a building with M floors. 
This elevator can take a max of X people at a time or max of total weight Y. 
Given that a set of people and their weight and the floor they need to stop, 
how many stops has the elevator taken to serve all the people? 
Consider the elevator serves in “first come first serve” basis and the order 
for the queue can not be changed.

Example:
Let Array A be the weight of each person A = [60, 80, 40]. 
Let Array B be the floors where each person needs to be dropped off B = [2, 3, 5].
The building has 5 floors, maximum of 2 persons are allowed in the elevator 
at a time with max weight capacity being 200. For this: example, 
the elevator would take total of 5 stops in floors: 2, 3, G, 5 and finally G.
"""

def calcStops(A, B, M, X, Y):
    curr_weight = 0
    curr_ppl = 0
    dest = set() #floor dest maybe duplicate
    
    count = 0
       
    i = 0
    while i < len(A):
        while curr_weight <= Y or curr_ppl <= X:
            #check whether can fit this person
            if (curr_weight + A[i]) > Y or (curr_ppl + 1) > X: 
                break
            
            #can fit
            curr_weight += A[i]
            curr_ppl += 1
            dest.add(B[i])
            
            i += 1
            
            if i == len(A): break #last person

        #lift is full, make stops     
        count += len(dest)
        count += 1 #return to G
        
        #reset
        curr_weight = 0
        curr_ppl = 0
        dest.clear()
        
    return count

A = [60, 80, 40]
B = [2, 3, 5]
print(calcStops(A, B, 5, 2, 200))
