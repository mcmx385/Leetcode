class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        arr=[0]*26
        for c in sentence:
            arr[ord(c)-ord('a')]+=1
        return 0 not in arr

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        arr=[0]*26
        for c in sentence:
            arr[ord(c)-ord('a')]+=1
        return sum(arr)==26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in sentence:
                return False
        return True

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
    
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mapp={val:False for val in 'abcdefghijklmnopqrstuvwxyz'}
        for c in sentence:
            mapp[c]=True
        return all(mapp.values())
    
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set("abcdefghijklmnopqrstuvwxyz")==set(sentence)