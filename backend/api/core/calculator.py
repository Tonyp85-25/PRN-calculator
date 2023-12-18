from queue import LifoQueue


class Calculator:
    @staticmethod
    def calculate(expression: str):
        stack = LifoQueue()
        for i in expression.split():
            if i.isdigit():
                stack.put(float(i))
            elif i in "+-*/^":
                num2 = stack.get()
                num1 = stack.get()
                if i == "+":
                    stack.put(num1 + num2)
                elif i == "-":
                    stack.put(num1 - num2)
                elif i == "*":
                    stack.put(num1 * num2)
                elif i == "/":
                    try:
                        stack.put(num1 / num2)
                    except ZeroDivisionError:
                        return "Error: Division by zero"
                    stack.put(num1 / num2)
                elif i == "^":
                    stack.put(num1**num2)
        return stack.get()
