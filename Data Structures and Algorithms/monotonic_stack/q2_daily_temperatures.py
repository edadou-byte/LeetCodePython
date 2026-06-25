from ast import List


class Solution:
    def dailyTemperaturesV1(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        n = len(temperatures)

        for i in range(n):
            stack = temperatures[i+1:]

            for idx, val in enumerate(stack):
                if val > temperatures[i]:
                    res[i] = idx+1
                    break
        return res


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
        return res



def main():
    temperatures = [73,74,75,71,69,72,76,73]

    sol = Solution()

    print(sol.dailyTemperatures(temperatures=temperatures))


if __name__ == '__main__':
    main()