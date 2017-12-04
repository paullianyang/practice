#!/user/bin/python
# https://codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    int_to_bin = '{0:b}'.format(N)
    max_gap = 0
    gap_counter = 0
    one_track = 0
    for i in int_to_bin:
        if one_track == 1 and i == '0':
            gap_counter += 1
        if i == '1' and one_track == 0:
            one_track = 1
        elif i == '1' and one_track == 1:
            max_gap = gap_counter if gap_counter > max_gap else max_gap
            gap_counter = 0
    return max_gap

print 0, solution(0)
print 1, solution(1)
print 5, solution(5)
print 1041, solution(1041)
print 2147483647, solution(2147483647)
