def round_result(value, precision):
    """지정된 정밀도로 값을 반올림하는 함수입니다."""
    return round(value, precision)

def convert_to_radians(angle, unit):
    """각도를 라디안으로 변환하는 함수입니다."""
    if unit == 'degree':
        return math.radians(angle)
    return angle