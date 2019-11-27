from behave import given, when, then
# from ptest.assertion import assert_equals
from test.pages.homepage import HomePage
from test.pages.searchpage import SearchPage
from selenium import webdriver
import logging

@given (u'I am on homepage')
def i_am_on_homepage(context):
    url =  'https://buythisspace.com.au/'
    homepage = HomePage(context.driver)
    homepage.visit_page(url)
    assert True, homepage.is_title_matches()

@given (u'I am on searchpage')
def i_am_on_searchpage(context):
    url =  'https://buythisspace.com.au/search-page/?gmw_address[0]=sydney&gmw_distance=50&gmw_units=metric&gmw_form=1&gmw_per_page=51&gmw_lat=-33.8688197&gmw_lng=151.20929550000005&gmw_px=pt&action=gmw_post'
    searchpage = SearchPage(context.driver)
    searchpage.visit_page(url)
    assert True, searchpage.is_title_matches()



@when (u'I type "{location}" in the search input field on "{pageName}" page')
def i_type_location_input_in_the_search_input_field_on_page(context, location, pageName):
    page = ""
    if pageName =='homepage':
        page = HomePage(context.driver)
    elif pageName == 'searchpage':
        page = SearchPage(context.driver)

    assert True, page.is_search_input_field_displayed()
    print(page.pageTitle)
    page.field_in_search_input_filed(location)




@when (u'I click the search button on "{pageName}" page')
def i_click_the_search_button(context, pageName):
    page = ""
    if pageName == 'homepage':
        page = HomePage(context.driver)
    elif pageName == 'searchpage':
        page = SearchPage(context.driver)

    assert True, page.is_search_button_displayed()
    page.click_search_button()

@then (u'I Should be on the search result page')
def i_should_on_the_search_page(context):
    searchpage = SearchPage(context.driver)
    logging.info(context.driver.title)

    assert True, searchpage.is_title_matches()

    #####
    from time import sleep
    sleep(5)
    #####

    # raise NotImplementedError(u'STEP: I Should be on the search result page')


@then(u'I should be able to get status codes')
def i_should_be_able_to_get_status_codes(context):
    homepage = HomePage(context.driver)
    assert True, homepage.is_title_matches()
    ##############
    # import requests
    # r = requests.get(homepage.homepageUrl, allow_redirects=True)
    # print(r.status_code)
    # print("------------------------")
    # logging.info("######################")
    # logging.info(r.status_code)
    ##############
    # logs = context.driver.get_log('browser')
    # print(logs)

    # performance_log = context.driver.get_log('driver')
    # print(str(performance_log).strip('[]'))
    # logging.info("##################################")
    #
    # print("#########################################")
    # for entry in context.driver.get_log('browser'):
    #     print(entry)
    #     logging.info(entry)
    #
    # # print("#########################################")
    # logging.info(performance_log)
    # logging.info()















