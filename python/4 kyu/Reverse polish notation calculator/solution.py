def calc(expr):
    array = expr.split()
    if len(array) == 0:
        return 0

    index = 0
    while index < len(array):
        if array[index] in "+-*/":
            num1 = float(array.pop(index-2))
            num2 = float(array.pop(index-2))
            index -= 2
            result = 0
            if array[index] == "+":
                result = num1 + num2
            elif array[index] == "-":
                result = num1 - num2
            elif array[index] == "*":
                result = num1 * num2
            elif array[index] == "/":
                result = num1 / num2
            else:
                print ("HOW!1!")
            array[index] = result
        index += 1
    return float(array[len(array)-1])
