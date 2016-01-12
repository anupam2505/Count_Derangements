# Count Derangements 

## Problem
A Derangement is a permutation of n elements, such that no element appears in its original position. For example, a derangement of {3, 0, 1, 2} is {2, 3, 0, 1}.

Given a number n, find total number of Derangements of a set of n elements.

```python
Input: n = 2
Output: 1
For two elements say {1, 0}, there is only one 
possible derangement {0, 1}

Input: n = 3
Output: 2
For three elements say {0, 1, 2}, there are two 
possible derangements {2, 0, 1} and {1, 2, 0