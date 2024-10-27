class Solution:
    def partitionString(self, s: str) -> int:
        buffer = {s[0]}
        nb_partitions = 1
        for char in s[1:]:
            print(char in buffer)
            if char in buffer:
                nb_partitions += 1
                buffer.clear()            
            buffer.add(char)
        return nb_partitions
        