class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []

        for start, end in intervals:
            # If ans is empty or no overlap, start a new interval
            if not ans or start > ans[-1][1]:
                ans.append([start, end])
            else:
                # Overlap: extend the last interval's end if needed
                ans[-1][1] = max(ans[-1][1], end)

        return ans