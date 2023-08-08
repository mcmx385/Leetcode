class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rem = purchaseAmount%10
        if rem>4:
            purchaseAmount+=10-rem
        else:
            purchaseAmount-=rem
        return 100-purchaseAmount
    
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rem = purchaseAmount%10
        return purchaseAmount+10-rem if rem>4 else purchaseAmount-rem
    
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 -(purchaseAmount+5)//10*10
    
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount//10+(purchaseAmount%10>4))*10
    
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return (104-purchaseAmount)//10*10