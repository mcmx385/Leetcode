class Solution:
    def helper(self, arr, candidates, target):
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                self.final.append(arr + [candidate])
            elif candidate > target:
                return
            elif target - candidate > 0:
                self.helper(arr + [candidate], candidates[i + 1 :], target - candidate)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        candidates.sort()
        self.helper([], candidates, target)
        self.final = [tuple(x) for x in self.final]
        self.final = set(self.final)
        self.final = [list(x) for x in self.final]
        return self.final


class Solution:
    def helper(self, arr, candidates, index, target):
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            candidate = candidates[i]
            if candidate == target:
                if arr + [candidate] not in self.final:
                    self.final.append(arr + [candidate])
            elif candidate > target:
                return
            elif target - candidate > 0:
                self.helper(arr + [candidate], candidates, i + 1, target - candidate)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.final = []
        candidates.sort()
        self.helper([], candidates, 0, target)
        return self.final
