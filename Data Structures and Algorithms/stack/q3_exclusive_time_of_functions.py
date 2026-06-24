from ast import List


class Solution:

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        res = [0] * n
        pre = 0

        for log in logs:
            i, operation, time = log.split(':')
            id, current = int(i), int(time)

            if operation == 'start':
                if stack:
                    res[stack[-1]] += current - pre
                stack.append(id)
                pre = current
            else:
                res[stack.pop()] += current - pre + 1
                pre = current + 1
        return res


def main():
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    n = 1

    sol = Solution()

    print(sol.exclusiveTime(n=n, logs=logs))


if __name__ == '__main__':
    main()