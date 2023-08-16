from typing import List
from collections import defaultdict

class Solution:

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []


        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)
            
        
        return result

# Create an instance of the Solution class and call the function
solution = Solution()
print(solution.groupAnagrams(Solution.strs))
print(solution.groupAnagrams(Solution.strs))