from fractions import Fraction


def convert(number: int):
    integer_part = int(number)
    fractional_part = number - integer_part

    fraction = Fraction(fractional_part).limit_denominator()

    if fraction.numerator == 0:
        return f"{integer_part}"
    else:
        return f"{integer_part} {fraction.numerator}/{fraction.denominator}"
