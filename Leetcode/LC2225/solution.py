class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mapp={}
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in mapp:
                mapp[winner]=0
            if loser not in mapp:
                mapp[loser]=1
            else:
                mapp[loser]+=1
        nolose=[]
        onelost=[]
        for key, val in mapp.items():
            if val==0:
                nolose.append(key)
            elif val==1:
                onelost.append(key)
        return [sorted(nolose),sorted(onelost)]

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = zip(*matches)
        return [sorted(set(win) - set(lose)), sorted(set(lose) - set(win))]
    
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:        
        return (lambda win,lose:[sorted(set(win)-set(lose)),sorted(k for k,v in Counter(lose).items() if v==1)])(*zip(*matches))