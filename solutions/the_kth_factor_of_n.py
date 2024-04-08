class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        to_n = range(1,n+1)
        rank = -1
        factor = 0
        for e in to_n:
            if n % e == 0:
                factor+=1
            print(factor)
            if factor == k:
                
                rank = e
                break
        print(rank)
        return rank