from typing import List
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def shift(c:int, direction:int):
            sign = 1 if direction else -1        
            result = c + sign
            result = result % 26
            return result
        
        def normlize(c:str):
            return ord(c) - 97

        offsets = np.zeros(len(s),dtype=np.int_)
        
        sign = [-1,1]
        for action in shifts:
            start = action[0]
            end = action[1] + 1
            direction = action[2]
            offsets[start:end] = offsets[start:end] + sign[direction]
        ord_func = np.frompyfunc(ord, 1, 1)
        chr_func = np.frompyfunc(chr, 1, 1)
        offsets = (offsets + (ord_func(np.array(list(s))) - 97)) % 26 
        return ''.join(chr_func(offsets + 97))