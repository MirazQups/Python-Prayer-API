import requests


def data_from_server(method="", endpoint="", headers="", params=""):
    # pull data from api
    res = requests.request(method, endpoint, headers=headers, data=params)
    return res

