class Solution:
    def helper(self, arr, candidates, target):
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                self.final.append(arr+[candidate])
            elif target-candidate > 0:
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
            elif candidate > target:
                return
            elif target-candidate > 0:
                self.helper(arr+[candidate], candidates[i:], target-candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        candidates.sort()
        self.helper([], candidates, target)
        return self.final


class Solution:
    def helper(self, arr, candidates, index, target):
        for i in range(index, len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                self.final.append(arr+[candidate])
            elif candidate > target:
                return
            elif target-candidate > 0:
                self.helper(arr+[candidate], candidates, i, target-candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        candidates.sort()
        self.helper([], candidates, 0, target)
        return self.final
