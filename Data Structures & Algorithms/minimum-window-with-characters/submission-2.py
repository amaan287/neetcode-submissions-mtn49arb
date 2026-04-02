class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t,window={},{}

        for c in t:
            count_t[c] = 1 + count_t.get(c,0)
        
        res,res_len=[-1,-1], float("inf")
        have,need=0,len(count_t)
        l=0
        for r,c in enumerate(s):
            window[c] = 1 + window.get(c,0)

            if c in count_t and window[c] == count_t[c]:
                have+=1
                while have == need:
                    if r-l+1 < res_len:
                        res,res_len=[l,r], r-l+1
                    left_char=s[l]
                    window[left_char] -= 1
                    if left_char in count_t and window[left_char] < count_t[left_char]:
                        have-=1
                    l+=1
        l,r= res

        return s[l:r+1] if res_len != float("inf") else ""