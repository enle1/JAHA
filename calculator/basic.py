class DivisionByZeroError(Exception):
    pass

class Calculator:
    def add(self, *args, **kwargs):
        result = sum(args)
        return round_result(result, kwargs.get('precision'))

    def subtract(self, *args, **kwargs):
        if len(args) < 2:
            raise ValueError("빼기에는 최소 두 개의 숫자가 필요합니다.")
        result = args[0] - sum(args[1:])
        return round_result(result, kwargs.get('precision'))

    def multiply(self, *args, **kwargs):
        result = 1
        for num in args:
            result *= num
        return round_result(result, kwargs.get('precision'))

    def divide(self, *args, **kwargs):
        if len(args) < 2:
            raise ValueError("나누기에는 최소 두 개의 숫자가 필요합니다.")
        for num in args[1:]:
            if num == 0:
                raise DivisionByZeroError("0으로 나눌 수 없습니다.")
        result = args[0]
        for num in args[1:]:
            result /= num
        return round_result(result, kwargs.get('precision'))