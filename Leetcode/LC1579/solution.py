class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr = colors[0]
        times = []
        total = 0
        for index, color in enumerate(colors):
            if color != curr:
                times.remove(max(times))
                total += sum(times)
                times.clear()
                curr = color
            times.append(neededTime[index])
        times.remove(max(times))
        total += sum(times)
        return total
