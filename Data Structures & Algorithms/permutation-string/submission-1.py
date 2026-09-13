class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False 

        countS1 = {}
        window_count = {}
        
        for char in s1: 
            countS1[char] = countS1.get(char, 0) + 1

        left = 0 

        for right in range(len(s2)):

            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1
            
            if countS1 == window_count:
                return True 
        return False