class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_char,t_char={},{}
        for i in range(len(s)):
            s_char[s[i]]=1+s_char.get(s[i],0)
            t_char[t[i]]=1+t_char.get(t[i],0)
        for c in s_char:
            if s_char[c]!=t_char.get(c,0):
                return False
        return True

