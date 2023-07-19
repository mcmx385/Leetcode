class Solution:
    def helper(self, arr, k):
        allres = []
        if len(arr) == 1:
            return [arr]
        for i in arr:
            remain = arr.copy()
            remain.remove(i)
            res = self.helper(remain, k)
            for r in res:
                if len(r) == k:
                    allres += res
                else:
                    for j in range(len(r)):
                        ret = r[:j] + [i] + r[j:]
                        ret.sort()
                        allres.append(ret)
        return allres

    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        res = self.helper(arr, k)
        return list(set(map(tuple, res)))


class Solution:
    def helper(self, arr, k):
        allres = []
        if len(arr) == 1:
            return [arr]
        if k == 1:
            return [[i] for i in arr]
        for i in arr:
            remain = arr.copy()
            remain.remove(i)
            res = self.helper(remain, k - 1)
            for r in res:
                for j in range(len(r)):
                    ret = r[:j] + [i] + r[j:]
                    ret.sort()
                    allres.append(ret)
        return allres

    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        res = self.helper(arr, k)
        return list(set(map(tuple, res)))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(arr, k, path):
            if k == 0:
                res.append(path)
                return
            for i in range(len(arr)):
                helper(arr[i + 1 :], k - 1, path + [arr[i]])

        helper([i for i in range(1, n + 1)], k, [])
        return res
