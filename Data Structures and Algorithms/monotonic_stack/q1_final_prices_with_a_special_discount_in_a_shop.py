from ast import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]
        stack = []
        n = len(prices)

        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                price = stack.pop()
                res[price] -= prices[i]
            stack.append(i)
        return res



def main():
    prices = [8,4,6,2,3]

    sol = Solution()

    print(sol.finalPrices(prices=prices))


if __name__ == '__main__':
    main()