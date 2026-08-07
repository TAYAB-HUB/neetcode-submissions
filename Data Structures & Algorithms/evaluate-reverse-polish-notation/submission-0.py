class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in tokens:
            if i == '+' :
                numbers.append(numbers.pop() + numbers.pop())
            elif i == '-' :
                second , first = numbers.pop(),numbers.pop()
                numbers.append(first - second)
            elif i == '*' :
                numbers.append(numbers.pop() * numbers.pop())
            elif i == '/' :
                second , first = numbers.pop(),numbers.pop()
                numbers.append(int(first/second))
            else:
                numbers.append(int(i))
        return numbers[0]

        