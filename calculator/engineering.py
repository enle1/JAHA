import math
from basic import Calculator

class DivisionByZeroError(Exception):
    pass

class EngineeringCalculator(Calculator):
    """공학적 기능을 추가한 계산기 클래스입니다."""
    
    def square_root(self, x, **kwargs):
        # 제곱근
        result = math.sqrt(x)
        return self._format_result(result, **kwargs)

    def power(self, x, y, **kwargs):
        # 거듭제곱
        result = math.pow(x, y)
        return self._format_result(result, **kwargs)

    def log(self, x, base=10, **kwargs):
        # 로그
        result = math.log(x, base)
        return self._format_result(result, **kwargs)

    def sin(self, x, angle_unit='radian', **kwargs):
        # 사인
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.sin(x)
        return self._format_result(result, **kwargs)

    def cos(self, x, angle_unit='radian', **kwargs):
        # 코사인
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.cos(x)
        return self._format_result(result, **kwargs)

    def tan(self, x, angle_unit='radian', **kwargs):
        # 탄젠트
        if angle_unit == 'degree':
            x = math.radians(x)
        result = math.tan(x)
        return self._format_result(result, **kwargs)

    def divide(self, *args, **kwargs):
        if args[1] == 0:
            raise DivisionByZeroError("Division by zero is not allowed")
        return super().divide(*args, **kwargs)