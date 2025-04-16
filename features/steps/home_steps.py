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
    log.logger.info('When verify the home page title is ' + title)
    act_title = HomePage(context.driver).verifyPageTitle()
    assert title == act_title


@when(u'user hover on Company Tab')
def step_impl(context):
    log.logger.info('When user click on Company Tab')
    HomePage(context.driver).moveToCompanyTab()


@then(u'user is able to verify the below links under Company Tab')
def step_impl(context):
    log.logger.info('Then user is able to verify the below links under Company Tab')
    list_links = []
    for row in context.table:
        list_links.append(row[0])
    print(list_links)
    act_list = HomePage(context.driver).verifyLinks()


@then(u'click and verify the link {link} under Company Tab')
def step_impl(context, link):
    print(u'STEP: Then click and verify the link Enterprise under Company Tab')
    print(link)
    act_link = HomePage(context.driver).verifyLinkNavigation(link)
    print(act_link)
    assert link == act_link
