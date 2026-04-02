class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_len,s2_len= len(s1),len(s2)
        s1_count,s2_count=[0] * 26, [0] * 26

        for i in range(s1_len):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(s1_len,s2_len):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - s1_len]) - ord('a')] -= 1

        return s1_count == s2_count
