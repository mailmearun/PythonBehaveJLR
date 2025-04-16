import time
import requests
from behave import *
import logging

from utils.Config import ReadConfig
from utils.LogFile import Logger

log = Logger(__name__, logging.INFO)


@given(u'Execute Get API using endpoint {endpoint}')
def step_impl(context, endpoint):
    log.logger.info('Given Execute Get API using endpoint')
    global response
    endpoint = ReadConfig.getValue("basic","api_endpoint")+endpoint.replace('"','')
    response = requests.get(endpoint)


@when(u'verify the response code is {sts_code}')
def step_impl(context, sts_code):
    log.logger.info('When verify the response code is 200')
    code = sts_code.replace('"','')
    assert response.status_code == int(code)
    if response.status_code == int(code):
        assert True
    else:
        assert response.json()['code'] == 1
        assert response.json()['type'] == "error"
        assert response.json()['error'] == "Pet not found"
        print("API Execution Failed with status code "+str(response.status_code))
        assert False


@then(u'verify the data in response')
def step_impl(context):
    log.logger.info(u'STEP: Then verify the pet id in response')
    parsed_res = response.json()
    assert parsed_res['id'] == int(context.table[0][0])
    # assert parsed_res['name'] == context.table[0][1]
    assert parsed_res['status'] == context.table[0][2]


