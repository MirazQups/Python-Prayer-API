import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get dates prayer times')
def test_04_prayer_times():
    response_body, status_code = response_get_prayer_times_hijri_calendar_by_address()
    print(response_body)
    assert status_code == 200
