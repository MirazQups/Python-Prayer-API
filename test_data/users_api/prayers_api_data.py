from test_data.api_enpoints import *
from test_data.common_data import data_from_server
from test_data.headers import headers_post
from test_data.payloads import *


def response_get_prayer_times_calender():
    res = data_from_server("POST", test_url)
    return res.json(), res.status_code, headers_post, user_to_register


def response_get_prayer_times_calendar_by_address():
    res = data_from_server("GET", prayer_times_calendar_by_address)
    return res.json(), res.status_code


def response_get_prayer_times_calendar_by_city():
    res = data_from_server("GET", prayer_times_calendar_by_city)
    return res.json(), res.status_code


def response_get_prayer_times_calendar_by_hijri_calendar():
    res = data_from_server("GET", prayer_times_calendar_by_hijri_calendar)
    return res.json(), res.status_code


def response_get_prayer_times_hijri_calendar_by_address():
    res = data_from_server("GET", prayer_times_hijri_calendar_by_address)
    return res.json(), res.status_code


def response_get_prayer_times_hijri_calendar_by_city():
    res = data_from_server("GET", prayer_times_hijri_calendar_by_city)
    return res.json(), res.status_code


def response_get_current_date():
    res = data_from_server("GET", current_date)
    return res.json(), res.status_code

#
# def test():
#     """returns response and status for login with only email password"""
#     res = data_from_server("GET", test_url)
#     return res.json(), res.status_code
#
#
# def test_post():
#     """returns response and status for login with only email password"""
#     res = data_from_server("POST", test_post_url, headers_post, params=create)
#     return res.text, res.status_code
