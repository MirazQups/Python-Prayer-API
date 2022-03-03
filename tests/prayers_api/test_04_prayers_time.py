import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get this month prayer times')
def test_04_prayer_times():
    response_body, status_code = response_get_prayer_times_calendar_by_hijri_calendar()
    print(response_body)
    assert status_code == 200
