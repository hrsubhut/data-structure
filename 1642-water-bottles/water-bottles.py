class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        n = numBottles
        result = n
        n1 = 0

        while n >= numExchange:

            n1 = n// numExchange
            result += n1
            n = n1+ n % numExchange

        return result

        