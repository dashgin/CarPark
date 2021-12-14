from django.core.validators import RegexValidator


def plate_number_validator(value):
    """
    validate if string format is `AA 1234 OO`
    """
    regex = r"^[A-Z]{2} \d{4} [A-Z]{2}$"
    validator = RegexValidator(regex=regex, message="Invalid plate number format")
    validator(value)
