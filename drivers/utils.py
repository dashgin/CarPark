from datetime import date


def string_to_date(string):
    """
    function for convert `16-1-2021` string format to `YYYY-MM-DD` format for using in query
    """
    reversed_string = string[::-1]
    splitted_string = reversed_string.split("-")
    integer_list = list(map(int, splitted_string))
    filter_date = date(*integer_list)
    return filter_date
