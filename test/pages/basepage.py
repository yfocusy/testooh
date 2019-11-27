"""
BasePage class initialise the base page that will be called from all pages
"""

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

        self.pageTitle = ""



    def visit_page(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def is_title_matches(self):
        return self.pageTitle in self.driver.title


