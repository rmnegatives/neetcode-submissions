from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count module
        # ans_list = Counter(nums)
        # return [ key for key,value in ans_list.most_common(k)]
        # --------------------------------------------
        # or loop through make map of num -> freq
            # dict_ = {}
            # for num in nums:
            #     dict_[num] = 1 + dict_.get(num,0)
        # sort
            # sorted_keys = sorted(dict_, key=dict_.get, reverse=True)
            # return sorted_keys[0:k]
        # min_heap
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        return [num for num, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]

        