from ast import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        rank = {}

        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        result = [rank[num] for num in nums]

        return result

def main():
    nums = [8,1,2,2,3]

    sol = Solution()

    print(sol.smallerNumbersThanCurrent(nums))


if __name__ == '__main__':
    main()