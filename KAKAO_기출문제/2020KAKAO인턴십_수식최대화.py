import sys

input = sys.stdin.readline


# 연산식과 계산할 operator를 전달해여 해당 operator만 계산해 나온 expression을 Return
def calculate(list_exp, op):
    new_exp = []
    idx = 0
    while idx < len(list_exp):
        if list_exp[idx] != op:
            new_exp.append(list_exp[idx])
            idx += 1
        else:
            if op == "*":
                new_exp[-1] = new_exp[- 1] * list_exp[idx + 1]
            elif op == "+":
                new_exp[-1] = new_exp[- 1] + list_exp[idx + 1]
            else:
                new_exp[-1] = new_exp[- 1] - list_exp[idx + 1]
            idx += 2
    return new_exp


def solution(expression):
    list_exp = []
    start = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            list_exp.append(int(expression[start:i]))
            list_exp.append(expression[i])
            start = i + 1
    list_exp.append(int(expression[start:]))

    first_mul = calculate(list_exp, "*")
    first_plus = calculate(list_exp, "+")
    first_min = calculate(list_exp, "-")

    mul_plus = calculate(first_mul, "+")
    mul_plus = calculate(mul_plus, '-')[0]
    mul_min = calculate(first_mul, "-")
    mul_min = calculate(mul_min, "+")[0]
    del first_mul

    plus_mul = calculate(first_plus, "*")
    plus_mul = calculate(plus_mul, '-')[0]
    plus_min = calculate(first_plus, "-")
    plus_min = calculate(plus_min, "*")[0]
    del first_plus

    min_mul = calculate(first_min, "*")
    min_mul = calculate(min_mul, "+")[0]
    min_plus = calculate(first_min, "+")
    min_plus = calculate(min_plus, "*")[0]
    del first_min

    answer = max(list(map(abs, [mul_plus, mul_min, plus_mul, plus_min, min_mul, min_plus])))
    return answer