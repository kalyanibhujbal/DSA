class Solution:
    def maxProfit(self,prices):
        minPrice=prices[0]
        maxProfit=0

        for price in prices:

            if price < minPrice :
                minPrice= price

            profit=price - minPrice

            if profit > maxProfit :
                maxProfit= profit
        
        return maxProfit

#Approach -
#This problem uses the Sliding Window / Two Pointer (Greedy) pattern because we only need to track the minimum buying price seen so far.
#Keep track of Minimum buying price and Maximum profit
#Whenever a smaller price comes, update minimum. whenever larger profit comes, update profit.
        
#Time Complexity - O(n) - One loop
#Space Complexity - O(1) -Only two variables


