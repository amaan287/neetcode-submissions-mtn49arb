class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        j = sorted(count.values(), reverse=True)
        kth = j[k - 1]
        for num, freq in count.items():
            if freq >= kth and len(res) < k:
                res.append(num)
        return res