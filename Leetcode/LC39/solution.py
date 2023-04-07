class Solution:
    def helper(self, arr, candidates, target):
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                self.final.append(arr+[candidate])
            if target-candidate > 0:
                self.helper(arr+[candidate], candidates[i:], target-candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        self.helper([], candidates, target)
        return self.final


class Solution:
    def helper(self, arr, candidates, target):
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                self.final.append(arr+[candidate])
            if candidate > target:
                return
            if target-candidate > 0:
                self.helper(arr+[candidate], candidates[i:], target-candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        candidates.sort()
        self.helper([], candidates, target)
        return self.final

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final = []
        def helper(arr, candidates, target):
            for i in range(len(candidates)):
                candidate = candidates[i]
                if candidate == target:
                    final.append(arr+[candidate])
                if candidate > target:
                    return
                if target-candidate > 0:
                    helper(arr+[candidate], candidates[i:], target-candidate)
        helper([], candidates, target)
        return final
