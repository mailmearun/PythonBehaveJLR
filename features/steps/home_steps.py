import time
import requests
from behave import *
import logging

from features.pages.HomePage import HomePage
from utils.LogFile import Logger



log = Logger(__name__, logging.INFO)

@given(u'user launch the url')
def step_impl(context):
    log.logger.info('Given user launch the url')
    HomePage(context.driver).launh_url()
    time.sleep(10)



@when(u'verify the home page title is {title}')
def step_impl(context, title):
    log.logger.info('When verify the home page title is ""')
    act_title = HomePage(context.driver).verifyPageTitle()
    assert title == act_title


@when(u'user click on Company Tab')
def step_impl(context):
    log.logger.info('When user click on Company Tab')
    HomePage(context.driver).clickCompanyTab()


@then(u'user is able to verify the below links under Company Tab')
def step_impl(context):
    log.logger.info('Then user is able to verify the below links under Company Tab')
    list_links = []
    for row in context.table:
        list_links.append(row[0])
    HomePage(context.driver).verifyLinks(list_links)


@given(u'Execute Get API using endpoint {endpoint}')
def step_impl(context, endpoint):
    log.logger.info('Given Execute Get API using endpoint ""')
    res = requests.get(endpoint)
    context.response = res
    context.status = res.status_code


@when(u'verify the response code is {sts_code}')
def step_impl(context, sts_code):
    log.logger.info('When verify the response code is \'200\'')
    assert context.status == sts_code


@then(u'verify the pet id in response')
def step_impl(context):
    print(u'STEP: Then verify the pet id in response')
    print(context.response)
