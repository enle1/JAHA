class ComplexCalculator:
    """복소수 연산을 위한 클래스입니다."""

    @staticmethod
    def add(a, b):
        """복소수 덧셈."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """복소수 뺄셈."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """복소수 곱셈."""
        return a * b

    @staticmethod
    def divide(a, b):
        """복소수 나눗셈."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def magnitude(complex_num):
        """복소수의 절대값 계산."""
        return abs(complex_num)

    @staticmethod
    def argument(complex_num):
        """복소수의 편각 계산."""
        return cmath.phase(complex_num)

    @staticmethod
    def to_cartesian(r, theta):
        """극 좌표를 직교 좌표계로 변환."""
        return r * cmath.cos(theta), r * cmath.sin(theta)

    @staticmethod
    def to_polar(x, y):
        """직교 좌표계를 극 좌표로 변환."""
        return abs(complex(x, y)), cmath.phase(complex(x, y))