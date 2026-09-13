class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for wrd in strs: 

            count = [0] * 26

            for c in wrd: 
                index = (ord(c) - ord("a"))
                count[index] += 1

            key = tuple(count)

            if key not in groups: 
                groups[key] = []

            groups[key].append(wrd)

        return list(groups.values())
                