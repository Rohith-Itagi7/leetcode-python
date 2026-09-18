class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_profit=prices[0]

        for val in prices:
            if val<min_profit:
                min_profit=val

            profit=val - min_profit

            if profit>max_profit:
                max_profit=profit
        return max_profit
