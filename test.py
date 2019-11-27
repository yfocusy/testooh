import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

geckodriver_path = "/Users/yuli510/Downloads/chromedriver"

caps = DesiredCapabilities.CHROME
# caps['loggingPrefs'] = {'performance': 'ALL'}
caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}

# driver = webdriver.Remote(
# command_executor='http://127.0.0.1:5555/wd/hub',
# desired_capabilities=caps
# )

url =  'https://buythisspace.com.au/'
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=geckodriver_path)
driver.get(url)
logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]

print(logs)
with open('performance.json', 'wt') as file:
    json.dump(logs, file)


driver.close()