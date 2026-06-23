from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result

def main():

    nums = [4,3,2,7,8,2,3,1]

    sol = Solution()

    print(sol.findDisappearedNumbers(nums))


if __name__ == '__main__':
    main()