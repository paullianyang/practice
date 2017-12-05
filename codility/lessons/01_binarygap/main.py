#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://codility.com/programmers/lessons/1-iterations/binary_gap/

# Constraints:
# Time O(log(N))
# Space O(1)

def solution(N):
    # first convert integer to binary string
    # iterate through string while tracking:
    #     first initial 1 (one_track)
    #     subsequent closing 1 (i == '1')
    #     number of 0 within 1s (gap_counter)
    #     largest number of 0 within 1s (max_gap)
    int_to_bin = '{0:b}'.format(N)
    max_gap = 0
    gap_counter = 0
    one_track = 0
    for i in int_to_bin:
        # count 0 if opening 1 occurred
        if one_track == 1 and i == '0':
            gap_counter += 1
        # trackings first 1 occurence
        if i == '1' and one_track == 0:
            one_track = 1
        # finds largest gap_counter
        elif i == '1' and one_track == 1:
            max_gap = gap_counter if gap_counter > max_gap else max_gap
            gap_counter = 0
    return max_gap

print 0, solution(0)
print 1, solution(1)
print 5, solution(5)
print 1041, solution(1041)
print 2147483647, solution(2147483647)
