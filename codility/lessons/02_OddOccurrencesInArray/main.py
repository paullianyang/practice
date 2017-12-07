#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# Constraints:
# Time O(N)
# Space O(1)

def solution(A):
    # because all but one pair up, a bitwise comparison XOR
    # of the prime factorization will result with the extra number
    remaining = 0
    for i in A:
        remaining = remaining ^ i
    return remaining

print solution([9,3,3,9,9,9,7])
print solution([1])
print solution([4,1,1,5,1,2,2,1,4])
