from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapp={}
        for char in magazine:
            if char not in mapp:
                mapp[char]=0
            mapp[char]+=1
        for char in ransomNote:
            if char not in mapp or mapp[char]==0:
                return False
            mapp[char]-=1
        return True
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1=Counter(ransomNote)
        counter2=Counter(magazine)
        return not counter1-counter2

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1=Counter(ransomNote)
        counter2=Counter(magazine)
        return all(counter1[char]<=counter2[char] for char in counter1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1=Counter(ransomNote)
        counter2=Counter(magazine)
        return counter1 & counter2 == counter1