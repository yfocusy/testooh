from selenium import webdriver
from behave.log_capture import capture


GEO = 'data:application/json,{"location":{"lat":22.893,"lng":72.4095},"accuracy": 100.0}'

@capture
def before_feature(context, feature):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('geo.enabled',True)
    profile.set_preference('geo.prompt.testing', True)
    profile.set_preference('geo.prompt.testing.allow', True)
    profile.set_preference('geo.wifi.uri',GEO)

    # context.browser.set_page_load_timeout(10)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:5555/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        browser_profile=profile
    )

@capture
def after_feature(context, feature):
    context.driver.quit()
    # context.browser.quit()


@capture
def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()
    # -- ALTERNATIVE: Setup logging with a configuration file.
    # context.config.setup_logging(configfile="behave_logging.ini")

# def after_all(context):
#     context.browser.quit()