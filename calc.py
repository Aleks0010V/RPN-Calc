def calculate(num1, num2, sing):
    if sing is '+':
        return num2 + num1
    elif sing is '*':
        return num2 * num1
    elif sing is '-':
        return num2 - num1
    elif sing is '/':
        return num2 / num1

def rpn(s):
    nums = list()
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    sings = list()
    for el in s:
        try:
            el = float(el)
            nums.append(el)
        except:
            if el not in '+-*/()|':
                print('Incorrect operator')
                quit()
            elif el == '|':
                while len(sings) > 0:
                    nums.append(sings.pop())
                break;
            elif len(sings) == 0 or el == '(' or sings[-1] == '(':
                sings.append(el)
            elif el == ')':
                while True:
                    if sings[-1] == '(':
                        sings.pop()
                        break
                    else:
                        nums.append(sings.pop())
            elif len(sings) >= 1 and priority.get(el) > priority.get(sings[-1]):
                sings.append(el)
            elif len(sings) >= 1 and priority.get(el) <= priority.get(sings[-1]):
                while(len(sings) >= 1 and priority.get(el) <= priority.get(sings[-1])):
                    if sings[-1] != '(':
                        nums.append(sings.pop())
                    else:
                        break
                sings.append(el)
    return nums

def solve(nums):
    result = list()
    while len(nums) > 0:
        result.append(nums.pop(0))
        if result[-1] == '+' or result[-1] == '*' or result[-1] == '-' or result[-1] == '/':
            num2 = result.pop(-3)
            num1 = result.pop(-2)
            sing = result.pop()
            result.append(calculate(num1, num2, sing))
    return result[0]

def main():
    s = input('>>> ')
    s = s.split()
    s.append('|')
    diff = rpn(s)
    result = solve(diff)
    print(result)

def calc(s):
    s = s.split()
    s.append('|')
    diff = rpn(s)
    result = solve(diff)
    return result

if __name__ == '__main__':
    main()
