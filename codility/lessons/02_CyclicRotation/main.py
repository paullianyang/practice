#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A, K):
    # Since shifts beyond the array length just wraps around
    # max shift is determined by the length of the array
    # and any further extra can be reduced to the modulo
    array_len = len(A)
    rotation = array_len % K
    return A[rotation:] + A[:rotation]

print solution([3, 8, 9, 7, 6], 3)
print solution([0, 0, 0], 1)
print solution([1, 2, 3, 4], 4)
