class Solution:
    def helper(self, arr, candidates, index, target, length):
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            candidate = candidates[i]
            if candidate == target and length == 1:
                if arr + [candidate] not in self.final:
                    self.final.append(arr + [candidate])
            elif candidate > target:
                return
            elif target - candidate > 0 and length > 1:
                self.helper(
                    arr + [candidate], candidates, i + 1, target - candidate, length - 1
                )

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.final = []
        candidates = [i for i in range(1, 10)]
        self.helper([], candidates, 0, n, k)
        return self.final
