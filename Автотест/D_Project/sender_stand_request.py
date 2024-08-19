import configuration

import requests

import data


def create_new_order(body):
    current_headers = data.headers.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                  json=body,
                  headers=current_headers)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, {'t':track})
