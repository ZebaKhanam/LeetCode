class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        for i in strs:
            hashmap[len(i)] = i
        pr = ""
        hash1 = min(hashmap)
        for j in range(hash1):
            my_ids = [idx[j] for idx in strs]
            result = my_ids.count(my_ids[0]) == len(my_ids)
            if result == False:
                break
            pr = pr + my_ids[0]
        return pr
