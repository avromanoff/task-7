

def polish_func():
    operators = ['+', '-', '*', '/']
    no_space = ' '.join(polish_string.split())   # удаление лишних пробелов в веденной строке
    polish_elements = no_space.split(' ')
    operator = polish_elements[0]
    try:
        assert operator in operators
    except AssertionError:
        return 'Указан неправильный оператор.'
    try:
        operand_1 = float(polish_elements[1])
        operand_2 = float(polish_elements[2])
    except ValueError:
        return 'Вместо чисел введено что-то еще.'
    if len(polish_elements) > 3:
        return 'Введено слишком много значений.'
# Непонятно, как использовать try-except для большого количества значений, как сгенерить системную ошибку
    result = 0
    if operator == '+':
        result = operand_1 + operand_2
    elif operator == '-':
        result = operand_1 - operand_2
    elif operator == '*':
        result = operand_1 * operand_2
    elif operator == '/':
        try:
            result = operand_1 / operand_2
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'
    return result


polish_string = input('Введите арифметический оператор, а затем 2 числа через пробел ')
print(polish_func())
