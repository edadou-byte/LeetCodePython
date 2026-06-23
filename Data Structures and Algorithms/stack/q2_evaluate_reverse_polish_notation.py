from ast import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if  token not in ["+","-","*","/"]:
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val1 - val2)
                elif token == "*":
                    stack.append(val1 * val2)
                else:
                    stack.append(int(val1 / val2))

        return stack[-1]


def main():
    tokens = ["2","1","+","3","*"]
    tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    sol = Solution()

    print(sol.evalRPN(tokens2))


if __name__ == '__main__':
    main()