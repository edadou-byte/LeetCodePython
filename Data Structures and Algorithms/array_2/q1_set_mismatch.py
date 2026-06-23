from ast import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        # Trouver le doublon
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        # Trouver le nombre manquant
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]

def main():
    nums = [1,2,2,4]
    sol = Solution()

    print(sol.findErrorNums(nums))

if __name__ == '__main__':
    main()

