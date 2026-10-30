class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else: # bill == 20
                # Try to give change using one $10 bill and one $5 bill first
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # Otherwise, try to give change using three $5 bills
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
        return True