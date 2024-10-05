# two sum 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

------

I ran into some problems with even just the brute force implementation of this one. 
- Enumerate returns a tuple of (index, value)
- Since we don't want a synchronized loop (we want an offset loop), the inner loop index needs to be modified accordingly
