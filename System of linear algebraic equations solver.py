def solve(number_of_variables, number_of_equations):
    matrix = []
    ans = []
    for i in range(number_of_equations):
        matrix.append(list(map(lambda x: float(x), input().split())))
        if len(matrix[-1]) != number_of_variables + 1:
            return "Некорректный ввод. Количество переменных не совпадает с количеством введённых коэффициентов."
    for i in range(len(matrix[0]) - 1):
        check = []
        for j in range(len(matrix)):
            check.append(matrix[j][i])
        if check == [0] * len(matrix):
            return "Неверно задана система уравнений. Во всех уравнениях один из коэффициентов равен 0."
    if independence_check(matrix) < number_of_variables:
        return "Система уравнений имеет бесконечное множество решений"
    while matrix[0][0] == 0:
        matrix = matrix[1:] + [matrix[0]]
    matrix = format(matrix, number_of_variables)[::-1]
    for i in range(len(matrix)):
        ans = ans + [(matrix[i][-1] - summ_of_string(ans, matrix[i])) / matrix[i][len(matrix[i]) - i - 2]]
    return ans[::-1]


def format(matrix, number):
    for i in range(1, len(matrix)):
        coeff = matrix[i][len(matrix[0]) - number - 1] / matrix[0][len(matrix[0]) - number - 1]
        for j in range((len(matrix[0]))):
            matrix[i][j] = matrix[i][j] - matrix[0][j] * coeff
    if len(matrix) > 2:
        matrix = [matrix[0]] + format(matrix[1:], number - 1)
    return matrix


def summ_of_string(ans, string):
    ot = 0
    for i in range(len(ans)):
        ot += string[len(string) - i - 2] * ans[i]
    return ot


def independence_check(matrix):
    indep = [matrix[0]]
    for i in range(1, len(matrix)):
        for j in range(len(indep)):
            coefficients = []
            for k in range(len(matrix[i])):
                coefficients.append(matrix[i][k] / indep[j][k])
            if coefficients != coefficients[0] * len(coefficients):
                indep.append(matrix[i])
    return len(indep)


print(solve(int(input()), int(input())))
