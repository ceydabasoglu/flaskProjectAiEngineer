class MathTool:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ValueError("Divide by zero error!")
        return num1 / num2

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def sqrt(num):
        if num < 0:
            raise ValueError("Square root of negative number cannot be taken!")
        return num ** 0.5
