from ast import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for pair in zip(nums[:n], nums[n:]) for x in pair]

def main():
    nums = [1,2,3,4,5,6]
    sol = Solution()
    print(sol.shuffle(nums=nums, n=3))

if __name__ == '__main__':
    main()