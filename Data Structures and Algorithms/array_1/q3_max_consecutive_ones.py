from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = []
        current = []

        for i in nums:
            if i == 1:
                current.append(i)
            elif current:
                result.append(current)
                current = []

        if current:
            result.append(current)

        return max((len(x) for x in result), default=0)

def main():
    nums = [1, 1, 0, 1, 1, 1]
    sol = Solution()

    print(sol.findMaxConsecutiveOnes(nums=nums))

if __name__ == '__main__':
    main()