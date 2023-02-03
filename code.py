from functools import cache
#The cache keeps references to the arguments and return values until they age out of the cache or until the cache is cleared. 
#If a method is cached, the self instance argument is included in the cache.

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def inform_time(i):
            if i == -1:
                return 0
            return informTime[i] + inform_time(manager[i])
        return max(map(inform_time, range(n)))
      

