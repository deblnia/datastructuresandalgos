
Setup: :set spell spelllang=en_us to get spellcheck

## Question I. 
(A) Reading takes one operation. 

(B) Searching for a value not contained in the array takes N operations where N is the length of the array. 
 
(C) Insertion at the beginning of the array takes N+1 operations, since we have to shift every element of the array to the right and then insert the value. 
(D) Insertion at the end of the array takes one operation since the compiler keeps track of the length of the array, so can just insert at the next memory address.
 
(E) Deletion at the beginning of the array takes N operations since the deletion is one operation, and then all the other elements of the array (N-1) need to be shifted left. 

(F) Deletion at the end of an array takes one operation. 

## Question II. 

(A) Reading from an array based set will take one operation. 

(B) Searching an array based set for a value it does not contain will take N operations where N is the length of the array. 

(C) Insertion of a new value at the beginning of a set  will take 2N+1 operations. One pass will be needed to search and make sure that the element doesn't already exist in the set, and then we can insert, and then we need to shift every element right. 

(D) Insertion at the end of a set will take N+1 one operations (one to do the deletion and N to shift everything else right). 

(E) Deletion from the beginning of an array will take one step just like a classic array.  

(F) Deletion from the end of an array will take one step. 



Question III.  
To find all instances of an element in an array, we would need to traverse the entire array, so that's N operations. 
