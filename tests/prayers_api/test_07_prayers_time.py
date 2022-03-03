import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get prayer month times')
def test_07_prayer_times_current_date():
    response_body, status_code = response_get_current_date()
    print(response_body)
    assert status_code == 200
