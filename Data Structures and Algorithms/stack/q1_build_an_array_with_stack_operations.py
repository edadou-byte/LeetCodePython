from ast import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        j = 0

        for i in range(1, n+1):
            if j >= len(target):
                break

            result.append("Push")

            if i == target[j]:
                j += 1
            else:
                result.append("Pop")

        return result

def main():

    nums = [1,2,3]
    n = 3
    
    sol = Solution()

    print(sol.buildArray(nums, n=n))


if __name__ == '__main__':
    main()