from ast import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = []
        nums2 = []
        for i in range(len(nums)):
            nums1.append(nums[i])
            nums2.append(nums[i])
        return nums1 + nums2

def main():
    nums = [1,2,3,4,5,6]
    sol = Solution()
    print(sol.getConcatenation(nums=nums))

if __name__ == '__main__':
    main()